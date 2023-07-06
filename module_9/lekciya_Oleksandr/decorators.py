from functools import wraps
from datetime import datetime


def simple_decorator(func):

    @wraps(func)
    def simple_wrapper(*args, **kwargs):
        date = datetime.now().date()

        with open(f"E:\{date}.txt", "w") as log:
            result = func(*args, **kwargs)
            log.write(f"{result}")

        return (result)
    return simple_wrapper


def simple_decorator_2(func):

    @wraps(func)
    def simple_wrapper(*args, **kwargs):
        date = datetime.now().date()

        with open(f"E:\{date}.txt", "a") as log:
            result = func(*args, **kwargs)
            log.write(f"kdlfjkdfjkdjf{result}jlkjlkjlkjlkj")

            return (result)

    return simple_wrapper


@simple_decorator
@simple_decorator_2
def mult(x, y):
    return x*y


mult(5, 7)
