import time

__version__ = '1.2'


def wrap(func, times_to_try: int = 5, time_to_sleep: int = 30, errors_to_catch: tuple = (Exception), callback = None):
    def error_handle(*args, **kwargs):
        print(';ddd')
        times = 0
        while True:
            try:
                return func(*args, **kwargs)
            except errors_to_catch as e:
                if not times > times_to_try:
                    time.sleep(time_to_sleep)
                    times += 1
                else:
                    if callback:
                        callback(e)
                    raise e
    return error_handle
