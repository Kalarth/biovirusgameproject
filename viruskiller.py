#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import time
from viruskillerdrawing import *

os.system('clear')

# grille: index de 0 à 99, represente dans le terminal par des points rouge.
grille = [casevide] * 100
virus = []
ATP = []

# bombe: [position,puissance] ; "n" pour none cad n'apparaissant pas sur la grille
bombeloader = {
    "bombe1": ["n", 8],
    "bombe2": ["n", 6],
    "bombe3": ["n", 4],
    "bombe4": ["n", 2]
}

# mouvement du joueur [ancienne position, nouvelle position, type de déplacement, continuer le déplacement]
# "n": ne s'est pas encore déplacé pendant le tour | "v" déplacé verticalement | "h" déplacé horizontalement
mouvement = [0, 0, "n", 1]

# message: utilisé parfois à certains moment pendant le tour de jeu sur l'interface utilisateur
message = "Tour de jeu" + JAUNE + "\t\t\t\t\t█" + BLANC


# sautdeligne - fonction de "style" pour le print de la grille dans le terminal
def sautdeligne():
    print(JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" +
          "\t\t\t\t\t\t█" + BLANC)
    print(JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" +
          "\t\t\t\t\t\t█" + BLANC)
    print(JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" +
          "\t\t\t\t\t\t█" + BLANC)
    print(JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" +
          "\t\t\t\t\t\t█" + BLANC)

# histoire sur le menu
def lore():
    print(BLANC + """\n\n       Unité 13,\n
       C'est le moment de mettre vos nerfs à rude épreuve.                                                                                     \\\ /////
       Vos derniers exploits dans la bataille contre ce satané R-HuM, sont célèbres dans le corps entier.                                      |     '|
       Plusieurs virus non-identifiés ont fait irruption dans des cellules. Ils sont extrêmement dangereux.                                   (| _  _ |)
       En effet de par leurs déplacements totalement aléatoires, ils sont difficilement atteignables et particulièrement irritants.            |` |   |
       Ils sont de plus capables de déclencher des stress cellulaires provoquant une érruption de réactions comme : """
          + BLANC + "\t\t               |  __  |")
    print("\t\t  - " + ROUGE + "NameError Traceback (most recent call last)" +
          BLANC + "\t\t\t\t\t\t\t\t\t         >>>___/\_^__/\___<<<")
    print("\t\t  - " + ROUGE + "IndexError: index out of range" + BLANC +
          "\t\t\t\t\t\t\t\t\t\t        /               |||  \\ \n")
    print(
        """       ... vous obligeant à revenir sur le menu et relancer une partie. Mais si les virus sont calmes ça ne devrait pas arriver.\n
       Unité 13... Bonne Chance""")


def credit():

    for i in range(100):
        os.system('clear')
        print(BLEU + thomaspierrot + BLANC+"\n\n\n")
        print(BLEU+"\t\t\t Loading: "+BLANC+str(100*i/100)+" %"+BLANC + " "*i + VERT +"(■_■)"+ROUGE +"   (◣_◢)"+BLANC)
        print(""+BLEU+"\t\t\t______________________________" + "_"*i+BLANC+"_"*(100-i))
        time.sleep(0.04)

# Explications des règles
def instructions():
    os.system('clear')
    print(regles)
    print(keyboard)
    input("\n\n  Appuyer sur ENTRER pour revenir au menu...")


# Affichage de la grille
# Le principe est le suivant; Dans une boucle for, on print chaque élément de la liste 1 par 1 sans retour à la ligne (,end="").
# Tous les 10 éléments print, c'est à dire les index 9,19,29... définis par ( i % 10 == 9 ) on insert un retour à la ligne.
# Les tabulations (\t) servent à assurer une distance équivalente entre chaque éléments de la GRILLE
# Le reste n'est que des considérations graphiques comme à i == 9 par exemple où l'on print le titre à la fin avant d'effectuer un retour à la ligne
# Ceci permet d'afficher une section à droite de la grille contenant des éléments d'interface utilisateur.
def showGameBoard(grille, message):
    os.system('clear')
    barrehaute = "\n" + (JAUNE + "█" + BLANC) * 209
    barrebasse = (JAUNE + "█" + BLANC) * 209

    UI = {
        'Titre': '  VIRUS KILLER',
        'BOMBE1': VERT + '  Bombe 1' + BLEU + '   PUISSANCE:  ' + str(bombeloader["bombe1"][1]) + BLANC,
        'BOMBE2': VERT + '  Bombe 2' + BLEU + '   PUISSANCE:  ' + str(bombeloader["bombe2"][1]) + BLANC,
        'BOMBE3': VERT + '  Bombe 3' + BLEU + '   PUISSANCE:  ' + str(bombeloader["bombe3"][1]) + BLANC,
        'BOMBE4': VERT + '  Bombe 4' + BLEU + '   PUISSANCE:  ' + str(bombeloader["bombe4"][1]) + BLANC,
        'ATP': VERT + '',
        'VIRUSRESTANT': ROUGE + " (◣_◢) X " + str(grille.count(casevirus)) + BLANC,
    }

    print (barrehaute)
    print (JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" + "\t\t\t\t\t\t█" + BLANC)
    print (JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" + "\t\t\t\t\t\t█" + BLANC)

    for i in range(100):
        if i % 10 == 0:
            print (JAUNE + "█" + BLANC, end="")
        print (grille[i], end='')

        if i == 9:
            print (JAUNE + "█" + BLANC, UI["Titre"], JAUNE + "\t\t\t\t█" + BLANC)
            sautdeligne()
        if i == 19:
            print (JAUNE + "█" + "\t\t\t\t\t\t█" + BLANC)
            print (JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" + BLANC, UI["BOMBE1"], JAUNE + "\t\t\t█" + BLANC)
            print (JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" + BLANC, UI["BOMBE2"], JAUNE + "\t\t\t█" + BLANC)
            print (JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" + BLANC, UI["BOMBE3"], JAUNE + "\t\t\t█" + BLANC)
            print (JAUNE + "█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█" + BLANC, UI["BOMBE4"], JAUNE + "\t\t\t█" + BLANC)
        if i == 39:
            print (JAUNE + "█" + VERT, "  Virus restant: ", UI["VIRUSRESTANT"], JAUNE + "\t\t\t█" + BLANC)
            sautdeligne()
        if i == 49:
            print (JAUNE + "█" + BLANC, "  " + message)
            sautdeligne()
        if i % 10 == 9 and i not in [9, 19, 39, 49]:
            print (JAUNE + "█" + "\t\t\t\t\t\t█" + BLANC)
            sautdeligne()

    print (barrebasse)


def initvirus(virus):
    # Génére une liste de 4 index entre 0 et 99 dans la grille
    virus = random.sample(range(0, 100), 4)
    # Refais un aléa si les index généré sont sur des cases non vides
    while grille[virus[0]] != casevide or grille[virus[1]] != casevide or grille[virus[2]] != casevide or grille[virus[3]] != casevide:
        virus = random.sample(range(0, 100), 4)
    # on remplie la grille avec les 4 virus
    for i in range (len(virus)):
        grille[virus[i]] = casevirus
    return virus

# Renvoie une valeur aléatoire dans la grille à un emplacement casevide;
def randomingrille(n1, n2):
    value = random.randint(n1, n2)
    while grille[value] != casevide:
        value = random.randint(n1, n2)
    return value

# Renvoie true si la valeur testée sort de la grille ou reviens par l'autre coté
def passemuraille(oldpos, newpos):
    if (newpos < 0 or newpos > 99 or (oldpos % 10 == 9 and newpos % 10 == 0) or (oldpos % 10 == 0 and newpos % 10 == 9)):
        return True
    else:
        return False

# Initialisation des murs, choix de la difficulté (nombre et longueur des murs), sens aléatoire.
def initmurs():
    os.system("clear")
    # Choix de la difficulté génère des valeurs différente pour le nombre de murs et leurs longueurs.
    print("\n\t A quel niveau de difficulté voulez vous jouer ?\n\n\t " + BLEU + "Rhume: (1)" + ORANGE + "   Gastro: (2)" + ROUGE + "   Chikungunya: (3) " + BLANC)
    inputdifficulty = input("\n\n\t Niveau: ")
    if inputdifficulty == "1":
        nbmur = random.randint(3, 4)
        longmur = random.randint(2, 3)
    elif inputdifficulty == "2":
        nbmur = random.randint(4, 5)
        longmur = random.randint(4, 5)
    elif inputdifficulty == "3":
        nbmur = random.randint(5, 6)
        longmur = random.randint(6, 7)
    else:
        initmurs()

    # Boucle while pour générer tous les murs (while mur <= nbmur)
    mur = 1
    while mur <= nbmur:
        # On génère en suite soit un mur vertical (sensmur=1) soit un mur horizontal (sensmur=2)
        sensmur = random.randint(1, 2)
        # On tire une position au hasard sur la grille pourvu que la place soit disponible (avec la fonction randomingrille)
        startingpoint = randomingrille(0, 99)
        grille[startingpoint] = casemur
        # Pour les verticaux on remplie vers le haut. Si l'on sort de la grille (fonction passemuraille), on commence à remplir vers le bas.
        # On a donc besoin d'avoir des compteurs indépendant pour haut et bas.
        if sensmur == 1:
            haut = 0
            bas = 0
            for brique in range(1, longmur):
                oldpos = startingpoint - 10 * haut
                newpos = startingpoint - 10 * (haut + 1)
                if passemuraille(oldpos, newpos) is False:
                    grille[newpos] = casemur
                    haut = haut + 1

                else:
                    oldpos = startingpoint + 10 * bas
                    newpos = startingpoint + 10 * (bas + 1)
                    if passemuraille(oldpos, newpos) is False:
                        grille[newpos] = casemur
                        bas = bas + 1

        # Pour les horizontaux on remplie vers la gauche... si l'on sort de la grille, on commence à remplir vers la droite.
        # On a donc besoin d'avoir des compteurs indépendant pour gauche et droite.
        else:
            gauche = 0
            droite = 0
            for brique in range(1, longmur):
                oldpos = startingpoint - 1 * gauche
                newpos = startingpoint - 1 * (gauche + 1)
                if passemuraille(oldpos, newpos) is False:
                    grille[newpos] = casemur
                    gauche = gauche + 1

                else:
                    oldpos = startingpoint + 1 * droite
                    newpos = startingpoint + 1 * (droite + 1)
                    if passemuraille(oldpos, newpos) is False:
                        grille[newpos] = casemur
                        droite = droite + 1
        mur += 1

# Initialisation du joueur
def initjoueur(mouvement):
    joueur = randomingrille(0, 99)
    mouvement[1] = joueur
    grille[joueur] = casejoueur
    return mouvement

# Permet de compter combien d'ATP est présent dans la grille
def countATP():
    nbATP = 0
    for i in range(len(grille)):
        if grille[i] == caseATP:
            nbATP = nbATP + 1
    return nbATP

# Permet de générer de l'ATP sur un emplacement vide de la grille
def randomATP():
    randomATPpos = randomingrille(0, 99)
    return randomATPpos

# Génère de l'ATP tant qu'il y a moins de 8 molecules dans la grille.
def spawnATP():
    nbATP = countATP()
    while nbATP < 8:
        newATP = randomATP()
        grille[newATP] = caseATP
        nbATP = countATP()
    showGameBoard(grille, message)
    return grille

# Gestion des touches utilisés par le joueur pendant son tour de jeu.
def keyinput(mouvement):
    message="Début de votre tour" + JAUNE + "\t\t\t\t█" + BLANC
    showGameBoard(grille, message)
    # newpos et oldpos sont utilisés pour le déplacement, oldpos est conservé si la direction testée (newpos) ne réponds pas aux critères de déplacement
    newpos = mouvement[0]
    oldpos = mouvement[1]
    voh = mouvement[2]          # vertical ou horizontal ou none
    continuer = 1  # continuer le déplacement tant que continuer = 1

    inputkey = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    ► Action :  ")
    while inputkey not in ["z","q","s","d","1","2","3","4"," "]:
        inputkey = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    ► Selectionnez la bonne touche :  ")

    # aller vers le haut (z) si on s'est déplacé verticalement (v) ou pas encore déplacé (n)
    if inputkey == "z" and (voh == "v" or voh == "n"):
        newpos = oldpos - 10    # Pour aller vers le haut on enlève 10 à l'index.
        voh = "v"

    # aller vers la gauche (q) si on s'est déplacé horizontalement (h) ou pas encore déplacé (n)
    elif inputkey == "q" and (voh == "h" or voh == "n"):
        newpos = oldpos - 1
        voh = "h"

    # aller vers le bas (s) si on s'est déplacé verticalement (v) ou pas encore déplacé (n)
    elif inputkey == "s" and (voh == "v" or voh == "n"):
        newpos = oldpos + 10
        voh = "v"

    # aller vers la droite (d) si on s'est déplacé horizontalement (h) ou pas encore déplacé (n)
    elif inputkey == "d" and (voh == "h" or voh == "n"):
        newpos = oldpos + 1
        voh = "h"

    # poser une bombe si on ne s'est pas déplacé
    elif (inputkey in ["1", "2", "3", "4"] and voh == "n"):
        newpos = oldpos
        voh = "n"

    # empêche la pose de bombe si on s'est déplacé
    elif (inputkey in ["1", "2", "3", "4"] and voh != "n"):
        newpos = oldpos

    # demande de fin de tour (touche espace)
    elif (inputkey == " "):
        newpos = oldpos
        continuer = 0
 
    mouvement = [oldpos, newpos, voh, continuer]
    return mouvement, inputkey

# Fonction de déplacement du joueur et de posage de bombe - interprete la fonction keyinput.
def actionjoueur(mouvement, bombeloader):
    testmouvement, inputkey = keyinput(mouvement)
    oldpos = testmouvement[0]                       # oldpos= position actuelle
    newpos = testmouvement[1]                       # newpos = position a tester
    voh = testmouvement[2]                          # voh = type de deplacement
    continuer = testmouvement[3]                    # continuer = 0 ou 1

    if continuer == 0:                              # Cas où il y a eu touche espace: fin de tour
        mouvement = [oldpos, newpos, voh, continuer]
        return mouvement, bombeloader

    elif newpos != oldpos:                          # Si la nouvelle position testée est différente de l'ancienne il s'agit d'un déplacement.
        if passemuraille(oldpos, newpos) == True or grille[newpos] not in [casevide, caseATP]:  # Cas où le déplacement n'est pas autorisé
            continuer = 1
            message = "Vous ne pouvez pas aller là" + JAUNE + "\t\t\t█" + BLANC
        elif grille[newpos] == casevide:            # Cas où le déplacement est autorisé et va sur une case vide
            if (grille[oldpos] == casejoueurbomb):  # Cas où à l'ancienne position le joueur avait amorcé la bombe
                grille[oldpos] = casebomb
            else:                                   # Cas standard où l'ancienne position devient vide après déplacement du joueur
                grille[oldpos] = casevide
            grille[newpos] = casejoueur
            mouvement = [oldpos, newpos, voh, continuer]
            message = "Vous avancez" + JAUNE + "\t\t\t\t█" + BLANC
        elif grille[newpos] == caseATP:             # Cas où le déplacement est autorisé et va sur une case d'ATP
            if grille[oldpos] == casejoueurbomb:
                grille[oldpos] = casebomb
            else:
                grille[oldpos] = casevide
            grille[newpos] = casejoueur
            mouvement = [oldpos, newpos, voh, continuer]
            message = "Vous avancez" + JAUNE + "\t\t\t\t█" + BLANC
            boostbombe(bombeloader)                 # On boost deux bombes au hasard

    # Si la nouvelle position testée est identique à l'ancienne il s'agit d'une tentative d'amorçage de bombe
    # (la condition de fin de tour (continuer=0) où le joueur reste à la même position ayant été préalablement testé avec le premier if).
    elif (newpos == oldpos and voh != "n"):         # Cas où la bombe ne peut être posé car le joueur s'est déplacé
        grille[newpos] = casejoueur
        message = "Bombes inaccessible après déplacement" + JAUNE + "\t█" + BLANC

    elif (newpos == oldpos and voh == "n"):         # Cas où la bombe peut être posé
        grille[newpos] = casejoueurbomb
        tabulationdumessage = JAUNE + "\t\t█" + BLANC
        print ("INPUT=", inputkey)
        if inputkey == "1":
            bombeloader["bombe1"][0] = newpos
            message = "Vous venez de déposer la bombe 1" + tabulationdumessage
        elif inputkey == "2":
            bombeloader["bombe2"][0] = newpos
            message = "Vous venez de déposer la bombe 2" + tabulationdumessage
        elif inputkey == "3":
            bombeloader["bombe3"][0] = newpos
            message = "Vous venez de déposer la bombe 3" + tabulationdumessage
        elif inputkey == "4":
            bombeloader["bombe4"][0] = newpos
            message = "Vous venez de déposer la bombe 4" + tabulationdumessage
    showGameBoard(grille, message)
    return mouvement, bombeloader

# Renvoie pour un virus les directions possibles
def dirpossiblevirus(virus, numvirus):
    posvirus = virus[numvirus]
    dirpossible = []
    if posvirus > 9:
        if grille[posvirus - 10] == casevide:
            dirpossible.append(0)
    if posvirus < 90:
        if grille[posvirus + 10] == casevide:
            dirpossible.append(1)
    if posvirus > 0:
        if grille[posvirus - 1] == casevide and posvirus % 10 != 0:  # le virus ne peut aller vers la gauche si il est contre la paroi
            dirpossible.append(2)
    if posvirus < 99:
        if grille[posvirus + 1] == casevide and posvirus % 10 != 9:  # le virus ne peut aller vers la droite si il est contre la paroi
            dirpossible.append(3)
    if dirpossible == []:  # Dans le cas où les conditions ne sont pas remplis le virus essaie d'aller vers la gauche (sinon une erreur est renvoyé)
        dirpossible.append(1)
    return dirpossible

# Appel la fonction de déplacement aléatoire des virus en fonction de la direction possible
def randommovevirus(virus):
    for numvirus in range(len(virus)):
        if virus[numvirus] != "mort":
            oldvirpos = virus[numvirus]
            dirpossible = dirpossiblevirus(virus, numvirus)  # choix des directions où le virus ne sera pas bloqué
            direction = random.choice(dirpossible)
            if direction == 0:  # haut
                dirvalue = -10
                maxdistance = int(oldvirpos / 10) + (oldvirpos % 10 > 0)  # oldvirpos % 10 > 0 arrondie à la valeur supérieure
            elif direction == 1:  # bas
                dirvalue = 10
                maxdistance = 10 - int(oldvirpos / 10) + (oldvirpos % 10 > 0)
            elif direction == 2:  # gauche
                dirvalue = -1
                maxdistance = oldvirpos % 10 + 1
            elif direction == 3:  # droite
                dirvalue = +1
                maxdistance = 10 - (oldvirpos % 10)
            distance = random.randint(1, maxdistance)  # distance a parcourir
            pas = 0
            while pas < distance:
                movevirus(virus, numvirus, dirvalue)
                pas = pas + 1

# Fonction de déplacement des virus
def movevirus(virus, numvirus, dirvalue):
    oldvirpos = virus[numvirus]
    newposvir = oldvirpos + dirvalue
    message = "Les virus se déplacent" + JAUNE + "\t\t\t█" + BLANC
    if (newposvir > 0 and newposvir < 100):
        if passemuraille(oldvirpos, newposvir) is True:
            message = "Le virus tente en vain de passer la paroi" + JAUNE + "\t█" + BLANC
            time.sleep(0.3)
        else:
            if grille[newposvir] == casevide:
                grille[oldvirpos] = casevide
                virus[numvirus] = newposvir
                grille[newposvir] = casevirus
                time.sleep(0.3)
            else:
                time.sleep(0.1)
    showGameBoard(grille, message)

# Selectionne deux bombes aléatoirement parmis le chargeur et incrémente de 1 sa puissance
def boostbombe(bombeloader):
    selectrandombombe = random.sample(list(bombeloader.keys()), 2)
    bombeloader[selectrandombombe[0]][1] = bombeloader[selectrandombombe[0]][1] + 1
    bombeloader[selectrandombombe[1]][1] = bombeloader[selectrandombombe[1]][1] + 1
    return bombeloader

# Fonction explosion des bombes
def boom(bombeloader):
    activebombe = []
    for bombe in bombeloader.keys():  # détecte si une bombe a une valeur de position différente de "n"
        if bombeloader[bombe][0] != "n":
            activebombe.append(bombeloader[bombe][0])
            activebombe.append(bombeloader[bombe][1])
            bombeloader[bombe][1] = "X"

    if activebombe != []:
        posbombes = activebombe[0]
        rayon = int(activebombe[1] / 2) + (activebombe[1] % 2 > 0)
        print (rayon)
        for motif in [ROUGE + "\t  ✸  \t" + BLANC, casevide]:
            grille[posbombes] = motif
            i = 1
            while i <= rayon:
                if posbombes - 10 * i >= 0:
                    grille[posbombes - 10 * i] = motif
                if posbombes + 10 * i < 99:
                    grille[posbombes + 10 * i] = motif
                if rayon <= 2:  # Explosion en croix pour les bombes de rayons <= 2
                    if posbombes - 1 * i >= 0 and (posbombes - 1 * i) % 10 != 9:
                        grille[posbombes - 1 * i] = motif
                    if posbombes + 1 * i < 99 and (posbombes + 1 * i) % 10 != 0:
                        grille[posbombes + 1 * i] = motif
                i = i + 1
            message = "BOOOOM" + JAUNE + "\t\t\t\t\t█" + BLANC
            showGameBoard(grille, message)
            time.sleep(1)
        for item in bombeloader.keys():
            bombeloader[item][0] = "n"
        return bombeloader

 # Fonction de recharge de bombe après explosion
def reloadbombe(bombeloader):
    for slot in bombeloader.keys():
        if bombeloader[slot][1] == "X":
            val = random.sample([3, 5, 7, 9], 1)
            bombeloader[slot][1] = val[0]

# Fonction qui décrémante la puissance des bombes de 1
def bombemolle(bombeloader):
    for slot in bombeloader.keys():
        if bombeloader[slot][1] != 0:  # Les bombes ne peuvent pas avoir une puissance négative
            bombeloader[slot][1] = bombeloader[slot][1] - 1
    showGameBoard(grille, message)
    return bombeloader

# Regarde quels sont les virus qui sont mort (après explosion)
def constatdesmorts(virus):
    for individus in range(0, 4):
        if virus[individus] != "mort":
            if grille[virus[individus]] == casevide:
                virus[individus] = "mort"
    return virus

# Gagné si 4 virus sont mort (nbmort == 4)
def win(virus):
    victory = 0
    nbmort = virus.count("mort")
    if nbmort == 4:
        victory = 1
        os.system('clear')
        print (iconvictory)
        time.sleep(3)
    return victory

# Perdu si les 4 bombes sont à zéro de puissance
def loose(bombeloader):
    bombeazero = 0
    for item in bombeloader.keys():
        if bombeloader[item][1] <= 0:
            bombeazero = bombeazero + 1
    rip = 0
    if bombeazero == 4:
        rip = 1
        os.system('clear')
        print (icondefaite)
        time.sleep(3)
    return rip


# Fonction tour de jeu
def startgame(virus, mouvement, grille, message, bombeloader, ATP):
    initmurs()                                             # Initialise les murs
    initjoueur(mouvement)                                  # Initialise le joeur
    virus = initvirus(virus)                               # Initialise les virus
    spawnATP()                                             # Initialise l'ATP
    showGameBoard(grille, message)                         # Affiche la grille
    victory = win(virus)                                   # Condition de victoire
    rip = loose(bombeloader)                               # Condition de défaire

    while victory == 0 and rip == 0:                       # Jouer tant qu'il n'y a ni victoire ni défaite
        randommovevirus(virus)                             # Mouvement des virus  
        while mouvement[3] == 1:                           # Fonction mouvement tant que mouvement[continuer] == 1
            mouvement, bombeloader = actionjoueur(mouvement, bombeloader)
        boom(bombeloader)                                  # Explosion éventuelle des bombes
        virus = constatdesmorts(virus)                     # Recalcul du nombre de virus encore en vie
        spawnATP()                                         # Régénère le nombre d'ATP sur la grille
        reloadbombe(bombeloader)                           # Recrée une bombe de puissance aléatoire si une bombe a été posée
        bombemolle(bombeloader)                            # Décrémente la puissance des bombes
        victory = win(virus)                               # Re-vérifie si les conditions de victoire sont réunies (victory = 1 ?)
        rip = loose(bombeloader)                           # Re-vérifie si les conditions de défaite sont réunies (victory = 1 ?)
        mouvement[2] = "n"                                 # Réinitialise le type de mouvement du joueur à "n"
        mouvement[3] = 1                                   # Ré-autorise le joueur à bouger

    input('     Appuyer sur entrer pour continuer... ')    # Partie terminée
    menu()


def menu():
    os.system("clear")
    print (JAUNE + iconbombe + BLANC)
    lore()
    time.sleep(1)
    input(ORANGE + "\n\n       Appuyer sur ENTRER pour continuer..." + BLANC)
    os.system("clear")
    print (JAUNE + iconbombe + BLANC)
    print (VIOLET + iconmenu + BLANC)
    selection = input("\n\n\t\t\t\t\t\t\t\t Choix: ")
    if selection == "1":
        startgame(virus, mouvement, grille, message, bombeloader, ATP)
    if selection == "2":
        instructions()
    if selection == "0":
        sys.exit()
    else:
        menu()


# -- MAIN ---
credit()
menu()
