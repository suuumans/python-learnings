
# Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided,
# it should greet with a default name.

def greet_user(name = "Suman"):
    return "Hello," + name + "!"

print(greet_user())
print(greet_user("John"))