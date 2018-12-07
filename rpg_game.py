# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random 
import pygame
pygame.mixer.init()
pygame.init()
sounda= pygame.mixer.Sound("ZeldaSong.wav")
sounda.play()

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Dempsey'

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        multiplier = 1
        enemy.health -= self.power

        if self.name == "Hero":
            randomizer = random.randint(1,10)
            if multiplier == 0:
                pass
            elif randomizer <= 2:
                enemy.health -= self.power
                print (f"{self.name} did double damage!")
                multiplier = 2

        if enemy.name == "Medic":
            randomizer = random.randint(1,10)
            if randomizer <= 2:
                enemy.health += 2
                print(f"{enemy.name} recovered 2 health points.")

        if enemy.name == "Shadow":
            randomizer = random.randint(1,10)
            if randomizer <=1:
                self.power -= enemy.health
            else:
                print(f"{self.name} missed his attack.")
                multiplier = 0
        if enemy.name == "Zombie" and enemy.health <= 0:
            self.power -= enemy.health
            print(f"{self.name} is immortal. ")
            
        print(f"{self.name} does {self.power * multiplier} damage to the {enemy.name}.")

        if enemy.health <= 0:
            print(f"{enemy.name} is dead.")
        if self.health <= 0:
            print(f"{self.name} is dead.")
    
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")


class Hero(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Hero"


class Medic(Character):
    def __init__(self,health,power):
        super().__init__(health, power)
        self.name = "Medic"

class Goblin(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"

class Zombie(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Zombie"

class Shadow(Character):
    def __init__(self,health,power):
        super().__init__(health, power)
        self.name="Shadow"

def main():
    hero = Hero(50,2)
    goblin = Goblin(10,2)
    zombie = Zombie(5,5)
    medic = Medic(10,1)
    shadow = Shadow(1,2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        if goblin.health > 0:
            goblin.attack(hero)

    while medic.alive() and hero.alive():
        hero.print_status()
        medic.print_status()
        print()
        print("What do you want to do?")
        print("1. fight medic")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(medic)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        if medic.health > 0:
            medic.attack(hero)

    while shadow.alive() and hero.alive():
        hero.print_status()
        shadow.print_status()
        print()
        print("What do you want to do?")
        print("1. fight Shadow")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(shadow)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        if shadow.health > 0:
            shadow.attack(hero)


    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        if zombie.health > 0:
            zombie.attack(hero)

main()


