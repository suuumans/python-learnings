
# Reverse a String
# Problem: Reverse a given string using a loop.

input_string = input("Enter a string: ")

# Initialize an empty string to store the reversed string
reversed_string = ""

# Iterate through the input string in reverse order
for char in input_string:
    # Append each character to the reversed string
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)