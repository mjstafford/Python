
import random
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 1.3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nAttack: {self.strength} \nHealth: {self.health}\n")

    def attack( self , ninja ):
        self.strength = random.randint(6, 14)
        attack = self.speed * self.strength
        if ninja.health >= attack:
            ninja.health -= attack
        else:
            ninja.health = 0
        return self

    def heal(self):
        heal = random.randint(6, 15)
        if self.health + heal > 100:
            self.health = 100
        else:
            self.health += heal


    def is_alive( self ):
        if self.health > 0:
            return True
        else:
            return False
            