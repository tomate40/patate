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

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if settings.moveLeft == True:
                settings.Xpos += self.vel

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if settings.moveRight == True:
                settings.Xpos -= self.vel

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if settings.moveUp == True:
                settings.Ypos += self.vel

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if settings.moveDown == True:
                settings.Ypos -= self.vel

def initPlayer1():
    global p1
    pygame.init()
    multiplayer.take_position()
    p1 = Player1((settings.ScreenSize[0] / 2) - (settings.size / 2), (settings.ScreenSize[1] / 2) - (settings.size / 2), settings.size, settings.size, (255, 165, 0))
    start_new_thread(upload, ())


def upload():
    clock = pygame.time.Clock()
    while True:
        clock.tick(settings.FPScap)
        multiplayer.upload()