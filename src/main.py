
from routes.app import app
import sys

from newrelic.api.profile_trace import ProfileTrace
from newrelic.common.object_wrapper import transient_function_wrapper, function_wrapper


def main():
    # Force DT to sample all traces
    @function_wrapper
    def dt_enabled(wrapped, instance, args, kwargs):
        @transient_function_wrapper("newrelic.core.adaptive_sampler", "AdaptiveSampler.compute_sampled")
        def force_sampled(wrapped, instance, args, kwargs):
            wrapped(*args, **kwargs)
            return True

        wrapped = force_sampled(wrapped)

        return wrapped(*args, **kwargs)  # pylint: disable=E1102

    @dt_enabled
    def _main():
        # Set profile tracer to instrument all function calls (max depth 100)
        sys.setprofile(ProfileTrace(100))
        app.run(host='0.0.0.0', port=8000)

    _main()

if __name__ == "__main__":
    main()
