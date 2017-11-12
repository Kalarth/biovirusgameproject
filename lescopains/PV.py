import os
import sys
from random import *
grille=[]
joueur=0
virus1=1
virus2=2
virus3=3
virus4=4
nb_nrj=8
nb_bombe=4
bombe1=8
bombe2=6
bombe3=4
bombe4=2
puissance_bombe=[2,4,6,8]
pos_J=0
for i in range(1,101):
    grille.append("  ")
def afficher_grille(grille): #affiche la grille de jeu en un carré de 10 cases
    print("      0)      1)     2)      3)     4)    5)     6)      7)    8)    9)")
    print("   -----------------------------------------------------------------------")
    print("0)", end='')
    for i in range(10):
        print("  |  "+str(grille[i]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("1)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+10]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("2)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+20]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("3)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+30]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("4)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+40]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("5)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+50]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("6)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+60]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("7)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+70]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("8)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+80]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")
    print("9)", end='')
    for i in range(10):
        print("  |  "+str(grille[i+90]), end='')
    print(" |")
    print("   -----------------------------------------------------------------------")

def affiche_joueur_depart(grille,pos_J):
        colonneJ=0 #coordonnees de depart pour le joueur J, ici 0 et 0
        ligneJ=0
        while grille[int(colonneJ)+int(ligneJ)*10]!="  ":
            print("Cette case est deja jouée ! Choix d'une autre case en cours !")
            colonneJ=randrange(10)
            ligneJ=randrange(10)
        pos_J=int(colonneJ)+int(ligneJ)*10 #sauvegarde la pos du joueur dans la variable pos_J
        grille[int(pos_J)]="J " #affiche la pos du joueur sur la grille avec le symbole J

"""def deplacement_joueur(grille):
        
        colonneJ=x
        ligneJ=x
        while grille[int(colonneJ)+int(ligneJ)*10]!="  ":
            afficher_grille(grille)
            print("Cette case est deja jouée ! Choix d'une autre case en cours !")
            colonneJ=randrange(10)
            ligneJ=randrange(10)
        grille[int(colonneJ)+int(ligneJ)*10]="J "
        afficher_grille(grille)"""
        
def affiche_virus(grille):
    i=1
    while i<=4:
        colonnevir=randrange(10)
        lignevir=randrange(10)
        while grille[int(colonnevir)+int(lignevir)*10]!="  ":
            print("Cette case est deja jouée ! Choix d'une autre case en cours !")
            colonnevir=randrange(10)
            lignevir=randrange(10)
        grille[int(colonnevir)+int(lignevir)*10]="*"+str(i) #calcul pour afficher les virus avec le symbole * sur la grille (virus 1 a virus 4)
        i+=1

def affiche_paroi(grille):
    z=1
    while z<=20:
        pos_paroi=randrange(100)
        while grille[int(pos_paroi)]!="  ":
            print("Cette case est deja jouée ! Choix d'une autre case en cours !")
            pos_paroi=randrange(100)
        grille[int(pos_paroi)]="XX" #calcul pour afficher les parois avec le symbole XX sur la grille (20 parois)
        z+=1
    
def affiche_energie(grille):
    y=1
    while y<=8:
        colonnenrj=randrange(10)
        lignenrj=randrange(10)
        while grille[int(colonnenrj)+int(lignenrj)*10]!="  ":
            print("Cette case est deja jouée ! Choix d'une autre case en cours !")
            colonnenrj=randrange(10)
            lignenrj=randrange(10)
        grille[int(colonnenrj)+int(lignenrj)*10]="o " #affiche les boules d'energie avec le symbole o sur la grille
        y+=1

"""def poser_bombe(grille):
    bombe1=8
    bombe2=6
    bombe3=4
    bombe4=2
    if (bombe1 & bombe2 & bombe3 & bombe4)!=0:
    print("Choississez le numero de la bombe a poser (1,2,3 ou 4)")
    choix_bombe=int(input())
    if choix_bombe==1:
                grille[int(colonneJ)+int(ligneJ)*10]="J$"
                bombe1=random.choice(puissance_bombe)
    afficher_grille(grille)
    if choix_bombe==2:":
                grille[int(colonneJ)+int(ligneJ)*10]="J$"
                bombe2=random.choice(puissance_bombe)
    if choix_bombe==3:
                grille[int(colonneJ)+int(ligneJ)*10]="J$"
                bombe3=random.choice(puissance_bombe)
    if choix_bombe==4:
                grille[int(colonneJ)+int(ligneJ)*10]="J$"
                bombe4=random.choice(puissance_bombe)"""
       
