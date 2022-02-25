import pygame
import settings
import InitMap
import gun
import Map
import hud
import col
import multiplayer
import player
import player2
from _thread import *

settings.init()

settings.ScreenSize = (536, 266)
settings.win = pygame.display.set_mode(settings.ScreenSize)
pygame.display.set_caption('client')
settings.win.fill((255, 255, 255))

InitMap.InitMap()

def PlayWindow(win):
	win.fill((255, 255, 255))
	if settings.mode == "PLAY" or "MENU":
		gun.DrawGun()
		Map.m.draw(win)
		player.p1.draw(win)
		player2.p2.draw(win)
		hud.gui.DrawUI()
	if settings.mode == "MENU":
		hud.Hud.DrawMenu()
		hud.buttons_draw()

def SettingsWindow(win):
	win.fill((0, 0, 250))
	#hud.Hud.DrawSettings()
	hud.Hud.drawSettingsButtons()

def loop():
	clock = pygame.time.Clock()
	while True:

		if settings.mode == "PLAY" or "MENU":
			clock.tick(settings.FPScap)
			PlayWindow(settings.win)

		if settings.mode == "SETTINGS":
			clock.tick(settings.FPScap/2)
			SettingsWindow(settings.win)
			if pygame.key.get_pressed()[pygame.K_o]:
				settings.mode = "PLAY"
		
		pygame.display.update()

def checkforevents():
	clock = pygame.time.Clock()
	while True:
			clock.tick(settings.FPScap/2)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.MOUSEWHEEL:
					settings.scroll = event.y

def main():
	global getTicksLastFrame
	multiplayer.initMultiplayer()
	player.initPlayer1()
	player2.initPlayer2()
	Map.initMap()
	col.initcollision()
	gun.initGunP1()
	hud.initHUD()
	getTicksLastFrame = 0
	start_new_thread(checkforevents,())
	loop()

if __name__ == "__main__":
	main()