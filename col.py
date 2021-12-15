import pygame
import time
import Map
import player
import settings
from _thread import *


def initcollision():
    start_new_thread(loop, ())


def loop():
    global current_collision
    time.sleep(0.1)
    clock = pygame.time.Clock()
    collision_tolerance = 10
    current_collision = []
    while True:
        clock.tick(60)
        for a in range (len(Map.m.rectangles)):
            if Map.m.rectangles[a] in current_collision:
                if not abs(Map.m.rectangles.bottom - player.p.rectangle_player.top) < collision_tolerance:
                    settings.moveUp = True
                    current_collision.remove(Map.m.rectangles[a])
            if player.p.rectangle_player.colliderect(Map.m.rectangles[a]):
                if abs(Map.m.rectangles[a].bottom - player.p.rectangle_player.top) < collision_tolerance:
                    print('top collision')
                    settings.moveUp = False
                    if not Map.m.rectangles[a] in current_collision:
                        print('ajouté a current_collision')
                        #start_new_thread(loopUp, (Map.m.rectangles[a], collision_tolerance, ))
                        current_collision.append(Map.m.rectangles[a])
                if abs(Map.m.rectangles[a].top - player.p.rectangle_player.bottom) < collision_tolerance:
                    print('bottom collision')
        Map.m.rectangles.clear()

def loopUp(rectangle, tol):
        clock.tick(20)
        print('healfaewfoijawoiefjaweoijfjoaweijoifewajifewa;ijafwejio;')
        

        
 