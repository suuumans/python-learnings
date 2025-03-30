
# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments
# every time the function is called.


def debug(func):
    """
    This is a decorator that prints the function name and its arguments before execution.
    """
    def wrapper(*args, **kwargs):
        """
        This is the inner wrapper function that does the actual debugging.
        """
        # Convert positional arguments to a comma-separated string.
        args_value = ', '.join(str(args) for args in args)
        # Convert keyword arguments to a string like "key=value, key=value".
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        # Print the function name and its arguments.
        print(f"Function {func.__name__} called with arguments: {args_value}, {kwargs_value}")
        # Execute the original function and return its result.
        # Note: There was a typo "retrun" which has been corrected to "return"
        return func(*args, **kwargs)
    return wrapper


@debug
def add(a, b):
    return a + b

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print(f'sum of 3 and 4 is: {add(3, 4)}')
greet("Suman", greeting="Hey")