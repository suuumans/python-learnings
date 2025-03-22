
# List Uniqueness Checker
# Problem: Check if all elements in a list are unique.
# If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

# set is a collection of unique elements. It is used to check for duplicates
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item found:", item)
        break
    unique_item.add(item)