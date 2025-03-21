
# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: ")

# len() is a function that returns the length of a string
if len(password) < 6:
    print("Weak password 💀")
elif len(password) <= 10:
    print("Medium password 🌟")
else:
    print("Strong password 💪")