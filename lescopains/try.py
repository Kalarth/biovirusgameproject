#!/usr/bin/python
'''
Created on 11 nov. 2017
Release of 16 nov. 2017

@author: Denou Julien
@author: Bock Pauline
python version 2.7.13
'''
# -*- coding: uft-8 -*-
import os, sys
import random
from random import *
import time
#Fonction de difficulte
def difficult(selection):
    if  selection == 1:
        nbParoi = randint(7,12) #medium
        return nbParoi
    elif selection == 2:
        nbParoi = randint(12,19) #hard
        return nbParoi
    else :
        nbParoi = randint(3,7) #facile : peu de paroi cellulaire par defaut
        return nbParoi
#Fonction initialisation du plateau de jeu a vide
def init_plateau(Plateau): # rappeler init plateau et remplir si J et V bloques par les parois
    i=0
    while i<145:
        Plateau.append(' . ')
        i=i+1
#Fonction d'appel aleatoire
def alearemp():
    alea = randint(0,144)
    while Plateau[alea] != ' . ':
        alea = randint(0,144)
    return alea
#Fonction remplissage du plateau avec les differents elements
def remplir(Tableau, Plateau,nbjoueurs,position,nbvirus, nbParoi, nbenergie):
    for k in range(len(Tableau)):
        Plateau[Tableau[k]]=' # '#dessin des bords du plateau dont les indice sont dans Tableau
    for i in range(nbjoueurs):
        alea=alearemp()
        Plateau[alea]=' J '
        position.append(alea) #sauvegarde de la position du joueur
    for i in range(nbvirus):
        alea =alearemp()
        Plateau[alea]=' V '
        position.append(alea)#sauvegarde de la position des virus
    for i in range(nbParoi):
        alea =alearemp()
        Plateau[alea]='[#]'
    for i in range(nbenergie):
        alea =alearemp()
        Plateau[alea]='{~}'
#Fonction de possibilite d'un deplacement
def depIsPossible(Plateau, position, direction, nbcase):
    temp=position+direction*nbcase
    if temp>0 and temp<144:
        if Plateau[temp]==' . ':
            return True
        if Plateau[temp]=='{~}':
            return True
    else :
        return False
#Fonction de comptage de cases
def compteurCase(nbcase):
    nbcase=nbcase+1
    return nbcase
#Fonction d'affichage
def afficherPlateau(Plateau):
    print "\n"
    for i in range(0,144,12):
        print Plateau[i],'+',Plateau[i+1],'+',Plateau[i+2],'+',Plateau[i+3],'+',Plateau[i+4],'+',Plateau[i+5],'+',Plateau[i+6],'+',Plateau[i+7],'+',Plateau[i+8],'+',Plateau[i+9],'+',Plateau[i+10],'+',Plateau[i+11]
#Verification deplacement
def verifDep(nbcase, pos, direct):
    nbcase=1
    booleen =depIsPossible(Plateau, position[pos], direction[direct], nbcase)
    while booleen == True :
        nbcase=compteurCase(nbcase)
        booleen=depIsPossible(Plateau, position[pos], direction[direct], nbcase)
    return nbcase
#Choix des cases pour le Joueur
def choixCases(nbcase):
    if nbcase-1 == 0:
        nbcase=nbcase+1
    print "Entrez un nombre de cases compris entre 1 et",nbcase-1,":"
    nbcase=input()
    return nbcase
#Fonction de deplacement d'une seule case
def dep(Plateau, pos, direct, symbole,i):
    if Plateau[pos+direct]==' . ':
        Plateau[pos]=' . '
        position[i]=pos+direct
        Plateau[pos+direct]=symbole
    elif Plateau[pos+direct]=='{~}':
        Plateau[pos]=' . '
        position[i]=pos+direct
        Plateau[pos+direct]=symbole
        alea=alearemp()
        Plateau[alea]='{~}'
        if symbole == ' J ':
            boosterBombes(inventaire)
