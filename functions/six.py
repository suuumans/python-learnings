
# Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

x = int(input("Enter a number: "))

# lamda function is basically a small anonymous function
cube = lambda x: x ** 3
print("The cube of", x, "is:", cube(x))


# --------- #### ***** In Short ***** #### ----------
# Lambda functions are valuable tools in Python for creating small, 
# anonymous functions, especially when working with higher-order functions or 
# when you need to pass a function as an argument to another function. They are 
# often used when you need a concise way to express a simple operation. However, 
# they are not a replacement for regular functions, and you should choose the 
# appropriate method based on the complexity and reusability of the function you're creating.