class Dinakdakan:
    def __init__(self, meat, dry_seasoning, wet_seasoning):
        self.meat = meat                # Public attribute 
        self._dryseasoning = dry_seasoning    # Protected attribute
        self.__wetseasoning = wet_seasoning   # Private attribute 
        
    def __str__(self):
        return f"Ang dinakdakan ko ay {self.meat}, {self._dryseasoning}, {self.__wetseasoning}"
    
    def may_onion_ba(self):
        return "onion" in self.__wetseasoning.lower()
        
    def set_onion(self, bagong_value):
        self.__wetseasoning = bagong_value
    
dinakdakan1 = Dinakdakan("Baboy (pork)", "asin, paminta, bawang", "suka, kalamansi, toyo")
dinakdakan2 = Dinakdakan("Manok (chicken)", "asin, paminta, bawang", "suka, kalamansi, toyo")
dinakdakan3 = Dinakdakan("Baka (beef)", "asin, paminta, bawang", "suka, kalamansi, toyo, onion")

print(dinakdakan1)
print(dinakdakan2)
print(dinakdakan3)

print(f"May onion ba sa Dinakdakan 1? {'Yes' if dinakdakan1.may_onion_ba() else 'No'}")
print(f"May onion ba sa Dinakdakan 2? {'Yes' if dinakdakan2.may_onion_ba() else 'No'}")
print(f"May onion ba sa Dinakdakan 3? {'Yes' if dinakdakan3.may_onion_ba() else 'No'}")

dinakdakan1.set_onion("suka, kalamansi, toyo, onion")
dinakdakan2.set_onion("suka, kalamansi, toyo, onion")
dinakdakan3.set_onion("suka, kalamansi, toyo, onion, garlic")

print("\nAfter updating wet seasonings:")
print(dinakdakan1)
print(dinakdakan2)
print(dinakdakan3)


print(f"May onion ba sa Dinakdakan 1? {'Yes' if dinakdakan1.may_onion_ba() else 'No'}")
print(f"May onion ba sa Dinakdakan 2? {'Yes' if dinakdakan2.may_onion_ba() else 'No'}")
print(f"May onion ba sa Dinakdakan 3? {'Yes' if dinakdakan3.may_onion_ba() else 'No'}")
