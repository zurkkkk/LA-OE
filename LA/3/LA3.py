class character:
    def __init__(self, hero, role):
        self.hero = hero
        self.role = role
        
    def describe(self):
        print(f"{self.hero} is a {self.role} role.")
        
mage = character("Harith", "Mage")
mage.describe()
