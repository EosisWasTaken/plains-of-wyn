###########################################
#           ~  PLAINS OF WYN  ~           #
###########################################
# A game by Antoine.c | Project started November 1st of 2020 | Genre: Text-based RPG (with interestings mechanics) #
# Made as my first python beginner project | Coded with <3 with Atom IDE | AMA: Eosis#6008 on discord #


#VARIABLES ET IMPORTS
import random #pour la RNG
import sys #pour quitter le jeu
import time #pour faire des pauses
import pickle #sauvegarde du dict joueur
import pyfiglet #pour le title en ASCII

map = ["Cuisine","Salon","Chambre","Garage","SDB"]
north = ""
south = ""
east = ""
west = ""
class player:
    def __init__(self,name):
        self.name = name
        self.hp = 8
        self.mp = 20
        self.gold = 100
        self.inv = {}
        self.maxInvSize = 50






#INVENTAIRE
class Inv:
    def addItem(item,count): #Ajouter un item a l'inventaire

        checkInv = P.inv.get(item,False)
        weight = 0
        if Inv.getWeight() <= P.maxInvSize:
            if checkInv == False:
                P.inv[item] = count
            else:
                P.inv[item] += count

    def checkItem(item): #Vérifier l'existence d'un item dans l'inventaire (son nombre?)

        if item in P.inv:
            return True
        else:
            return False

    def removeItem(item,count): #Retirer un item de l'inventaire

        checkInv = P.inv.get(item,False)
        if checkInv == False:
            return "error"
        else:
            if count > P.inv[item]:
                P.inv.pop(item)
            else:
                P.inv[item] -= count

    def getWeight(): #Obtenir le "poids" de l'inventaire (1 value = 1 unité de poids)

        weight = 0
        for v in P.inv.values():
            weight += v
        return weight

#DICE
class Dice:
    def __init__(self,sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)


#JEU
def start():
    global P
    title = pyfiglet.print_figlet('Plains of Wyn!\n')
    askname = str(input("Entrez votre nom\n->"))
    P = player(askname)
    P.gold = 694200000000000000000
    P.hp = 8
    P.mp = 20
    Inv.addItem("test",10)
    Inv.removeItem("test",10)
    title = pyfiglet.print_figlet("Welcome, " + P.name + "!")
    print(P.inv)
    c = input("Que veux tu faire?\n1)Charger\n2)Sauvegarder\n3)Quitter")
    if c in ['1','charger','Charger']:
        with open('player.wyn','rb') as f:
            P = pickle.load(f)
            print(f"sauvegarde chargée, tu est maintenant {P.name}, tu as {P.gold} gold, et ton inventaire contient {P.inv}")
    elif c in ['2','sauvegarder','Sauvegarder']:
            with open('player.wyn', 'wb') as f:
                pickle.dump(P,f)
                print("Partie sauvegardée! Ne touche surtout pas au fichier player.wyn!")

    elif c in ['3','quitter','Quitter']:
        sys.exit()
    else:
        print("erreur, normalement dans une class fonction on re call la fonction après avoir affiché un message d'erreur")





#FONCTIONS
start()
