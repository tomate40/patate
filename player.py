import pygame
import settings
import col
import time
import Map
from _thread import *


class Player1():
    def __init__(self, x, y, width, height, color):
        self.width = width
        self.height = height
        self.rectangle_player = pygame.Rect(300-25, 200-25, width, height)
        self.color = color
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rectangle_player)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if settings.moveLeft == True:
                settings.Xpos += self.vel

        if keys[pygame.K_RIGHT]:
            if settings.moveRight == True:
                settings.Xpos -= self.vel

        if keys[pygame.K_UP]:
            if settings.moveUp == True:
                settings.Ypos += self.vel

        if keys[pygame.K_DOWN]:
            if settings.moveDown == True:
                settings.Ypos -= self.vel         

def initPlayer1():
    global p1
    pygame.init()
    p1 = Player1(268-25, 133-25, 50, 50, (255, 165, 0))
    start_new_thread(loop, ())


def loop():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                print('quit')
        