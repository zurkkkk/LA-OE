class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")
class Car(Vehicle):
    pass
class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass
my_car = Car("Toyota", "Corolla Big Body", "Gasoline")
my_carrr = Car("Honda", "2007 FD", "Gasoline")
my_motor = Motorcycle("Suzuki","Raider FI","Gasoline")
print() 
my_motor.describeVehicle()
print()
my_car.describeVehicle()
print()
my_carrr.describeVehicle()
