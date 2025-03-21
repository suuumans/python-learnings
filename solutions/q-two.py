
# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
# $8 for children. Everyone gets a $2 discount on Wednesday.

# we are using int() to convert the input to an integer
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
    
print(f"The movie ticket price is ${price}")