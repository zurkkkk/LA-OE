class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} with {self.attack_power} damage")
        print(f"{target.name} has now {target.health} health")
        if target.health <= 0:
            print(f"{target.name} is defeated")
            
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount}. Current health: {self.health}")
        

dragon_knight = Player("Draganor the Dragon Knight", 500, 80)
elven_archer = Player("Lirael the Elven Archer", 350, 50)

dragon_knight.attack(elven_archer)
elven_archer.attack(dragon_knight)

while dragon_knight.health > 0 and elven_archer.health > 0:
    dragon_knight.attack(elven_archer)
    if elven_archer.health <= 0:
        print(f"{dragon_knight.name} wins!")
        break
    
    elven_archer.attack(dragon_knight)
    if dragon_knight.health <= 0:
        print(f"{elven_archer.name} wins!")
        break

dragon_knight.heal(150)
