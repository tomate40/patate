import pygame
import gun
import multiplayer
from _thread import *

def initAttaque():
	start_new_thread(loop, ())

def loop():
	clock = pygame.time.Clock()
	while True:
		clock.tick(60)
		buttons = pygame.mouse.get_pressed()
		if buttons[0]:
			gun.shot()