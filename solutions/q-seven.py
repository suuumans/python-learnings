
# Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

size = input("Enter your coffee size (small, medium, large): ").lower()
extraShot = input("Do you want an extra shot? (yes, no): ").lower()

if extraShot == "yes":
    print("You ordered an extra shot - ")
else:
    print("You did not order an extra shot.")

if size == "small":
    print("of a small coffee.")
elif size == "medium":
    print("of a medium coffee.")
elif size == "large":
    print("of a large coffee.")
