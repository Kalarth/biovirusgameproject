#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system('clear')
print("Debut du programme !",'\n')
x=[1,2,3,4,5,6,7,8,9,10]
y=[0,10,20,30,40,50,60,70,80,90]

grille=[]
grillex=[]
separator="---------------------------------------------------------------------------------------------------------------------------------------------------------------"

#Creation d'une liste sous la forme [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14...]]
for i in range(len(y)):
    grillex=[]
    for j in range(len(x)):
        value=x[j]+y[i]
        grillex.append(value)
    grille.append(grillex)

#Print de la liste avec un retour a la ligne entre chaque sous-liste et tabulation pour chaque elements
print ("\n",separator)
for i in range(len(grille)):                                    #on boucle à travers les listes "dizaine" 0. 1. 2. 3. [...]
    print("|\t\t"*(len(grille[j])+1))                           #print une ligne de "| |" vide avant et après les cases
    print ('|',end="\t")
    for j in range(len(grille[j])):                             #on boucle à travers les sous listes "unité" .0 .1 .2 .3 [...]
        print(grille[i][j],"\t|",end='\t')
    print("\n",end="")                                          #saute une ligne et laisse le texte du prochain print après
    print("|\t\t"*(len(grille[j])+1))                           #print une ligne de "| |" vide avant et après les cases
    print ("",separator)