#Fonction de deplacement pour plusieurs cases
def deplacement(symbole, nbcase):
    i=0
    k=0
    if symbole == ' J ':
        menuaction(inventaire)
        choix=raw_input()
        if choix=="z":
            nbcase=verifDep(nbcase, 0, 0)
            nbcase=choixCases(nbcase)
            for k in range(nbcase) :
                dep(Plateau,position[0],direction[0], symbole,i)
                afficherPlateau(Plateau)
                time.sleep(0.8)
                os.system('clear')
        elif choix=="q":
            nbcase=verifDep(nbcase, 0, 1)
            nbcase=choixCases(nbcase)
            for k in range(nbcase) :
                dep(Plateau,position[0],direction[1], symbole,i)
                afficherPlateau(Plateau)
                time.sleep(0.8)
                os.system('clear')
        elif choix=="s":
            nbcase=verifDep(nbcase, 0, 2)
            nbcase=choixCases(nbcase)
            for k in range(nbcase) :
                dep(Plateau,position[0],direction[2], symbole,i)
                afficherPlateau(Plateau)
                time.sleep(0.8)
                os.system('clear')
        elif choix== "d":
            nbcase=verifDep(nbcase, 0, 3)
            nbcase=choixCases(nbcase)
            for k in range(nbcase) :
                dep(Plateau,position[0],direction[3], symbole,i)
                afficherPlateau(Plateau)
                time.sleep(0.8)
                os.system('clear')
        elif choix=="e":
            sys.exit()
    if symbole == ' V ':
        b = randint(0,3)
        for i in range(1,5):
            b = randint(0,3)
            nbcase=verifDep(nbcase, i, b)
            while nbcase-1<1:
                nbcase=verifDep(nbcase, i, b)
                b = randint(0,3)
            aleatoire = randint(1,nbcase)
            for k in range(aleatoire) :
                dep(Plateau,position[i],direction[b], symbole,i)
                k = k+1
                afficherPlateau(Plateau)
                time.sleep(0.8)
                os.system('clear')
    #if symbole == '~`O' :

#menu des actions du joueur
def menuaction(inventaire):
    print "Etat de l'inventaire : ", inventaire
    print "\n"
    print "*****Phase de mouvement****** \n z-Se deplacer en haut \n q-Se deplacer a gauche \n s-Se deplacer en bas \n d-Se deplacer a droite \n Saisir choix:"

#Choix de depot d'une bombe pour le joueur
def askbombe(inventaire):
    print "Voulez-vous posez une bombe ? [Y/N]"
    print "Bombe 1 :",inventaire[0]," Bombe 2 :",inventaire[1]," Bombe 3 :",inventaire[2]," Bombe 4 :",inventaire[3]
    choix=raw_input()
    if choix == "N" or choix =="n":
        return
    #elif choix == "Y" or choix == "y":
       # bombe(inventaire,Plateau,position,direction,nbcase)
    else:
        print "Le choix est incorrect"
        askbombe(inventaire)
#Fonction pour gerer l'explosion A TERMINER
def bombe(inventaire,Plateau,position,direction,nbcase):
    print "Voici la puissance de vos bombes"
    print "Bombe 1 :",inventaire[0]," Bombe 2 :",inventaire[1]," Bombe 3 :",inventaire[2]," Bombe 4 :",inventaire[3]
    print "Entrez emplacement bombe entre 1 et ",len(inventaire),":"
    choixb=input()
    print "Sur quelle case voulez-vous deposer la bombe ?"
    print"z-Deposer en haut \n q-Deposer a gauche \n s-Deposer en bas \n d-Deposer a droite"
    choixd=raw_input()
    i=0
    b=0
    if choixd== "d":
        b=3
    if choixd=="q":
        b=1
    if choixd=="z":
        b=0
    if choixd=="s":
        b=2
    aleat=randrange(2,8,2)
    inventaire[choixb-1]=aleat
    TNT=b
    return TNT
    #print "Voulez-vous rejouez ? [Y/N]"
    #choixk = raw_input()
    #if choixk == "Y"

#Fonction d'amelioration des bombes
def boosterBombes(inventaire):
    a = randint(0,3)
    temp = inventaire[a]
    inventaire[a]=temp+1
    b = randint(0,3)
    while b == a :
        b = randint(0,3)
    temp = inventaire[b]
    inventaire[b]=temp+1
#deroulement d'un tour
def tour():
    endgame=False
    tour=1
    while endgame==False:
        afficherPlateau(Plateau)
        if tour > 1 :
            deplacement('~`O', TNT)
        #explosion(position)
        deplacement(' V ', nbcase)
        afficherPlateau(Plateau)
        askbombe(inventaire)
        os.system('clear')
        deplacement(' J ', nbcase)
        afficherPlateau(Plateau)
        for i in range(len(inventaire)):
            inventaire[i]=inventaire[i]-1
            if inventaire[i]<0:
                inventaire[i]=0
        tour=tour+1

#Main
print("""Veuillez choisir la difficulte : \n 0: easy \n 1: medium \n 2: hard""")
selection = input()
nbParoi = difficult(selection)
#constantes
Tableau=[0,1,2,3,4,5,6,7,8,9,10,11,12,23,24,35,36,47,48,59,60,71,72,83,84,95,96,107,108,119,120,131,132,133,134,135,136,137,138,139,140,141,142,143,144]
Plateau = [];position = [];direction = [-12,-1,12,1];symbole = ''
nbcase=1;inventaire=[4,8,6,2];nbjoueurs=1;nbvirus = 4;nbenergie = 8; TNT=0

init_plateau(Plateau)
remplir(Tableau, Plateau,nbjoueurs,position,nbvirus, nbParoi, nbenergie)

while len(position)>0:
        if len(position)==1:
            print "BRAVO, vous avez tue tous les virus !"
            print "***********JEU TERMINE**************"
        elif inventaire == [0,0,0,0] :
            print "Game Over !"
        else:
            tour()
