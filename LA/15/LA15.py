class Dog:
    def __init__(self, name):
        self.name = name 
  
    def speak(self):  
        print(f"{self.name} Bark!")  
  
class Cat:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        print(f"{self.name} Meow!")

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Chrip!")
  
dog = Dog("dog")  
cat = Cat("cat")  
bird = Bird("bird")  
  
animals = [dog, cat, bird]  
  
for animal in animals:  
    animal.speak()
