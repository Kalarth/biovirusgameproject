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
JAUNE="\033[33m"

casevirus=BLEU+"\t(◣_◢)\t"+BLANC
casevide=ROUGE+"\t   .   \t"+BLANC
casejoueur=VERT+"\t (•ิ_•ิ)\t"+BLANC
casejoueurbomb=ORANGE+"\t(■_■)☢\t"+BLANC
casebomb=""+JAUNE+"\t  (ϟ)\t"+BLANC
caseenergie=JAUNE+"\t (ϟ)\t"+BLANC
casemurver=JAUNE+"\t   █   \t"+BLANC
casemurhor=JAUNE+"\t   ⬜  \t"+BLANC


grille=[ROUGE+"\t   .   \t"+BLANC]*100



print (ORANGE + "DEBUT DU PROGRAMME (en couleur)","\n"
      + BLANC)


def showGameBoard(grille):
    os.system('clear')
    barrehaute=(JAUNE+"▄"+BLANC)*161
    barrebasse=(JAUNE+"▀"+BLANC)*161
    print (barrehaute)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC)
    for i in range(0,100):
        if i%10==0:
            print (JAUNE+"█"+BLANC,end="")
        print (grille[i],end='')
        if i%10==9:
            print (JAUNE+"█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC)
    print (barrebasse)


def initvirus():
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

def initmurs():
    debutmurs=random.sample(range(0,69),4)
    debutmurs1=[debutmurs[0],debutmurs[0]-10,debutmurs[0]-20,debutmurs[0]-30]
    debutmurs2=[debutmurs[1],debutmurs[1]+10,debutmurs[1]+20,debutmurs[1]+30]
    debutmurs3=[debutmurs[2],debutmurs[2]-1,debutmurs[2]-2,debutmurs[2]-3]
    debutmurs4=[debutmurs[3],debutmurs[3]+1,debutmurs[3]+2,debutmurs[3]+3]
    murshor=[debutmurs3,debutmurs4]
    mursver=[debutmurs1,debutmurs2]
    print (debutmurs[0])
    print (debutmurs[0]+1)

    for i in range(0,len(murshor)):
        for j in murshor[i]:
            if grille[j]==casevide:
                grille[j]=casemurhor
    for i in range(0,len(mursver)):
        for j in mursver[i]:
            if grille[j]==casevide:
                grille[j]=casemurver


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

    if inputkey==" ":
        newpos=oldpos
        position=[oldpos,newpos]
        return position

    else:
        return position



def movejoueur(position,continuer):
        testposition=keyinput(position)
        oldpos=testposition[0]
        newpos=testposition[1]

        if newpos != oldpos:
            if  newpos<0 or newpos>=100 or grille[newpos] != casevide or (oldpos%10==9 and newpos%10==0) or (oldpos%10==0 and newpos%10==9):
                #Test si on va sur une valeur hors liste, si on va sur une case non vide ou si on cherche a "se teleporter d'un bords a l'autre"
                print ("Vous ne pouvez pas avancer plus loin")
                print (position)
                continuer=0
                return position

            if grille[newpos] == casevide: #test si on va sur une case vide
                if (grille[oldpos]==casejoueurbomb): #TEST DE CASE BOMBE
                    grille[oldpos]=casebomb
                else:
                    grille[oldpos]=casevide
                grille[newpos]=casejoueur
                position=[oldpos,newpos]
                showGameBoard(grille)
                print (position)
                return position

        if newpos == oldpos:
            grille[newpos]=casejoueurbomb
            showGameBoard(grille)
            print (position)
            continuer=1
            return position



#MAIN

position=[0,random.randint(0,99)]
print (position)
continuer=1

initvirus()
initmurs()
initjoueur()
showGameBoard(grille)

while continuer==1:
    position=movejoueur(position,continuer)
