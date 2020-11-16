###########################################
#           ~  PLAINS OF WYN  ~           #
###########################################
# A game by Antoine.c | Project started November 1st of 2020 | Genre: Text-based RPG (with interestings mechanics) #
# Made as my first python beginner project | Coded with <3 with Atom IDE | AMA: Eosis#6008 on discord #


#VARIABLES ET IMPORTS
import random # Used for the RNG and randint func
import sys # To exit the game automatically
import time # Used to make pauses in the game and check current real time
import pickle # Used to make saving and loading system
import pyfiglet # For the ASCII titles

class player:
    def __init__(self,name):
        self.hp = 20
        self.mp = 8
        self.gold = 100
        self.name = name
        self.inv = {}
        self.maxInvSize = 50
        self.faction = None
        self.race = None

P = player("Eosis")
print(P.faction)

class dice:
    def __init__(self,sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

print(dice(20).roll())
