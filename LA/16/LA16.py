class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
   
    def operate(self):
        print("Operating!")
    
    def info(self):
        print(f"BRAND: {self.brand} MODEL: {self.model}")
       
class WashingMachine(Appliance):
    def operate(self):
        print(f"{self.brand} washing machine is cleaning your clothes!")

class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def operate(self):
        print(f"{self.brand} refrigerator is keeping your food fresh!")

class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def operate(self):
        print(f"{self.brand} microwave is heating your meal!")

washing = WashingMachine("Bosch", "Serie 6 9kg Front Load Washing Machine")
ref = Refrigerator("Whirlpool", "WRS321SDHZ Side-by-Side Refrigerator")
microwave = Microwave("Sharp", "R-21A0 Commercial Microwave Oven")

appliances = [washing, ref, microwave]

for appliance in appliances:
    appliance.operate()

for appliance in appliances:
    appliance.info()
