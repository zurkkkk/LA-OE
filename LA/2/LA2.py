class character:
    def __init__(hero,name,role):
        hero.name = name
        hero.role = role
        
champions = character("Harith", "Mage")
print(champions.name, champions.role)
