
# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter the species (dog, cat): ").lower()
age = int(input("Enter the age: "))

if species == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")

elif species == "cat":
    if age > 5:
        print("Senior cat food")
    else:
        print("Adult cat food")
else:
    print("Invalid species")