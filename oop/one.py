
# Basic Class and Object

# Problem: Create a Car class with attributes like brand and model.
# Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car('Audi', 'RS7')
print(my_car.brand, my_car.model)

my_new_car = Car('Porsche', '911 GT3 RS')
print(my_new_car.brand, my_new_car.model)