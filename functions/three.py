
# Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.


def multiply(a, b):
    return a * b

multiply('s', 5)
multiply(5, 7)
print("The result of multiplication is:", multiply(5, 7))
print("The result of multiplication is:", multiply('s', 5))