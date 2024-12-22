class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

car1 = Car("Mazda","Rx7","Black")
print(car1.brand, car1.model, car1.color)

car2 = Car("Honda","Civic FD" ,"White")
print(car2.brand, car2.model, car2.color)

car1.color = "Green"
print(car1.brand, car1.model, car1.color)

car2.color = "Blue"
print(car2.brand, car2.model, car2.color)
