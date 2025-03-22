
# Function with *args
# Problem: Create a function that takes any number of arguments and returns their sum.

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 3)
    return sum(args)

result = sum_all(1, 3, 4, 5, 7, 9)
print("The sum of all numbers is:", result)