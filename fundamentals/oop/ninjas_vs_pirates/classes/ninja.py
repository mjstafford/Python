import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 1.6
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nAttack: {self.strength}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        self.strength = random.randint(4, 13)
        attack = self.speed * self.strength
        if pirate.health >= attack:
            pirate.health -= attack
        else:
            pirate.health = 0
        return self


    def heal(self):
        heal = random.randint(3, 18)
        if self.health + heal > 100:
            self.health = 100
        else:
            self.health += heal

    def is_alive( self ):
        if self.health > 0:
            return True
        else:
            return False
            