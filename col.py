import pygame
import Map
import player
from _thread import *


def initcollision():
    start_new_thread(loop, ())


def loop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for a in range (len(Map.m.rectangles)):
            if player.p.rectangle_player.colliderect(Map.m.rectangles[a]):
                settings.avancer = False
            else:
                settings.avancer = True

def decide_collidable(Xpos, Ypos, rectangles):
    
