from abc import ABC, abstractmethod  
  
class GameCharacter(ABC):  
   @abstractmethod  
   def attack(self):  
      pass  
  
class Warrior(GameCharacter):  
   def attack(self):  
      print("swings sword!")  
  
class Mage(GameCharacter):  
   def attack(self):  
      print("casts a fireball!")  
  
class Archer(GameCharacter):  
   def attack(self):  
      print("shoots an arrow!")  

class Healer(GameCharacter):  
   def attack(self):  
      print("casts a healing spell on ally!")  
  
warrior = Warrior()  
mage = Mage()  
archer = Archer()  
  
warrior.attack()  
mage.attack()  
archer.attack()  
healer = Healer()  
healer.attack()
