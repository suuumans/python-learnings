
# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function,
# so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time


def Cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result =func(*args)
        cache_value[args] = result
        return result
    return wrapper

@Cache
def long_running_function(a, b):
    time.sleep(5)
    return a + b

print(long_running_function(3, 2))
print(long_running_function(3, 4))
print(long_running_function(5, 4))