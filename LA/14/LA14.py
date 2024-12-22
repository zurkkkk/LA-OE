class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describe_spiderman(self):
        print(f"Name: {self.name}  Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)  # Correctly call super() for parent class constructor
        self.movietitle = movietitle

class Andrew(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Tom(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

tobey = Tobey("Tobey Maguire", "49", "Spiderman 3")
andrew = Andrew("Andrew Garfield", "41", "The Amazing Spiderman")
tom = Tom("Tom Holland", "28", "Spiderman: No Way Home")

print(f"{tobey.name.upper()} - {tobey.movietitle}")
print(f"{andrew.name.upper()} - {andrew.movietitle}")
print(f"{tom.name.upper()} - {tom.movietitle}")
