
# Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 5:
        # Skip the fifth iteration. Continue to the next iteration
        continue
    result = n * i
    print(f"{n} x {i} = {result}")