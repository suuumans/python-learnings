
# Counting Positive Numbers

# Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# Initialize a variable to count positive numbers
positive_number_count = 0

# Iterate through the list and count positive numbers
for number in numbers:
    # Check if the number is positive
    if number > 0:
        # If it is, Increment the count
        positive_number_count += 1
print("Final count of positive numbers is: ", positive_number_count) 