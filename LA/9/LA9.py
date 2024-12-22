class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"
car1 = Car("Konigsegg")
print(car1)

del car1
