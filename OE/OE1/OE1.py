class Hero:
    def __init__(self, name, role, dmg_type, health, auto_attck_dmg, mana):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.mana = mana
        self.auto_attck_dmg = auto_attck_dmg

    def __str__(self):
        return f"This hero is {self.dmg_type}."

    def describe(self):
        print(f"{self.name} is a {self.role} with a {self.dmg_type} power")

    def meta(self):
        return f"{self.name} is a meta in this season."


# Updated heroes
hero_mm1 = Hero("Layla", "Marksman", "physical damage", 2500, 120, 350)
hero_fighter1 = Hero("Aldous", "Fighter", "burst damage", 3000, 150, 0)
hero_support1 = Hero("Angela", "Support", "heal", 2400, 80, 500)
hero_tank1 = Hero("Aldous", "Tank", "sustain", 3500, 100, 0)

# Print details for each hero
for hero in [hero_mm1, hero_fighter1, hero_support1, hero_tank1]:
    print(f'''
{hero.name}
{hero.role}
{hero.health} hp
{hero.mana} mana
{hero.auto_attck_dmg} basic damage
{hero.dmg_type}''')
    hero.describe()
    print(hero)
    print(hero.meta())
