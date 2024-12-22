class phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def describephone(self):
        print(f"{self.brand}, {self.model}")
        
class android(phone):
    def __init__(self, brand, model):
        phone.__init__(self, brand, model)

tilipon = android ("Iphone", "15")
tilipon.describephone()
