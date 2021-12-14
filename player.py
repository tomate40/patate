import pygame
import settings
import col
import time
#import main
#import multiplayer
import Map
from _thread import *


class Player():
    def __init__(self, x, y, width, height, color):
        self.width = width
        self.height = height
        self.rectangle_player = pygame.Rect(268-25, 133-25, width, height)
        self.color = color
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rectangle_player)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            settings.Xpos += self.vel

        if keys[pygame.K_RIGHT]:
            settings.Xpos -= self.vel

        if keys[pygame.K_UP]:
            settings.Ypos += self.vel

        if keys[pygame.K_DOWN]:
            settings.Ypos -= self.vel
    
    def collision(self):
        #for a in range (len(Map.m.rectangles)):
            #if self.rectangle_player.colliderect(Map.m.rectangles[a]):
                #print('heeleafeawfewawfeaewf')     
        pass           

def initPlayer():
    global p
    pygame.init()
    p = Player(268-25, 133-25, 50, 50, (255, 165, 0))
    start_new_thread(loop, ())


def loop():
    global p
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                print('quit')
        p.move()
        p.collision()