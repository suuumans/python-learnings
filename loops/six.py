
# Factorial Calculator
# Problem: Calculate the factorial of a given number.

n = int(input("Enter a number: "))
original_number = n

factorial = 1

while n > 0:
    factorial = factorial * n
    n = n - 1

print("Factorial of", original_number, "is:", factorial)