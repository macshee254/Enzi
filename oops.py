# object oriented programming
class Car:
    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # a method function
    def describe_car(self):
        print(f"My dream car make: {self.make},"
              f"My dream car model: {self.model},"
              f"manufacturer: {self.year}")
# create object or instances of a class
myobj: Car = Car("toyota", "lexus", 2024)
myobj.describe_car()