class Fruit:
    # constructor function
    def __init__(self, name, colour, price):
        self.name = name
        self.colour = colour
        self.price = price
     # method function
    def describe_fruit(self):
            print(f"I love eating  the fruit: {self.name},"
                  f"The colour of the fruit is: {self.colour},"
                  f"It's price is: {self.price}")
myfruit = Fruit("watermelon", "red", 200)
myfruit.describe_fruit()
