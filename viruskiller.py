#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
from tkinter import *



os.system('clear')


#COLORS
VIOLET = '\033[95m'
BLEU = '\033[94m'
VERT = '\033[92m'
ORANGE = '\033[93m'
ROUGE = '\033[91m'
BLANC = '\033[0m'
GRAS = '\033[1m'
SOULIGNE = '\033[4m'

casevirus=BLEU+"\t(◣_◢)\t"+BLANC
casevide=ROUGE+"\t   .   \t"+BLANC
casejoueur=VERT+"\t(⌐■_■)\t"+BLANC

grille=[ROUGE+"\t   .   \t"+BLANC]*100



print (ORANGE + "DEBUT DU PROGRAMME (en couleur)","\n"
      + BLANC)


def showGameBoard(grille):
    os.system('clear')
    for i in range(0,100):
        print (grille[i],end='')
        if i!=0 and i%10==9:
            print ("\n\n\n")



def positionvirus():
    virus=random.sample(range(0,99),4) #list of 4 different number
    vir1=virus[0]
    vir2=virus[1]
    vir3=virus[2]
    vir4=virus[3]
    print ("Position des virus: ",ROUGE,vir1,vir2,vir3,vir4,BLANC+"\n")
    grille[vir1]=casevirus
    grille[vir2]=casevirus
    grille[vir4]=casevirus
    grille[vir3]=casevirus


def initjoueur():
    joueur=position[1]
    grille[joueur]=casejoueur


def keyinput(position):
    oldpos=position[1]
    inputkey=input("Saisissez votre direction:  ")
    if inputkey=="z":
        newpos=oldpos-10
        position=[oldpos,newpos]
        return position

    if inputkey=="q":
        newpos=oldpos-1
        position=[oldpos,newpos]
        return position


    if inputkey=="s":
        newpos=oldpos+10
        position=[oldpos,newpos]
        return position


    if inputkey=="d":
        newpos=oldpos+1
        position=[oldpos,newpos]
        return position


def movejoueur(position,continuer):
        testposition=keyinput(position)
        oldpos=testposition[0]
        newpos=testposition[1]

        if grille[newpos] != casevide:
            print ("Vous ne pouvez pas avancer plus loin")
            print (position)
            continuer=0
            return position

        if grille[newpos] == casevide:
            grille[oldpos]=casevide
            grille[newpos]=casejoueur
            position=[oldpos,newpos]
            showGameBoard(grille)
            print (position)
            return position


#MAIN

position=[0,random.randint(0,99)]
print (position)
continuer=1

positionvirus()
initjoueur()
showGameBoard(grille)

while continuer==1:
    position=movejoueur(position,continuer)
