import time
import functools

__version__ = '1.2'


def handle_error(number_of_attempts: int = 5,
                 time_to_sleep: int = 30,
                 errors_to_catch: tuple = (Exception, ),
                 callback=None):
    def handle_error_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt_number in range(number_of_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except errors_to_catch as ex:
                    time.sleep(time_to_sleep)
            if callback:
                callback(ex)
            raise ex
        return wrapper
