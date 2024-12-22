class Dinakdakan:
    def __init__(self, meat, dry_seasoning, wet_seasoning):
        self.meat = meat
        self._dryseason = dry_seasoning
        self.__wetseason = wet_seasoning
        
    def __str__(self):
        return f"Ang dinakdakan ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
    
    def may_onion_ba(self):
        return "onion" in self.__wetseason.lower()
        
dinakdakan1 = Dinakdakan("Baboy (pork)", "asin, paminta, bawang", "suka, kalamansi, toyo")
dinakdakan2 = Dinakdakan("Manok (chicken)", "asin, paminta, bawang", "suka, kalamansi, toyo")
dinakdakan3 = Dinakdakan("Baka (beef)", "asin, paminta, bawang", "suka, kalamansi, toyo, onion")

print(dinakdakan1)
print(dinakdakan2)
print(dinakdakan3)

print(f"May onion ba sa Dinakdakan 1? {'Yes' if dinakdakan1.may_onion_ba() else 'No'}")
print(f"May onion ba sa Dinakdakan 2? {'Yes' if dinakdakan2.may_onion_ba() else 'No'}")
print(f"May onion ba sa Dinakdakan 3? {'Yes' if dinakdakan3.may_onion_ba() else 'No'}")
