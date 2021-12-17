import pygame, time
import settings
import multiplayer
from _thread import *

class Player2():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rectangle_player2 = pygame.Rect(settings.Xpos2-25, settings.Ypos2-25, width, height)
    
    def draw(self, win):
        self.rectangle_player2 = (settings.Xpos - settings.Xpos2, settings.Ypos - settings.Ypos2, self.width, self.height)
        pygame.draw.rect(win, self.color, self.rectangle_player2)

def initPlayer2():
    global p2
    p2 = Player2(settings.Xpos2, settings.Ypos2, 50, 50,(255, 0, 0))
    time.sleep(2)
    start_new_thread(loop, ())

def loop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        multiplayer.download()