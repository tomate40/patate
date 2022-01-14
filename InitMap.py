import pygame
import settings

dejaRect = []
Rectangles = []

Maph=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def buildBords():
    #haut
    Rectangles.append((-1 * settings.size, -1 * settings.size, 22 * settings.size, 1 * settings.size))
    #bas
    Rectangles.append((-1*settings.size, 11*settings.size, 22 * settings.size, 1 * settings.size))
    #gauche
    Rectangles.append((-1 * settings.size, -1 * settings.size, 1 * settings.size, 12 * settings.size))
    #droite
    Rectangles.append((21 * settings.size, -1 * settings.size, 1 * settings.size, 13 * settings.size))


def buildSquares(Liste):
    global WW, HH
    Rectangles.append((Liste[0][1]*50, Liste[0][0]*50, WW * settings.size, HH * settings.size))


def addToListe(height, liste):
    global WW
    adding = liste
    WW = len(liste)
    if height != 0:
        for j in range(height - 1):
            for i in range(WW):
                adding.append((liste[i][0] + (j + 1), liste[i][1]))
    return adding


def height(Y, X):
    global HH, WW
    P = 0
    run = True
    while run:
        if Y + P <= 20 and X != 0:
            if Maph[Y + P][X - 1] != 1:
                run = False
            else:
                P += 1
        else:
            run = False
    HH = P
    return P


def InitMap():
    global rectToDraw, HH, WW
    rectToDraw = []
    liste = []
    Xline = 0
    Yline = 0
    line = []
    buildBords()
    for i in range(len(Maph)):
        for j in range(len(Maph[i])):
            line = Maph[Yline]
            if line[Xline] == 1 and len(liste) != 0 and (Yline, Xline) not in dejaRect:
                liste.append((Yline, Xline))

            elif line[Xline] == 1 and len(liste) == 0 and (Yline, Xline) not in dejaRect:
                liste = [(Yline, Xline)]

            elif line[Xline] == 0 and len(liste) != 0 and (Yline, Xline) not in dejaRect:

                chose = height(Yline, Xline)
                liste = addToListe(chose, liste)
                buildSquares(liste)

                rectToDraw.extend(liste)
                dejaRect.extend(liste)

                HH = 0
                WW = 0
                liste.clear()

            Xline += 1

        Yline += 1
        Xline = 0