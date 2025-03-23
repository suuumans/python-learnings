
# Python Learnings

Welcome to the Python Learnings repository! This guide provides an introduction to the basics of Python programming, including data types, variable declarations, and other essential concepts for beginners.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Types](#data-types)
3. [Variable Declarations](#variable-declarations)
4. [Basic Operations](#basic-operations)
5. [Control Structures](#control-structures)
6. [Functions](#functions)

## Introduction
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Data Types
Python has several built-in data types that are used to store different kinds of data. Here are some of the most common data types:

### Numeric Types
- **int**: Integer values (e.g., `1`, `42`, `-7`)
- **float**: Floating-point numbers (e.g., `3.14`, `2.0`, `-0.5`)

### Sequence Types
- **str**: String of characters (e.g., `"Hello, World!"`, `'Python'`)
- **list**: Ordered collection of items (e.g., `[1, 2, 3]`, `['apple', 'banana', 'cherry']`)
- **tuple**: Ordered, immutable collection of items (e.g., `(1, 2, 3)`, `('apple', 'banana', 'cherry')`)

### Mapping Type
- **dict**: Collection of key-value pairs (e.g., `{'name': 'Alice', 'age': 30}`)

### Set Types
- **set**: Unordered collection of unique items (e.g., `{1, 2, 3}`, `{'apple', 'banana', 'cherry'}`)
- **frozenset**: Immutable version of a set (e.g., `frozenset([1, 2, 3])`)

### Boolean Type
- **bool**: Boolean values (`True` or `False`)

### None Type
- **NoneType**: Represents the absence of a value (`None`)

## Variable Declarations
In Python, variables are used to store data values. Variables do not need to be declared with a specific type, and their type can change dynamically.

### Examples
```python
# Integer variable
age = 25

# Float variable
pi = 3.14

# String variable
name = "Alice"

# List variable
fruits = ["apple", "banana", "cherry"]

# Tuple variable
coordinates = (10, 20)

# Dictionary variable
person = {"name": "Alice", "age": 25}

# Set variable
unique_numbers = {1, 2, 3}

# Boolean variable
is_valid = True

# NoneType variable
result = None
```

## Basic Operations
Python supports various basic operations, including arithmetic, comparison, logical, and assignment operations.

## Arithmetic Operations
```Python
a = 10
b = 3

# Addition
sum = a + b  # 13

# Subtraction
difference = a - b  # 7

# Multiplication
product = a * b  # 30

# Division
quotient = a / b  # 3.3333...

# Floor Division
floor_quotient = a // b  # 3

# Modulus
remainder = a % b  # 1

# Exponentiation
power = a ** b  # 1000
```

## Comparison Operations
```Python
x = 5
y = 10

# Equal to
print(x == y)  # False

# Not equal to
print(x != y)  # True

# Greater than
print(x > y)  # False

# Less than
print(x < y)  # True

# Greater than or equal to
print(x >= y)  # False

# Less than or equal to
print(x <= y)  # True
```

## Logical Operations
```Python
a = True
b = False

# Logical AND
print(a and b)  # False

# Logical OR
print(a or b)  # True

# Logical NOT
print(not a)  # False
```

## Assignment Operations
```Python
x = 10

# Addition assignment
x += 5  # x = 15

# Subtraction assignment
x -= 3  # x = 12

# Multiplication assignment
x *= 2  # x = 24

# Division assignment
x /= 4  # x = 6.0

# Modulus assignment
x %= 5  # x = 1.0

# Exponentiation assignment
x **= 3  # x = 1.0

# Floor division assignment
x //= 2  # x = 0.0
```
# Control Structures
Python provides several control structures for managing the flow of a program, including conditional statements and loops.

## Conditional Statements
```Python
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

# Loops
## for Loop
```Python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
## Iterate over a range of numbers
```python
for i in range(5):
    # Print numbers from 0 to 4
    print(i)
```

# while Loop
```Python
# Print numbers from 0 to 4
i = 0
while i < 5:
    print(i)
    i += 1
```

# Functions
Functions are reusable blocks of code that perform a specific task. They can accept parameters and return values.

## Defining a Function
```Python
def greet(name):
    return f"Hello, {name}!"
```
## Calling a function
```python
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```
## Function with Multiple Parameters
```Python
def add(a, b):
    return a + b
```

## Calling the function
```python
result = add(3, 5)
print(result)  # Output: 8
```
## Function with Default Parameters
```Python
def greet(name, message="Hello"):
    return f"{message}, {name}!"
```

## Calling the function
```python
print(greet("Alice"))        # Output: Hello, Alice!
print(greet("Bob", "Hi"))    # Output: Hi, Bob!
```
# Lambda Functions
Lambda functions are small anonymous functions that can have any number of arguments but only one expression.

## Lambda function to add two numbers
```python
add = lambda a, b: a + b
```

## Calling the lambda function
```python
result = add(3, 5)
print(result)  # Output: 8
```

## Conclusion
This is just a brief introduction to the basics of Python programming. Feel free to explore the repository for more topics and examples. Happy coding!
