
import Map
import player
from _thread import *


def initcollision():
    start_new_thread(loop, ())


def loop():
    clock = pygame.time.Clock()
    while True:
        for a in range(0, 200):
            if player.p.rectangle_player.colliderect(Map.m.rectangles[a]):
                print('heeleafeawfewawfeaewf')
