# -*- coding:utf-8 -*-

class Cercle:
    
    #constructeur
    def __init__(self):    
        self.rayon=0
    #fin constructeur
    
    #Saisie info
    def saisie(self):
        self.rayon=float(input("Rayon:"))
        
    # Calcul de l'aire et périmètre
    def calcul(self):
        print ("Le rayon est de :", (self.rayon**2)*3.14)
        print ("Le périmètre est de :", self.rayon*2*3.14)

#fin définition
    