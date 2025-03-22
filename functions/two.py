
# Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Function with Multiple Parameters
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)