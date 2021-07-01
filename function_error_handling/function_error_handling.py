import time
import functools
from contextlib import contextmanager



def wrap(
    func: callable = None,
    number_of_attempts: int = 5,
    time_to_sleep: int = 30,
    errors_to_catch: tuple = (Exception, ),
    validator: callable = None,
    callback=None
    ):

    def _decorate(func):

        @functools.wraps(func)
        def wrapped_function(*args, **kwargs):
            attempt_number = 0
            error = None
            while True:
                try:
                    result = func(*args, **kwargs)
                except errors_to_catch as e:
                    error = e
                else:
                    try:
                        if validator:
                            assert validator(result)
                    except Exception as e:
                        if isinstance(e, AssertionError):
                            error = ValueError('Validator function returned false.')
                        else:
                            error = e
                    else:
                        return result

                if attempt_number > number_of_attempts:
                    if callback:
                        callback(error)
                    raise error
                attempt_number += 1
                time.sleep(time_to_sleep)

        return wrapped_function

    if func:
        return _decorate(func)

    return _decorate



@contextmanager
def context_wrap(
    func: callable = None,
    number_of_attempts: int = 5,
    time_to_sleep: int = 30,
    errors_to_catch: tuple = (Exception, ),
    validator: callable = None,
    callback=None
    ):
    yield wrap(func, number_of_attempts, time_to_sleep, errors_to_catch, validator, callback)
