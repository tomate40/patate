import pygame
import time
import settings
import InitMap
import gun
import Map
import col
import multiplayer
import player
import player2
import attaque
from _thread import *

settings.init()

settings.ScreenSize = (536, 266)
settings.win = pygame.display.set_mode(settings.ScreenSize)
pygame.display.set_caption('client')
settings.win.fill((255, 255, 255))

InitMap.InitMap()

def redrawWindow(win):
	global iii
	win.fill((255, 255, 255))
	Map.m.draw(win)
	player.p1.draw(win)
	player2.p2.draw(win)
	gun.findAngle()
	pygame.display.update()

def loop():
	clock = pygame.time.Clock()
	while True:
		clock.tick(60)
		redrawWindow(settings.win)

def main():
	multiplayer.initMultiplayer()
	player.initPlayer1()
	player2.initPlayer2()
	Map.initMap()
	col.initcollision()
	attaque.initAttaque()
	gun.initSwordP1()
	loop()
main()