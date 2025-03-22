
# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_string = input("Enter a string: ")

for char in input_string:
    print(char)
    # Check if the character is present only once
    if input_string.count(char) == 1:
        print("The first non-repeated character is: ", char)
        break