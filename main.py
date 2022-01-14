import pygame
import time
import settings
import InitMap
import Map
import col
import multiplayer
import player
import player2
from _thread import *

settings.init()

width = 536
height = 266
settings.win = pygame.display.set_mode((width, height))
pygame.display.set_caption('client')
settings.win.fill((255, 255, 255))

InitMap.InitMap()

def redrawWindow(win):
    win.fill((255, 255, 255))
    Map.m.draw(win)
    player.p1.draw(win)
    player2.p2.draw(win)
    pygame.display.update()

def loop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        redrawWindow(settings.win)

def main():
    player.initPlayer1()
    player2.initPlayer2()
    Map.initMap()
    col.initcollision()
    loop()

main()