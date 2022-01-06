import pygame
import settings
import multiplayer
import Map
from _thread import *


class Player1():
    def __init__(self, x, y, width, height, color):
        self.width = width
        self.height = height
        self.rectangle_player = pygame.Rect(x, y, width, height)
        self.color = color
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rectangle_player)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if settings.moveLeft == True:
                settings.Xpos += self.vel
                start_new_thread(upload, ())

        if keys[pygame.K_RIGHT]:
            if settings.moveRight == True:
                settings.Xpos -= self.vel
                start_new_thread(upload, ())

        if keys[pygame.K_UP]:
            if settings.moveUp == True:
                settings.Ypos += self.vel
                start_new_thread(upload, ())

        if keys[pygame.K_DOWN]:
            if settings.moveDown == True:
                settings.Ypos -= self.vel  
                start_new_thread(upload, ())       

def initPlayer1():
    global p1
    pygame.init()
    multiplayer.take_position()
    p1 = Player1(268-25, 133-25, 50, 50, (255, 165, 0))


def upload():
    multiplayer.upload()