"""def depl_J_Hori(grille,pos_J):
    x=0
    while x<=9: #augmentation de la pos de 9 cases maxi
        if grille[int(pos_J)+int(x)]=="XX": #jaugmente la pos du joueur tant qu'il n'y pas de paroi
            break
        x+=1
    grille[int(pos_J)]="  "
    grille[int(pos_J)+int(x-1)]="J " #calcul pour afficher la nouvelle pos dans la grille
    afficher_grille(grille)
    pos_J=int(pos_J)+int(x-1) #sauvegarde de la nouvelle position du joueur"""


def depl_J(grille,pos_J,nb_nrj):
    print("Tapez 1 pour vous deplacer a la verticale et 2 pour l'horizontale")
    depl=int(input()) #on choisit si on veut se deplacer a la verticale (1) ou a l'horizontale (2)
    print("z et s = Haut et Bas, q et d = Droite et Gauche, p = Arret du deplacement et fin du tour")
    while grille[int(pos_J)]!="XX": #tant que la pos du joueur ne rencontre pas de paroi, le joueur peut bouger d'une case
        if depl==1:
            reponse=input()
            if reponse=="z": #si on appuie sur z, J se deplace de une case vers le haut
                grille[int(pos_J)]="  "
                pos_J+=-10
                if grille[int(pos_J)]=="o ": #si on passe sur une case avec une boule d'energie, on en affiche une nouvelle ailleurs
                    print("Vous avez ramassé de l'ATP !")
                    nb_nrj-=1
                    ajout_nrj(grille,nb_nrj)
                if grille[int(pos_J)]=="XX": #si pos_J = une case de la paroi, cela arrete le deplacement
                    break
                grille[int(pos_J)]="J "
                afficher_grille(grille)
                """os.system("clear")"""
            if reponse=="s": #si on appuie sur s, J se deplace de une case vers le bas
                 grille[int(pos_J)]="  "
                 pos_J+=10
                 if grille[int(pos_J)]=="o ":
                     print("Vous avez ramassé de l'ATP !")
                     nb_nrj-=1
                     ajout_nrj(grille,nb_nrj)
                 if grille[int(pos_J)]=="XX":
                     break
                 grille[int(pos_J)]="J "
                 afficher_grille(grille)
            if reponse=="p": #si on appuie sur p, cela quitte la boucle, arret du deplacement
                break
        if depl==2:
            reponse=input()
            if reponse=="q": #si on appuie sur q, J se deplace de une case vers la gauche
                grille[int(pos_J)]="  "
                pos_J+=-1
                if grille[int(pos_J)]=="o ":
                    print("Vous avez ramassé de l'ATP !")
                    nb_nrj-=1
                    ajout_nrj(grille,nb_nrj)
                if grille[int(pos_J)]=="XX":
                    break
                grille[int(pos_J)]="J "
                afficher_grille(grille)
            if reponse=="d": #si on appuie sur d, J se deplace de une case vers la droite
                 grille[int(pos_J)]="  "
                 pos_J+=1
                 if grille[int(pos_J)]=="o ":
                     print("Vous avez ramassé de l'ATP !")
                     nb_nrj-=1
                     ajout_nrj(grille,nb_nrj)
                 if grille[int(pos_J)]=="XX":
                     break
                 grille[int(pos_J)]="J "
                 afficher_grille(grille)
            if reponse=="p":
                break
            
def ajout_nrj(grille,nb_nrj): 
    if nb_nrj<8: #on ajoute une boule d'energie si il y en a moins de 8 sur la grille
        colonnenrj=randrange(10)
        lignenrj=randrange(10)
        while grille[int(colonnenrj)+int(lignenrj)*10]!="  ":
            print("Cette case est deja jouée ! Choix d'une autre case en cours !")
            colonnenrj=randrange(10)
            lignenrj=randrange(10)
        grille[int(colonnenrj)+int(lignenrj)*10]="o "
    nb_nrj+=1
    afficher_grille(grille)
    
if nb_bombe<4:
    nb_bombe+=1
    
affiche_joueur_depart(grille,pos_J)
affiche_virus(grille)
affiche_paroi(grille)
affiche_energie(grille)
afficher_grille(grille)
depl_J(grille,pos_J,nb_nrj)
