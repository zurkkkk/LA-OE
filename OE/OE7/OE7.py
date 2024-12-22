Create a Class TekkenCharacter
class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper

character = TekkenCharacter("Jin", "Electric Wind Hook Fist")

@character.introduce  # Step 5: Decorate the function with @introduce
def character_intro():
    # Prints the character's name and ability
    print(f"I am {character.name} and I can use {character.ability}.")

character_intro()
