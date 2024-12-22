class character:
    def __init__(self, hero, role):
        self.hero = hero
        self.role = role
       
    def __str__(self):
        return (f'{self.hero} is a {self.role} role.')
        
        
mage = character("Harith", "Mage")
print(mage)
