import time
import functools
def function_timer(_func=None,*, mode=True):
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if mode == False:
                value = func(*args, **kwargs)
                return value
            start = time.perf_counter()
            value = func(*args, **kwargs)
            end = time.perf_counter()
            times = end - start
            print(f"Function {func.__name__!r} takes {times:.7f} secs")
            return value
        return wrapper
    if _func == None:
        return timer
    else:
        return timer(_func)
def database_exist(_func=None,*,mode=True):
    pass