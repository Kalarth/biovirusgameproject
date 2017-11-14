#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import random
#from tkinter import *



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

#type de case
casevirus=BLEU+"\t (◣_◢) \t"+BLANC
casevide=ROUGE+"\t   .   \t"+BLANC
casejoueur=VERT+"\t (•ิ_•ิ)\t"+BLANC
casejoueurbomb=ORANGE+"\t(■_■)☢\t"+BLANC
casebomb=""+JAUNE+"\t(ϟ)\t"+BLANC
caseenergie=JAUNE+"\t(ϟ)\t"+BLANC
casemurver="\t  "+"\033[0;33;43m"+" ⬛"+BLANC+"\t"
casemurhor="\t  "+"\033[0;33;43m"+" ⬛"+BLANC+"\t"

#grille
grille=[ROUGE+"\t   .   \t"+BLANC]*100



def showGameBoard(grille,message):
    os.system('clear')
    barrehaute=(JAUNE+"▄"+BLANC)*161
    barrebasse=(JAUNE+"▀"+BLANC)*161
    print (barrehaute)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC+"  "+message)
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
    print ("mouvement des virus: ",ROUGE,vir1,vir2,vir3,vir4,BLANC+"\n")
    grille[vir1]=casevirus
    grille[vir2]=casevirus
    grille[vir4]=casevirus
    grille[vir3]=casevirus
    return virus



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
    joueur=mouvement["newpos"]
    grille[joueur]=casejoueur
    print(mouvement)

def keyinput(mouvement):
    oldpos=mouvement['oldpos']
    newpos=mouvement['newpos']
    voh=mouvement["typedeplacement"] #vertical ou horizontal ou none
    #print ("----POSTEST: ",mouvement)

    inputkey=input("Saisissez votre direction:  ")
    if inputkey=="z" and (voh=="v" or voh=="n"):  #aller vers le haut si on s'est déplacé verticalement ou pas déplacé
        oldpos=newpos
        newpos=oldpos-10
        voh="v" #vertical ou horizontal
        mouvement["newpos"]=newpos
        mouvement["oldpos"]=oldpos
        mouvement["typedeplacement"]=voh

        return mouvement

    if inputkey=="q" and (voh=="h" or voh=="n"):    #aller vers la gauche si on s'est déplacé horizontalement ou pas déplacé
        oldpos=newpos
        newpos=oldpos-1
        voh="h" #vertical ou horizontal
        mouvement["newpos"]=newpos
        mouvement["oldpos"]=oldpos
        mouvement["typedeplacement"]=voh
        return mouvement


    if inputkey=="s" and (voh=="v" or voh=="n"):    #aller vers le bas si on s'est déplacé verticalement ou pas déplacé
        oldpos=newpos
        newpos=oldpos+10
        voh="v" #vertical ou horizontal
        mouvement["newpos"]=newpos
        mouvement["oldpos"]=oldpos
        mouvement["typedeplacement"]=voh
        return mouvement


    if inputkey=="d" and (voh=="h" or voh=="n"):    #aller vers la droite si on s'est déplacé horizontalement ou pas déplacé
        oldpos=newpos
        newpos=oldpos+1
        voh="h" #vertical ou horizontal
        mouvement["newpos"]=newpos
        mouvement["oldpos"]=oldpos
        mouvement["typedeplacement"]=voh
        return mouvement

    if (inputkey=="1" and voh=="n"):                #poser une bombe si on ne s'est pas déplace
        newpos=oldpos
        voh="n" #vertical ou horizontal
        mouvement["newpos"]=newpos
        mouvement["typedeplacement"]=voh
        return mouvement

    if (inputkey=="1" and voh!="n"):                #ne pas poser une bombe si on s'est déplacé
        newpos=oldpos
        mouvement["newpos"]=newpos
        return mouvement

    if (inputkey==" " and voh!="n"):                #ne pas poser une bombe si on s'est déplacé
        mouvement["continuer"]=0
        print(mouvement)
        return mouvement


    else:
        return mouvement



def movejoueur():
        testmouvement=keyinput(mouvement)
        oldpos=testmouvement['oldpos']
        newpos=testmouvement['newpos']
        voh=testmouvement["typedeplacement"]

        if newpos != oldpos:
            if  newpos<0 or newpos>=100 or grille[newpos] != casevide or (oldpos%10==9 and newpos%10==0) or (oldpos%10==0 and newpos%10==9):
                #Test si on va sur une valeur hors liste, si on va sur une case non vide ou si on cherche a "se teleporter d'un bords a l'autre"
                message="Vous ne pouvez pas avancer dans cette direction"
                showGameBoard(grille,message)
                return mouvement

            if grille[newpos] == casevide: #test si on va sur une case vide
                if (grille[oldpos]==casejoueurbomb): #TEST DE CASE BOMBE
                    grille[oldpos]=casebomb
                else:
                    grille[oldpos]=casevide
                grille[newpos]=casejoueur
                mouvement["oldpos"]=oldpos
                mouvement["newpos"]=newpos
                mouvement["testmouvement"]=voh
                message="Vous avancez"
                showGameBoard(grille,message)

                #print ("MOUVEMENT DANS MOVEJOUEUR: ",mouvement)
                return mouvement

        if (newpos == oldpos and voh!="n"):
            grille[newpos]=casejoueur
            message="Bombes inaccessible après déplacement"
            showGameBoard(grille,message)
            return mouvement


        if (newpos == oldpos and voh=="n"):
            grille[newpos]=casejoueurbomb
            message="Vous venez de déposer une bombe"
            showGameBoard(grille,message)
            return mouvement


#def movevirus():




#MAIN

print (ORANGE + "DEBUT DU PROGRAMME (en couleur)","\n"+ BLANC)

mouvement={}
mouvement["oldpos"]=0
mouvement["newpos"]=random.randint(0,99)
mouvement["typedeplacement"]="n"
mouvement["continuer"]=1
#mouvement={"oldpos":random.randint(0,99),"newpos":0,"typedeplacement":"n","continuer":1}


continuer=1
message="Début du jeu"

initvirus()
initmurs()
initjoueur()
showGameBoard(grille,message)

while continuer==1:
    mouvement=movejoueur()
    continuer=mouvement["continuer"]
