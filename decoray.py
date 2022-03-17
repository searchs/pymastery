from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Took {t2 - t1} ms")
        return result

    return wrapper


@performance
def check_duration():
    for i in range(10000000):
        i * 5


check_duration()
