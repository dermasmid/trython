import time
import functools

__version__ = '1.2'


def wrap(
    func: callable = None,
    number_of_attempts: int = 5,
    time_to_sleep: int = 30,
    errors_to_catch: tuple = (Exception, ),
    callback=None
    ):

    def _decorate(func):

        @functools.wraps(func)
        def wrapped_function(*args, **kwargs):
            attempt_number = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except errors_to_catch as e:
                    if not attempt_number > number_of_attempts:
                        time.sleep(time_to_sleep)
                        attempt_number += 1
                    else:
                        if callback:
                            callback(e)
                        raise e
        return wrapped_function

    if func:
        return _decorate(func)

    return _decorate
