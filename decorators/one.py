
# Problem 1: Timing Function Execution
# Problem: Create a decorator that times the execution time of a function.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        stsrtTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"Function {func.__name__} took {endTime - stsrtTime} seconds to execute")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(3)

"""
Decorators - What They Do

Imagine you have a gift box.

The gift inside the box is your function. It does something specific, 
like adding numbers or printing a message.
A decorator is like wrapping paper or a ribbon you put around the gift box.
It doesn't change the gift itself, but it adds something extra to it.

"""