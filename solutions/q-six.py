
# Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# we are using float() to convert the input to a float (decimal number)
distance = float(input("Enter the distance in kilometers: "))

if distance < 3:
    print("You should walk 🚶🏻")
elif distance < 15:
    print("You can take your bike 🚴🏻")
else:
    print("You can take your car 🚗")