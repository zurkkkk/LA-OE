class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def describe_toy(self):
        print(f"Toy's name: {self.name}, Price: {self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

toykingdom = Car("Hotwheels Dodge Challenger", 199)

toykingdom.describe_toy()
