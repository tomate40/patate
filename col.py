import pygame
import Map
import player
import settings
from _thread import *


def initcollision():
    start_new_thread(loop, ())


def loop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for a in range (len(Map.m.rectangles)):
            if player.p.rectangle_player.colliderect(Map.m.rectangles[a]):
                settings.moveUp = True
            else:
                settings.moveUp = True
        
        Map.m.rectangles.clear()

def decide_collidable(Xpos, Ypos, rectangles):
    posInMap = 2


    #for i in range (len(Map.m.rectangles)):
        #check = Map.m.rectangles[i]
        #if check.x - 100 < Xpos or check.x + 100 > Xpos and check.y - 100 < Ypos or check.y +100 > Ypos:
            #collidable = 