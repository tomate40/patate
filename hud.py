import pygame
import settings

def initHUD():
	global s
	s = pygame.Surface((75,75), pygame.SRCALPHA)
	

def drawHUD(win):
	s.fill((255,255,255,128))
	win.blit(s, (0,0))

	keys = pygame.key.get_pressed()
	if keys[pygame.K_p]:
		openMenu()

def drawHP():
	pass

def drawInv():
	pass

def openMenu():
	pass