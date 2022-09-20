# -*- coding: UTF-8 -*-
# Programme qui simule un jeu de roulette simplifié

# Importation des modules
import math
import random
from random import randrange
from math import ceil

# Argent à dépenser
argent=float(input("argent à dépenser: "))

while argent > 0:              # Vérifie qu'il reste de l'argent
    
    mise=float(input("mise de départ: "))      # Choix de la mise
    while mise > argent :      # Vérifie que la mise n'est pas supérieur à l'argent restant     
        print ("Vous n'avez pas assez d'argent pour miser cette somme")
        mise = input("mise de départ: ")
    
    argent = argent - mise    # Mise à jour de l'argent restant
    
    numero=int(input("Misez sur un numéro entre 0 et 49: "))   # Choix du numéro
    if numero<0 or numero>49:        # Vérifie que le numéro choisi est bien entre 0 et 50
        print ("Entre 0 et 49 svp")
        numero=int(input("Misez sur un numéro entre 0 et 49: "))
    
    numero_roulette=randrange(0,50)                       # Lancement de la roulette
    print ("Le numéro roulette est : ", numero_roulette)
    
    if numero_roulette==numero:     # Résolution des gains/pertes
        print ("Bien joué !! Vous avez gagné 3 fois votre mise ! ") # Numéro = numéro roulette: gagné !
        argent = argent + 3*mise
        print ("Argent restant: ", argent)
    elif numero_roulette%2 == 0 and numero%2==0 :
        print ("Le numéro misé et le numéro de la roulette sont tous les deux pairs, bravo !") # 2 numéros pairs
        argent = ceil (argent + mise + 0.5*mise)
        print ("Argent restant: ", argent)
    elif numero_roulette%2 != 0 and numero%2!=0 :
        print ("Le numéro misé et le numéro de la roulette sont tous les deux impairs, bravo !") # 2 numéros impairs
        argent = ceil (argent + mise + 0.5*mise)
        print ("Argent restant: ", argent)
    else :                          # perdu
        print ("Vous avez perdu !")
        print ("Argent restant: ", argent)
    
    question=input("Voulez-vous rejouer ? [oui/non] ")  # Questionne le joueur pour une nouvelle partie
    if question=="non":
        break
        
print ("Veuillez quitter le casino")

