class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character is truly iconic!")
        return wrapper

naruto = AnimeCharacter("Naruto Uzumaki", "Shadow Clone Jutsu")

@naruto.introduce
def character_intro():
    print(f"I am {naruto.name}, and I can use {naruto.ability}.")

character_intro()
