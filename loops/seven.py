
# Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    user_input = int(input("Enter a number between 1 and 10: "))
    if 1 <= user_input <=10:
        print("You entered: ", user_input)
        break
    else:
        print("Invalid input. Please enter a number between 1 and 10.")