import pygame
import time
import settings
import Map
import col
#import multiplayer
import player
from _thread import *

settings.init()

width = 536
height = 266
settings.win = pygame.display.set_mode((width, height))
pygame.display.set_caption('client')
settings.win.fill((255, 255, 255))

def redrawWindow(win):
    win.fill((255, 255, 255))
    Map.m.draw(win)
    player.p.draw(win)
    pygame.display.update()

def loop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        redrawWindow(settings.win)

def main():
    player.initPlayer()
    Map.initMap()
    col.initcollision()
    start_new_thread(loop, ())

main()