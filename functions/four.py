
# Function Returning Multiple Values
# Problem: Problem: Create a function that returns both the area and circumference
# of a circle given its radius.

import math

radius = float(input("Enter the radius of the circle: "))

def circle_info(radius):
    # what this round( _ , 2 ) does is to round the value to 2 decimal places
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference

area, circumference = circle_info(radius)
print("Area of the circle: ", area, "Circumference of the circle: ", circumference)