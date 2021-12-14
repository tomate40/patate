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

clock = pygame.time.Clock()

def redrawWindow(win):
    win.fill((255, 255, 255))
    Map.m.draw(win)
    Map.m.rectangles.clear()
    player.p.draw(win)
    pygame.display.update()

def loop():
    while True:
        clock.tick(60)
        redrawWindow(settings.win)

def main():
    time.sleep(0.2)
    player.initPlayer()
    time.sleep(0.2)
    Map.initMap()
    time.sleep(0.2)
    col.initcollision()
    time.sleep(0.2)
    start_new_thread(loop, ())

main()