class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}! {target.name}'s health is now {target.health}")

    def special_move(self):
        pass

    def defend(self, attacker):
        print(f"{self.name} defends against {attacker.name} and reduces damage.")
        self.health -= attacker.power // 2
        print(f"{self.name}'s health is now {self.health}")

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2

class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball!")
        self.power = 100 

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow!")

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50

warrior = Warrior("Warrior", 300, 50)
mage = Mage("Mage", 200, 30)
archer = Archer("Archer", 250, 40)
monster = Monster("Monster", 400, 60)

warrior.special_move()
mage.special_move()
archer.special_move()
monster.special_move()

warrior.attack(monster)
mage.attack(monster)
archer.attack(monster)

monster.attack(warrior)
warrior.defend(monster)

monster.attack(mage)
mage.defend(monster)

monster.attack(archer)
archer.defend(monster)
