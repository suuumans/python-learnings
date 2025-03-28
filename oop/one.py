
# Basic Class and Object

# Problem: Create a Car class with attributes like brand and model.
# Then create an instance of this class.

class Car:
    # Problem 6: Add a class variable to Car that keeps track of the number of cars created.
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    # Problem 2: Create a Car class with attributes like brand and model. 
    # Then create an instance of this class.
    def full_name(self):
        return f"{self.__brand} {self.model}"

    # Problem 4: Modify the Car class to encapsulate the brand attribute, making it private,
    # and provide a getter method for it.
    def get_brand(self):
        return self.__brand + " is the brand"

    # for setter
    def set_brand(self, brand):
        self.__brand = brand
    # def set_brand(self, brand):: This defines the setter method.
    # set_brand is the name of the method. It's a common convention to name setters set_ followed by the attribute name.
    # self is a reference to the current instance of the Car class.
    # brand is the parameter that will hold the new value for the brand.
    # self.__brand = brand: This line does the actual assignment. It takes the brand 
    # value passed to the setter and assigns it to the private attribute __brand of the current Car object.

    #Problem 5: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, 
    # but with different behaviors.
    def fuel_type(self):
        return "Petrol or Diesel"

    # Problem 7: Add a static method to the Car class that returns a general description of a car.
    @staticmethod
    def general_description():
        retutn "Mostly cars are made of metal"
    
    # In Python, a static method is a method that belongs to the class itself, not to a specific
    # instance of the class. It's essentially a regular function that happens to be defined within a class.

    # Problem 8: Use a property decorator in the Car class to make the model attribute read-only.
    @property
    def model(self):
        return self.__model






# Problem 3: Create an ElectricCar class that inherits from the Car class and has an additional
# attribute battery_size.
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    # Problem 5
    def fuel_type(self):
        return "Electric"



# problem 1
my_car = Car('Audi', 'RS7')
print(my_car.brand, my_car.model)

my_new_car = Car('Porsche', '911 GT3 RS')
print(my_new_car.brand, my_new_car.model)

# problem 2
print(my_car.full_name())
print(my_new_car.full_name())

# problem 3
my_electric_car = ElectricCar('Porsche', 'Tycan', '75kWh')
print(my_electric_car.full_name())

# problem 4
# for getter
print(my_car.get_brand())

# for setter
my_car.set_brand('Skoda')
print(my_car.get_brand())

# problem 5
print(my_electric_car.fuel_type())
nexon = Car('Tata', 'Nexon')
print(nexon.fuel_type())

# problem 6
print(Car.total_car)
print(ElectricCar.total_car)

# problem 7
print(Car.general_description())

# problem 8
my_car.model = "City"
print(my_car.model)

# Problem 9: Demonstrate the use of isinstance() to check if my_tesla is an 
# instance of Car and ElectricCar.
print(isinstance(my_electric_car, ElectricCar))
print(isinstance(my_electric_car, Car))

# Problem 10: Create two classes Battery and Engine, and let the ElectricCar class
# inherit from both, demonstrating multiple inheritance.
class Battery:
    def battery_info(self):
        return "This is battey"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Car, Battery, Engine):
    pass


my_second_electric_car = ElectricCarTwo('Porsche', 'Tycan Turbo')
print(my_second_electric_car.battery_info())
print(my_second_electric_car.engine_info())