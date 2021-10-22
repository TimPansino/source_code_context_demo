from flask import Flask
import requests
import sys

from newrelic.api.profile_trace import ProfileTrace
from newrelic.common.object_wrapper import transient_function_wrapper, function_wrapper

app = Flask(__name__)

class MyClass(object):
    def my_func(self):
        return
    
    def __call__(self):
        return


@app.route('/')
def hello_world():
    req = requests.get('http://localhost:8000/external')
    req.raise_for_status()

    call_me()  # Maybe

    return " ".join(("Hello World!", req.text))


@app.route('/error')
def error():
    raise ValueError("1 != 0")


@app.route('/external')
def external_func():
    return "Hello, fellow humans!\n"


@app.route('/external/error')
def external_error():
    req = requests.get('http://localhost:8000/error')
    req.raise_for_status()

    return req.text


def call_me(i=3):
    if i <= 0:
        return other_function()
    return call_me(i-1)


def other_function():
    print("Hello")
    return 3


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
