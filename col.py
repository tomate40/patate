import pygame
import time
import Map
import player
import settings
from _thread import *


def initcollision():
    start_new_thread(loop, ())
    pass


def loop():
    global current_collision
    time.sleep(0.1)
    clock = pygame.time.Clock()
    collision_tolerance = 6
    current_collisionHaut = []
    current_collisionBas = []
    current_collisionGauche = []
    current_collisionDroite = []
    while True:
        clock.tick(60)
        for a in range (len(Map.m.rectangles)):
            
            #Check pour collision
            if player.p1.rectangle_player.colliderect(Map.m.rectangles[a]):
                #If collision = Droite
                if abs(Map.m.rectangles[a].left - player.p1.rectangle_player.right) < collision_tolerance:
                    if not Map.m.rectangles[a].y - settings.Ypos in current_collisionDroite:
                        settings.moveRight = False
                        current_collisionDroite.append(Map.m.rectangles[a].y - settings.Ypos)
                
                #If collision = Gauche
                if abs(Map.m.rectangles[a].right - player.p1.rectangle_player.left) < collision_tolerance:
                    if not Map.m.rectangles[a].y - settings.Ypos in current_collisionGauche:
                        settings.moveLeft = False
                        current_collisionGauche.append(Map.m.rectangles[a].y - settings.Ypos)

                #If collision = Haut
                if abs(Map.m.rectangles[a].bottom - player.p1.rectangle_player.top) < collision_tolerance:
                    if not Map.m.rectangles[a].x - settings.Xpos in current_collisionHaut:
                        settings.moveUp = False
                        current_collisionHaut.append(Map.m.rectangles[a].x - settings.Xpos)

                #If collision = bas
                if abs(Map.m.rectangles[a].top - player.p1.rectangle_player.bottom) < collision_tolerance:
                    if not Map.m.rectangles[a].x - settings.Xpos in current_collisionBas:
                        settings.moveDown = False
                        current_collisionBas.append(Map.m.rectangles[a].x - settings.Xpos)
            else:
                #check if collision Droite est encore True
                if Map.m.rectangles[a].y - settings.Ypos in current_collisionDroite:
                    if abs(Map.m.rectangles[a].left - player.p1.rectangle_player.right) < collision_tolerance:
                        settings.moveRight = True
                        current_collisionDroite.remove(Map.m.rectangles[a].y - settings.Ypos)
                        
                #check if collision gauche est encore True
                if Map.m.rectangles[a].y - settings.Ypos in current_collisionGauche:
                    if abs(Map.m.rectangles[a].right - player.p1.rectangle_player.left) < collision_tolerance:
                        settings.moveLeft = True
                        current_collisionGauche.remove(Map.m.rectangles[a].y - settings.Ypos)
                        
                #check if collision haut est encore True
                if Map.m.rectangles[a].x - settings.Xpos in current_collisionHaut:
                    if abs(Map.m.rectangles[a].bottom - player.p1.rectangle_player.top) < collision_tolerance:
                        settings.moveUp = True
                        current_collisionHaut.remove(Map.m.rectangles[a].x - settings.Xpos)
                        
                #Check if collision bas est encore True
                if Map.m.rectangles[a].x - settings.Xpos in current_collisionBas:
                    if abs(Map.m.rectangles[a].top - player.p1.rectangle_player.bottom) < collision_tolerance:
                        settings.moveDown = True
                        current_collisionBas.remove(Map.m.rectangles[a].x - settings.Xpos)
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print('quit')
        player.p1.move()
        Map.m.rectangles.clear()