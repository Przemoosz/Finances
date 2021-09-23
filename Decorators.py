import time
import functools
import psycopg2

'''This is decorators.py
    I added two decorators but one is used mostly its function_timer
    It measures time the function is executed and shows time using ptint function
    There is also database_exist decorator which control if the databes finanse exists'''


def function_timer(_func=None, *, mode=True):
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
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


def database_exist(_func=None, *, password=None):
    def inner_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if password is None:
                val = func(*args, **kwargs)
                return val
            else:
                with psycopg2.connect(host="localhost", user='postgres', password=password, port=5432) as conn:
                    with conn.cursor() as curs:
                        curs.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname='finanse';")
                        dblist = curs.fetchall()
                        if dblist != [] and dblist[0][0] == 'finanse':
                            print("Everything OK")
                        else:
                            print("Database does not exists! Create database 'finanse' using your psql console!")
                            return False
                val = func(*args, **kwargs)
                return val

        return wrapper

    if _func is None:
        return inner_func
    else:
        return inner_func(_func)
    pass
