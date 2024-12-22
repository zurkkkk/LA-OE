class HalloweenParty:
    def __init__(self, theme):
        self.theme = theme  # Party theme (e.g., Halloween)
        
    def __specialdish(self):
        print(f"secret dish: pumpkin soup {self.theme}")  
        
    def celebration(self):
        print(f"{self.theme} foods: pumpkin pie, eyeball cookies, witches' brew, caramel apples, candy corn")
        print("special dish: spooky spaghetti")
        self.__specialdish() 
        
halloween_party = HalloweenParty("Halloween")

halloween_party.celebration()
