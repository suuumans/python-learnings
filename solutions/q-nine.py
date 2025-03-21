
# Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter a year: "))

#  in python 'and' is a logical operator that returns True if both conditions are True
#  like other languages 'or' is a logical operator that returns True if at least one condition is True
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a Leap year 🌟")
else:
    print(year, "is Not a leap year 🚫")