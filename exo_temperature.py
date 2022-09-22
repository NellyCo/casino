# !/usr/bin/python3
# -*- coding : UTF-8 -*-

""" Exercice conversion température"""

a=input("Entrez la température à convertir [C pour celsius, F pour Fahrenheit]: ")

temp=("")

if a[-1]=="F":
    temp=int(a[0:-1])
    conv=(temp-32)/9*5
    print (a, "correspond à ",conv,"Celsius")
elif a[-1]=="C":
    temp=int(a[0:-1])
    conv=temp*9/5 + 32
    print (a, "correspond à ",conv,"Fahrenheit")
else:
    print ("Vous n'avez pas renseigné une unité (C ou F)")
    
