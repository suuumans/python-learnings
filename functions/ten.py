
# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

n = int(input("Enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(n)
print("Factorial of", n, "is:", result)




# in recursion we call the the function itself in the same function