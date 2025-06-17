import time

def timer(func):
    """
    Decorator that measures and prints the execution time of a function.

    :param func: The function whose execution time is to be measured.
    :return: The result of the function call.
    """
    def wrapper(*args, **kwargs):
        start: float = time.time()
        result = func(*args, **kwargs)
        end: float = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper