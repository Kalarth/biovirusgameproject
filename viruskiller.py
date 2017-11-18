    #!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import time
#from tkinter import *

os.system('clear')

######################################################################
######################################################################
######################## PARTIE GRAPHIQUE ############################
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
casevirus=ROUGE+"\t (◣_◢) \t"+BLANC
casevide=ROUGE+"\t   .   \t"+BLANC
casejoueur=VERT+"\t【•◡•】\t"+BLANC

casejoueurbomb=ORANGE+"\t(■_■)☢\t"+BLANC
casebomb=""+JAUNE+"\t 💣 \t"+BLANC
caseATP=BLEU+"\t ( ϟ ) \t"+BLANC
casemurver="\t  "+"\033[0;33;43m"+" ⬛"+BLANC+"\t"
casemurhor="\t  "+"\033[0;33;43m"+" ⬛"+BLANC+"\t"
thomaspierrot="""
\n\n\n
\t\t\t /████████ /██
\t\t\t|__  ██__/| ██
\t\t\t   | ██   | ███████   /██████  /███████████   /██████   /███████
\t\t\t   | ██   | ██__  ██ /██__  ██| ██_  ██_  ██ |____  ██ /██_____/
\t\t\t   | ██   | ██  \ ██| ██  \ ██| ██ \ ██ \ ██  /███████|  ██████
\t\t\t   | ██   | ██  | ██| ██  | ██| ██ | ██ | ██ /██__  ██ \____  ██
\t\t\t   | ██   | ██  | ██|  ██████/| ██ | ██ | ██|  ███████ /███████/
\t\t\t   |__/   |__/  |__/ \______/ |__/ |__/ |__/ \_______/|_______/
\n
\t\t\t\t                         /███
\t\t\t\t                        /██ ██
\t\t\t\t                       |  ███
\t\t\t\t                        /██ ██/██
\t\t\t\t                       | ██  ██_/
\t\t\t\t                       | ██   ██
\t\t\t\t                       |  ████/██
\t\t\t\t                        \____/\_/
\t\t\t
\t\t\t\t\t /███████  /██                                           /██
\t\t\t\t\t| ██    ██|__/                                          | ██
\t\t\t\t\t| ██    ██ /██  /██████   /██████   /██████   /██████  /██████
\t\t\t\t\t| ███████/| ██ /██__  ██ /██__  ██ /██__  ██ /██    ██|_  ██_/
\t\t\t\t\t| ██____/ | ██| ████████| ██  \__/| ██  \__/| ██    ██  | ██
\t\t\t\t\t| ██      | ██| ██_____/| ██      | ██      | ██    ██  | ██ /██
\t\t\t\t\t| ██      | ██|  ███████| ██      | ██      |  ██████/  |  ████/
\t\t\t\t\t|__/      |__/ \_______/|__/      |__/       \______/    \____/
"""
iconbombe="""
\n
                        . . .
                         \|/
                       `--+--'
                         /|\\
                        ' | '
                          |
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._              \t /██    /██ /██                                     /██   /██ /██ /██ /██                              ▀▄   ▄▀
                ,-'###############`-.           \t| ██   | ██|__/                                    | ██  /██/|__/| ██| ██                             ▄█▀███▀█▄
              ,'#####################`,         \t| ██   | ██ /██  /██████  /██   /██  /███████      | ██ /██/  /██| ██| ██  /██████   /██████         █▀███████▀█
             /#########################|        \t|  ██ / ██/| ██ /██__  ██| ██  | ██ /██_____/      | █████/  | ██| ██| ██ /██__  ██ /██__  ██        █ █▀▀▀▀▀█ █
            |###########################|       \t \  ██ ██/ | ██| ██  \__/| ██  | ██|  ██████       | ██  ██  | ██| ██| ██| ████████| ██  \__/           ▀▀ ▀▀
           |#############################|      \t  \  ███/  | ██| ██      | ██  | ██ \____  ██      | ██\  ██ | ██| ██| ██| ██_____/| ██
           |#############################|      \t   \  █/   | ██| ██      |  ██████/ /███████/      | ██ \  ██| ██| ██| ██|  ███████| ██                   █
           |#############################|      \t    \_/    |__/|__/       \______/ |_______/       |__/  \__/|__/|__/|__/ \_______/|__/               █
           |#############################|
           |#############################|                                                                                                                  █
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'
"""

iconmenu="""
\t\t\t\t\t\t\t\t   _                _
\t\t\t\t\t\t\t\t /  |              | |   ___    _   _    ___   _ __
\t\t\t\t\t\t\t\t  | |           _  | |  / _ \  | | | |  / _ \ | '__|
\t\t\t\t\t\t\t\t  | |     _    | |_| | | (_) | | |_| | |  __/ | |
\t\t\t\t\t\t\t\t  |_|    (_)    \___/   \___/   \__,_|  \___| |_|
\t\t\t\t\t\t\t\t  ____          ___                 _                           _     _
\t\t\t\t\t\t\t\t |___ \        |_ _|  _ __    ___  | |_   _ __   _   _    ___  | |_  (_)   ___    _ __    ___
\t\t\t\t\t\t\t\t   __) |        | |  | '_ \  / __| | __| | '__| | | | |  / __| | __| | |  / _ \  | '_ \  / __|
\t\t\t\t\t\t\t\t  / __/   _     | |  | | | | \__ \ | |_  | |    | |_| | | (__  | |_  | | | (_) | | | | | \__ \\
\t\t\t\t\t\t\t\t |_____| (_)   |___| |_| |_| |___/  \__| |_|     \__,_|  \___|  \__| |_|  \___/  |_| |_| |___/
\t\t\t\t\t\t\t\t   ___           ___            _   _     _
\t\t\t\t\t\t\t\t  / _ \         / _ \   _   _  (_) | |_  | |_    ___   _ __
\t\t\t\t\t\t\t\t | | | |       | | | | | | | | | | | __| | __|  / _ \ | '__|
\t\t\t\t\t\t\t\t | |_| |  _    | |_| | | |_| | | | | |_  | |_  |  __/ | |
\t\t\t\t\t\t\t\t  \___/  (_)    \__\_\  \__,_| |_|  \__|  \__|  \___| |_|
"""


regles=ORANGE+"""
        .-----------------------------------------------------------------------------------------------------------------.
        | Vous devez:                                                                                                     |
        |     - Appuyer sur """+BLANC+"ENTRER"+ORANGE+""" pour valider chacune de vos instructions (Z,Q,S,D,1,2,3,4,ESPACE)\t                  |
        |     - Appuyer sur """+BLANC+"ESPACE"+ORANGE+""" pour finir votre tour                                                                  |
        |     - Ramasser de l'ATP pour régénérer la puissance des bombes:\t"""+caseATP+ORANGE+"""\t                  |
        |     - Poser des bombes pour tuer les virus\t\t\t"""+casevirus+ORANGE+"""                                  |
        |                                                                                                                 |
        | Vous ne pouvez pas:                                                                                             |
        |     - Poser de bombe après déplacement                                                                          |
        |     - Vous déplacer verticalement après vous être déplacés horizontalement et réciproquement                    |
        |     - Passer les parois cellulaires                                                                             |
        '-----------------------------------------------------------------------------------------------------------------' """+BLANC
keyboard=BLEU+"""
                        HAUT                                     BOMBE 1               BOMBE 2              BOMBE 3              BOMBE 4
                  .----------------.                        .----------------.   .----------------.   .----------------.   .----------------.
                 | .--------------. |                      | .--------------. | | .--------------. | | .--------------. | | .--------------. |
                 | |   ________   | |                      | |     __       | | | |    _____     | | | |    ______    | | | |   _    _     | |
                 | |  |  __   _|  | |                      | |    /  |      | | | |   / ___ `.   | | | |   / ____ `.  | | | |  | |  | |    | |
                 | |  |_/  / /    | |                      | |    `| |      | | | |  |_/___) |   | | | |   `'  __) |  | | | |  | |__| |_   | |
                 | |     .'.' _   | |                      | |     | |      | | | |   .'____.'   | | | |   _  |__ '.  | | | |  |____   _|  | |
                 | |   _/ /__/ |  | |                      | |    _| |_     | | | |  / /____     | | | |  | \____) |  | | | |      _| |_   | |
                 | |  |________|  | |                      | |   |_____|    | | | |  |_______|   | | | |   \______.'  | | | |     |_____|  | |
                 | |              | |                      | |              | | | |              | | | |              | | | |              | |
                 | '--------------' |                      | '--------------' | | '--------------' | | '--------------' | | '--------------' |
                  '----------------'                        '----------------'   '----------------'   '----------------'   '----------------'
.----------------.   .----------------.   .----------------.  .---------------------------------------------------------------------------------.
| .--------------. | | .--------------. | | .--------------. | | .-----------------------------------------------------------------------------.  |
| |    ___       | | | |    _______   | | | |  ________    | | | |                                                                              | |
| |  .'   '.     | | | |   /  ___  |  | | | | |_   ___ `.  | | | |                                                                              | |
| | |  .-.  \    | | | |  |  (__ \_|  | | | |   | |   `. \ | | | |                                                                              | |
| | | |   | |    | | | |   '.___`-.   | | | |   | |    | | | | | |                                                                              | |
| | | ' _ ' \    | | | |  |`\____) |  | | | |  _| |___.' / | | | |   \______________________________________________________________________/   | |
| |  `.___.\ |   | | | |  |_______.'  | | | | |________.'  | | | |                                                                              | |
| |              | | | |              | | | |              | | | |                                                                              | |
| '--------------' | | '--------------' | | '--------------' | | '------------------------------------------------------------------------------' |
'----------------'   '----------------'   '----------------'  '----------------------------------------------------------------------------------'
   GAUCHE                BAS                  DROITE                                           FIN DU TOUR
"""+BLANC

iconvictory=BLEU+"""
████████           ██████████████████      ████████████████████████████████████     █████████     █████████████████   ███████       ███████
█░░░░░░█           █░░░░░░██░░░░░░░░█   ███░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░█   ██░░░░░░░░░██   █░░░░░░░░░░░░░░░░█  █░░░░░█       █░░░░░█
█░░░░░░█           █░░░░░░██░░░░░░░░█ ██░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░█ ██░░░░░░░░░░░░░██ █░░░░░░██████░░░░░█ █░░░░░█       █░░░░░█
█░░░░░░█           █░░░░░░███░░░░░░███░░░░░████████░░░░██░░░░░██░░░░░░░██░░░░░██░░░░░░░███░░░░░░░███░░░░░█     █░░░░░██░░░░░░█     █░░░░░░█
 █░░░░░█           █░░░░░█   █░░░░█ █░░░░░█       ████████████  █░░░░░█  ███████░░░░░░█   █░░░░░░█  █░░░░█     █░░░░░████░░░░░█   █░░░░░███
  █░░░░░█         █░░░░░█    █░░░░██░░░░░█                      █░░░░░█        █░░░░░█     █░░░░░█  █░░░░█     █░░░░░█   █░░░░░█ █░░░░░█
   █░░░░░█       █░░░░░█     █░░░░██░░░░░█                      █░░░░░█        █░░░░░█     █░░░░░█  █░░░░██████░░░░░█     █░░░░░█░░░░░█
    █░░░░░█     █░░░░░█      █░░░░██░░░░░█                      █░░░░░█        █░░░░░█     █░░░░░█  █░░░░░░░░░░░░░██       █░░░░░░░░░█
     █░░░░░█   █░░░░░█       █░░░░██░░░░░█                      █░░░░░█        █░░░░░█     █░░░░░█  █░░░░██████░░░░░█       █░░░░░░░█
      █░░░░░█ █░░░░░█        █░░░░██░░░░░█                      █░░░░░█        █░░░░░█     █░░░░░█  █░░░░█     █░░░░░█       █░░░░░█
       █░░░░░█░░░░░█         █░░░░██░░░░░█                      █░░░░░█        █░░░░░█     █░░░░░█  █░░░░█     █░░░░░█       █░░░░░█
        █░░░░░░░░░█          █░░░░█ █░░░░░█       ██████        █░░░░░█        █░░░░░░█   █░░░░░░█  █░░░░█     █░░░░░█       █░░░░░█
         █░░░░░░░█         ██░░░░░░███░░░░░████████░░░░█      ██░░░░░░░██      █░░░░░░░███░░░░░░░███░░░░░█     █░░░░░█       █░░░░░█
          █░░░░░█          █░░░░░░░░█ ██░░░░░░░░░░░░░░░█      █░░░░░░░░░█       ██░░░░░░░░░░░░░██ █░░░░░░█     █░░░░░█    ████░░░░░████
           █░░░█           █░░░░░░░░█   ███░░░░░░░░░░░░█      █░░░░░░░░░█         ██░░░░░░░░░██   █░░░░░░█     █░░░░░█    █░░░░░░░░░░░█
            ███            ██████████      █████████████      ███████████           █████████     ████████     ███████    █████████████
"""+BLANC

icondefaite=ROUGE+"""\n\n
████████▄     ▄████████    ▄████████    ▄████████  ▄█      ███        ▄████████
███   ▀███   ███    ███   ███    ███   ███    ███ ███  ▀█████████▄   ███    ███
███    ███   ███    █▀    ███    █▀    ███    ███ ███▌    ▀███▀▀██   ███    █▀
███    ███  ▄███▄▄▄      ▄███▄▄▄       ███    ███ ███▌     ███   ▀  ▄███▄▄▄
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀███████████ ███▌     ███     ▀▀███▀▀▀
███    ███   ███    █▄    ███          ███    ███ ███      ███       ███    █▄
███   ▄███   ███    ███   ███          ███    ███ ███      ███       ███    ███
████████▀    ██████████   ███          ███    █▀  █▀      ▄████▀     ██████████
"""+BLANC

######################## FIN PARTIE GRAPHIQUE ########################
######################################################################
######################################################################

grille=[ROUGE+"\t   .   \t"+BLANC]*100
virus=[]
ATP=[]

bombeloader={"bombe1":["n",8],"bombe2":["n",6],"bombe3":["n",4],"bombe4":["n",2]} #bombe:[position,puissance]
mouvement=[0,random.randint(0,99),"n",1]
message="Tours de Jeu"+JAUNE+"\t\t\t\t█"+BLANC


def sautdeligne():
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+"\t\t\t\t\t\t█"+BLANC)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+"\t\t\t\t\t\t█"+BLANC)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+"\t\t\t\t\t\t█"+BLANC)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+"\t\t\t\t\t\t█"+BLANC)

def lore():
    print(BLANC+"""\n\n       Unité 13,\n
       C'est le moment de mettre vos nerfs à rude épreuve.                                                                                     \\\ /////
       Vos derniers exploits dans la bataille contre ce satané R-HuM, sont célèbres dans le corps entier.                                      |     '|
       Plusieurs virus non-identifiés ont fait irruption dans des cellules. Ils sont extrêmement dangereux.                                   (| _  _ |)
       En effet de par leurs déplacements totalement aléatoire, ils sont difficilement atteignables et particulièrement irritants.             |` |   |
       Ils sont de plus capables de déclencher des stress cellulaires provoquant une érruption de réactions comme : """+BLANC+"\t\t               |  __  |")
    print("\t\t  - "+ROUGE+"NameError Traceback (most recent call last)"+BLANC+"\t\t\t\t\t\t\t\t\t         >>>___/\_^__/\___<<<")
    print("\t\t  - "+ROUGE+"IndexError: index out of range"+BLANC+"\t\t\t\t\t\t\t\t\t\t        /               |||  \\ \n")
    print("""       ... vous obligeant à revenir sur le menu et relancer une partie. Mais si les virus sont calmes ça ne devrait pas arriver.\n
       Unité 13... Bonne Chance""")

def credit():
    print(BLEU+thomaspierrot+BLANC)
    time.sleep(2)

def instructions():
    os.system('clear')
    print(regles)
    print (keyboard)
    input("\n\n  Appuyer sur ENTRER pour revenir au menu...")


def showGameBoard(grille,message):
    os.system('clear')
    barrehaute="\n"+(JAUNE+"█"+BLANC)*209
    barrebasse=(JAUNE+"█"+BLANC)*209

    UI={'Titre':'  VIRUS KILLER',
    'BOMBE1':VERT+'  Bombe 1'+BLEU+'   PUISSANCE:  '+str(bombeloader["bombe1"][1])+BLANC,
    'BOMBE2':VERT+'  Bombe 2'+BLEU+'   PUISSANCE:  '+str(bombeloader["bombe2"][1])+BLANC,
    'BOMBE3':VERT+'  Bombe 3'+BLEU+'   PUISSANCE:  '+str(bombeloader["bombe3"][1])+BLANC,
    'BOMBE4':VERT+'  Bombe 4'+BLEU+'   PUISSANCE:  '+str(bombeloader["bombe4"][1])+BLANC,
    'ATP':VERT+'',
    'sample':" ",
    'VIRUSRESTANT':ROUGE+" (◣_◢) X "+str(grille.count(casevirus))+BLANC,
    }

    print (barrehaute)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+"\t\t\t\t\t\t█"+BLANC)
    print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+"\t\t\t\t\t\t█"+BLANC)
    for i in range(0,100):
        if i%10==0:
            print (JAUNE+"█"+BLANC,end="")
        print (grille[i],end='')

        if i==9:
            print (JAUNE+"█"+BLANC,UI["Titre"],JAUNE+"\t\t\t\t█"+BLANC)
            sautdeligne()
        if i==19:
            print (JAUNE+"█"+"\t\t\t\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC,UI["BOMBE1"],JAUNE+"\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC,UI["BOMBE2"],JAUNE+"\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC,UI["BOMBE3"],JAUNE+"\t\t\t█"+BLANC)
            print (JAUNE+"█\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t█"+BLANC,UI["BOMBE4"],JAUNE+"\t\t\t█"+BLANC)
        if i==39:
            print (JAUNE+"█"+VERT,"  Virus restant: ",UI["VIRUSRESTANT"],JAUNE+"\t\t\t█"+BLANC)
            sautdeligne()
        if i==49:
            print (JAUNE+"█"+BLANC,"  "+message)
            sautdeligne()
        if i%10==9 and i not in [9,19,39,49]:
            print (JAUNE+"█"+"\t\t\t\t\t\t█"+BLANC)
            sautdeligne()

    print (barrebasse)


def initvirus(virus):
    virus=random.sample(range(0,99),4) #list of 4 different number
    while grille[virus[0]]!=casevide or grille[virus[1]]!=casevide or grille[virus[2]]!=casevide or grille[virus[3]]!=casevide: #Generation de virus en dehors des parois
            virus=random.sample(range(0,99),4)
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
    joueur=mouvement[1]
    grille[joueur]=casejoueur

def countATP():
    nbATP=0
    for i in range(len(grille)):
        if grille[i]==caseATP:
            nbATP=nbATP+1
    return nbATP

def randomATP():
    randomATPpos=random.randint(0,99)
    while grille[randomATPpos]!=casevide:
        randomATPpos=random.randint(0,99)
    return randomATPpos

def spawnATP():
    nbATP=countATP()
    while nbATP<8:
        newATP=randomATP()
        print(newATP)
        grille[newATP]=caseATP
        nbATP=countATP()
    showGameBoard(grille,message)
    return grille


def keyinput(mouvement):
    newpos=mouvement[0]
    oldpos=mouvement[1]
    voh=mouvement[2] #vertical ou horizontal ou none

    inputkey=input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    ► Action :  ")
    if inputkey=="z" and (voh=="v" or voh=="n"):  #aller vers le haut si on s'est déplacé verticalement ou pas déplacé
        newpos=oldpos-10
        voh="v" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey

    if inputkey=="q" and (voh=="h" or voh=="n"):    #aller vers la gauche si on s'est déplacé horizontalement ou pas déplacé
        newpos=oldpos-1
        voh="h" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey


    if inputkey=="s" and (voh=="v" or voh=="n"):    #aller vers le bas si on s'est déplacé verticalement ou pas déplacé
        newpos=oldpos+10
        voh="v" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey


    if inputkey=="d" and (voh=="h" or voh=="n"):    #aller vers la droite si on s'est déplacé horizontalement ou pas déplacé
        newpos=oldpos+1
        voh="h" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey

    if (inputkey=="1" and voh=="n"):                #poser une bombe si on ne s'est pas déplace
        newpos=oldpos
        voh="n" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey

    if (inputkey=="2" and voh=="n"):                #poser une bombe si on ne s'est pas déplace
        newpos=oldpos
        voh="n" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey

    if (inputkey=="3" and voh=="n"):                #poser une bombe si on ne s'est pas déplace
        newpos=oldpos
        voh="n" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey

    if (inputkey=="4" and voh=="n"):                #poser une bombe si on ne s'est pas déplace
        newpos=oldpos
        voh="n" #vertical ou horizontal
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey


    if ((inputkey=="1" or inputkey=="2" or inputkey=="3" or inputkey=="4") and voh!="n"):                #ne pas poser une bombe si on s'est déplacé
        newpos=oldpos
        continuer=1
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey

    if (inputkey==" "):                #ne pas poser une bombe si on s'est déplacé
        newpos=oldpos
        continuer=0
        mouvement=[oldpos,newpos,voh,continuer]
        return mouvement,inputkey


    else:
        return mouvement,inputkey



def movejoueur(mouvement):
        testmouvement,inputkey=keyinput(mouvement)
        oldpos=testmouvement[0]
        newpos=testmouvement[1]
        voh=testmouvement[2]
        continuer=testmouvement[3]
        print(inputkey)

        if continuer==0:
            mouvement=[oldpos,newpos,voh,continuer]
            return mouvement,bombeloader

        if newpos != oldpos:
            if  newpos<0 or newpos>=100 or grille[newpos] not in [casevide,caseATP] or (oldpos%10==9 and newpos%10==0) or (oldpos%10==0 and newpos%10==9):
                #Test si on va sur une valeur hors liste, si on va sur une case non vide ou si on cherche a "se teleporter d'un bords a l'autre"
                message="Vous ne pouvez pas aller là"+JAUNE+"\t\t\t█"+BLANC
                showGameBoard(grille,message)
                #print ("Vous ne pouvez pas avancer dans cette direction")
                #print (mouvement)
                continuer=1
                return mouvement,bombeloader

            if grille[newpos] == casevide: #test si on va sur une case vide
                if (grille[oldpos]==casejoueurbomb): #TEST DE CASE BOMBE
                    grille[oldpos]=casebomb
                else:
                    grille[oldpos]=casevide
                grille[newpos]=casejoueur
                mouvement=[oldpos,newpos,voh,continuer]

                message="Vous avancez"+JAUNE+"\t\t\t\t█"+BLANC
                showGameBoard(grille,message)

                #print (mouvement)
                return mouvement,bombeloader

            if grille[newpos] == caseATP: #test si on va sur une case vide
                if grille[oldpos]==casejoueurbomb: #TEST DE CASE BOMBE
                    grille[oldpos]=casebomb
                else:
                    grille[oldpos]=casevide
                grille[newpos]=casejoueur
                mouvement=[oldpos,newpos,voh,continuer]

                message="Vous avancez"+JAUNE+"\t\t\t\t█"+BLANC
                boostbombe(bombeloader)
                showGameBoard(grille,message)
                #print (mouvement)
                return mouvement,bombeloader


        if (newpos == oldpos and voh!="n"):
            grille[newpos]=casejoueur
            message="Bombes inaccessible après déplacement"+JAUNE+"\t█"+BLANC
            showGameBoard(grille,message)
            return mouvement,bombeloader


        if (newpos == oldpos and voh=="n"):
            grille[newpos]=casejoueurbomb
            tabulationbomb=JAUNE+"\t\t█"+BLANC
            print ("INPUT=",inputkey)
            if inputkey=="1":
                bombeloader["bombe1"][0]=newpos
                message="Vous venez de déposer la bombe 1"+tabulationbomb
                showGameBoard(grille,message)
                return mouvement,bombeloader
            if inputkey=="2":
                bombeloader["bombe2"][0]=newpos
                message="Vous venez de déposer la bombe 2"+tabulationbomb
                showGameBoard(grille,message)
                return mouvement,bombeloader
            if inputkey=="3":
                bombeloader["bombe3"][0]=newpos
                message="Vous venez de déposer la bombe 3"+tabulationbomb
                showGameBoard(grille,message)
                return mouvement,bombeloader
            if inputkey=="4":
                bombeloader["bombe4"][0]=newpos
                message="Vous venez de déposer la bombe 4"+tabulationbomb
                showGameBoard(grille,message)
                return mouvement,bombeloader


def dirpossiblevirus(virus,numvirus):
    posvirus=virus[numvirus]
    dirpossible=[]

    if posvirus > 0: #permet de ne pas dépasser les valeurs de la grille
        if grille[posvirus-1] == casevide and posvirus%10!=0:
            dirpossible.append(2)

    if posvirus < 99: #permet de ne pas dépasser les valeurs de la grille
        if grille[posvirus+1] == casevide and posvirus%10!=9:
            dirpossible.append(3)

    if posvirus > 9: #permet de ne pas dépasser les valeurs de la grille
        if grille[posvirus-10] == casevide:
            dirpossible.append(0)

    if posvirus < 90: #permet de ne pas dépasser les valeurs de la grille
        if grille[posvirus+10] == casevide:
            dirpossible.append(1)

    return dirpossible

def randommovevirus(virus):
    for numvirus in range(len(virus)):
        if virus[numvirus]!="mort":
            oldvirpos=virus[numvirus]
            #test des cases alentours pour choisir une direction où le virus ne sera pas bloqué
            dirpossible=dirpossiblevirus(virus,numvirus)
            direction=random.choice(dirpossible)
            j=0
            if direction==0: #haut
                dirvalue=-10
                maxdistance=int(oldvirpos/10)+ (oldvirpos % 10 > 0)
                distance=random.randint(1,maxdistance)#distance a parcourir
                while j < distance:
                    movevirus(virus,numvirus,dirvalue)
                    j=j+1

            if direction==1: #bas
                dirvalue=10
                maxdistance=10- int(oldvirpos/10)+ (oldvirpos % 10 > 0) # oldvirpos % 10 > 0 return 1 si true -> donc ajoute 1 si il y a un reste
                distance=random.randint(1,maxdistance)#distance a parcourir
                while j < distance:
                    movevirus(virus,numvirus,dirvalue)
                    j=j+1

            if direction==2: #gauche
                dirvalue=-1
                maxdistance=oldvirpos % 10 +1
                distance=random.randint(1,maxdistance)#distance a parcourir
                while j < distance:
                    movevirus(virus,numvirus,dirvalue)
                    j=j+1


            if direction==3: #gauche
                dirvalue=+1
                maxdistance=10-(oldvirpos % 10)
                distance=random.randint(1,maxdistance)#distance a parcourir
                while j < distance:
                    movevirus(virus,numvirus,dirvalue)
                    j=j+1


def movevirus(virus,numvirus,dirvalue):
    oldvirpos=virus[numvirus]
    #print ("OLDVIRPOS=",oldvirpos)
    newposvir=oldvirpos+dirvalue #test de la case cible
    #print ("TESTMOVEVIRUS=",newposvir)
    message="Les virus se déplacent"+JAUNE+"\t\t\t█"+BLANC
    if (newposvir > 0 and newposvir < 100):
        if (oldvirpos%10==9 and newposvir%10==0) or (oldvirpos%10==0 and newposvir%10==9):
            #print("ON PEUT PAS TRAVERSER LES MURS T'ES FOU")
            message="Le virus tente en vain de passer la paroi"+JAUNE+"\t█"+BLANC
            time.sleep(0.3)
            showGameBoard(grille,message)
        else:
            #verification que la valeur n'est pas hors range ou ne traverse pas les murs
            if grille[newposvir]==casevide:

                grille[oldvirpos]=casevide
                virus[numvirus]=newposvir
                grille[newposvir]=casevirus
                #print ("j'ai bougé normalement")
                time.sleep(0.3)
                showGameBoard(grille,message)

            else:
                #print ("le virus peut pas bouger plus loin")
                time.sleep(0.1)
                showGameBoard(grille,message)

    #else:
    #    print("PAS DANS LA RANGE DE LA GRILLE")


def boostbombe(bombeloader):
    i=0
    while i < 2:
        selectrandombombe=random.choice(list(bombeloader.keys()))
        bombeloader[selectrandombombe][1]=bombeloader[selectrandombombe][1]+1
        i=i+1
    return bombeloader

def boom(bombeloader):
    activebombe=[]
    if bombeloader["bombe1"][0]!="n":
        activebombe.append(bombeloader["bombe1"][0])
        activebombe.append(bombeloader["bombe1"][1])
        bombeloader["bombe1"][1]="X"
    if bombeloader["bombe2"][0]!="n":
        activebombe.append(bombeloader["bombe2"][0])
        activebombe.append(bombeloader["bombe2"][1])
        bombeloader["bombe2"][1]="X"
    if bombeloader["bombe3"][0]!="n":
        activebombe.append(bombeloader["bombe3"][0])
        activebombe.append(bombeloader["bombe3"][1])
        bombeloader["bombe3"][1]="X"
    if bombeloader["bombe4"][0]!="n":
        activebombe.append(bombeloader["bombe4"][0])
        activebombe.append(bombeloader["bombe4"][1])
        bombeloader["bombe4"][1]="X"
    print("BOMBE ACTIVE:  ",activebombe)

    if activebombe!=[]:
        posbombes=activebombe[0]
        rayon=int(activebombe[1]/2)+ (activebombe[1] % 2 > 0)
        print (rayon)
        grille[posbombes]=ROUGE+"\t  ✸  \t"+BLANC
        i=1
        while i <= rayon:
            if posbombes-10*i >= 0:
                grille[posbombes-10*i]="\t  ✸  \t"
            if posbombes+10*i < 99:
                grille[posbombes+10*i]="\t  ✸  \t"
            i=i+1
        message="BOOOOM"+JAUNE+"\t\t\t\t\t█"+BLANC
        showGameBoard(grille,message)
        time.sleep(2)
        grille[posbombes]=casevide
        k=1
        while k <= rayon:
            if posbombes-10*k >= 0:
                grille[posbombes-10*k]=casevide
            if posbombes+10*k < 99:
                grille[posbombes+10*k]=casevide
            k=k+1
        showGameBoard(grille,message)
        for item in bombeloader.keys():
            bombeloader[item][0]="n"
        return bombeloader

def reloadbombe(bombeloader):
    for slot in bombeloader.keys():
        if bombeloader[slot][1]=="X":
            val =random.sample([3,5,7,9],1)
            bombeloader[slot][1]=val[0]

def bombemolle(bombeloader):
    for slot in bombeloader.keys():
        print("bombeloader[slot][1]",bombeloader[slot][1])
        if bombeloader[slot][1]!=0: #Les bombes peuvent pas etre négative yo
            bombeloader[slot][1]=bombeloader[slot][1]-1
    print(bombeloader)
    showGameBoard(grille,message)
    return bombeloader

def constatdesmorts(virus):
    for individus in range(0,4):
        if virus[individus]!="mort":
            if grille[virus[individus]]==casevide:
                virus[individus]="mort"
        print (virus)
    return virus

def win(virus):
    victory=0
    nbmort=virus.count("mort")
    if nbmort==4:
        victory=1
        os.system('clear')
        print (iconvictory)
        time.sleep(3)
    return victory

def loose(bombeloader):
    rip=0
    bombezero=0
    for item in bombeloader.keys():
        if bombeloader[item][1]<=0:
            bombezero=bombezero+1

    if bombezero==4:
        rip=1
        os.system('clear')
        print (icondefaite)
        time.sleep(3)
    return rip


def startgame(virus,mouvement,grille,message,bombeloader,ATP):
    initmurs()
    initjoueur()
    virus=initvirus(virus)
    spawnATP()
    showGameBoard(grille,message)
    victory=win(virus)
    rip=loose(bombeloader)

    while victory==0 and rip==0:
        while mouvement[3]==1:
            mouvement,bombeloader=movejoueur(mouvement)
        randommovevirus(virus)
        boom(bombeloader)
        virus=constatdesmorts(virus)
        spawnATP()
        reloadbombe(bombeloader)
        bombemolle(bombeloader)
        victory=win(virus)
        rip=loose(bombeloader)
        mouvement[2]="n"
        mouvement[3]=1



    input('     Appuyer sur entrer pour continuer... ')
    menu()

def menu():
    os.system("clear")
    print (JAUNE+iconbombe+BLANC)
    lore()
    time.sleep(1)
    input(ORANGE+"\n\n    Appuyer sur ENTRER pour continuer..."+BLANC)
    os.system("clear")
    print (JAUNE+iconbombe+BLANC)
    print (VIOLET+iconmenu+BLANC)
    selection = input("\n\n\t\t\t\t\t\t\t\t Choix: ")
    if selection=="1":
        startgame(virus,mouvement,grille,message,bombeloader,ATP)
    if selection=="2":
        instructions()
    if selection=="0":
        sys.exit()
    else:
        menu()

credit()
menu()
