
# Generator Function with yield
# Problem: Create a generator function that generates even numbers up to a specified limit.

def even_generator(limit):
    range(2, limit + 1, 2)
    for num in range(2, limit + 1, 2):
        yield num


limit = int(input("Enter the limit: "))
even_numbers = even_generator(limit)
print("Even numbers up to", limit, ":")
for num in even_numbers:
    print(num)