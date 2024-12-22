class Dinakdakan:
    def __init__(self, meat, dry_seasoning, wet_seasoning):
        self.meat = meat
        self._dry_seasoning = dry_seasoning
        self.__wet_seasoning = wet_seasoning
        
    def __str__(self):
        return f"Ang dinakdakan ko ay {self.meat}, {self._dry_seasoning}, at may {self.__wet_seasoning}"

dinakdakan1 = Dinakdakan("Baboy (pork)", "asin, paminta, bawang", "suka, kalamansi, toyo")
dinakdakan2 = Dinakdakan("Manok (chicken)", "asin, paminta, bawang", "suka, kalamansi, toyo")
dinakdakan3 = Dinakdakan("Baka (beef)", "asin, paminta, bawang", "suka, kalamansi, toyo")

print(dinakdakan1)
print(dinakdakan2)
print(dinakdakan3)

print(dinakdakan1._dry_seasoning)
