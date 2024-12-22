class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def laptop_info(self):
        return f"{self.brand} {self.model}"

laptop = Laptop("Acer", "NITRO 7")
print(laptop.laptop_info())
