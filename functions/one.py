
# Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

number = int(input("Enter a number: "))
# in python functions are defined using def keyword
def suqare(number):
    return number ** 2

result = suqare(number)
print("The square of", number, "is:", result)