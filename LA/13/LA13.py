class isda():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describefish(self):
        print(f" fish name: {self.name} type: {self.type}")

class animal(isda):
    def __init__(self, name, type, can_swim):
        super().__init__(name,type)
        self.can_swim = True
    
tilapia = animal("tilapia", "fish", True)
tilapia.describefish()
print (tilapia.can_swim)
