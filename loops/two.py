
# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a number: "))

# Initialize a variable to store the sum of even numbers
sum_of_even_numbers = 0

# Iterate through numbers from 1 to n and add even numbers to the sum
# range is a built-in function that returns a sequence of numbers
for number in range(1, n + 1):
    if number % 2 == 0:
        sum_of_even_numbers += number

print("Sum of even numbers up to", n, "is:", sum_of_even_numbers)