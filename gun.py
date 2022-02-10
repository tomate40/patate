import pygame
import time
import math
import settings
from _thread import *

def shot():
	global angle
	if settings.striking == False:
		settings.striking = True
		angle = 0

def DrawGun():
	if settings.currentWapon == "GUN":
		findAngle()

def findAngle():
	mousePos = pygame.mouse.get_pos()

	vector2Y = mousePos[1] - (settings.ScreenSize[1]/2)
	vector2X = mousePos[0] - (settings.ScreenSize[0]/2)

	vector1X = settings.ScreenSize[0]/2
	vector1Y = settings.ScreenSize[1]/2

	v1_theta = math.atan2(vector1Y, vector1X)
	v2_theta = math.atan2(vector2Y, vector2X)

	r = (v1_theta - v2_theta) * (180.0 / math.pi)

	r += 425


	image_rect = settings.GunP1.get_rect(midtop = (settings.ScreenSize[0]/2, settings.ScreenSize[1]/2))
	offset_center_to_pivot = pygame.math.Vector2(settings.ScreenSize[0]/2, settings.ScreenSize[1]/2) - image_rect.center

	rotated_offset = offset_center_to_pivot.rotate(-abs(r))

	rotated_image_center = (settings.ScreenSize[0]/2 - rotated_offset.x, settings.ScreenSize[1]/2 - rotated_offset.y)

	rotated_image = pygame.transform.rotate(settings.GunP1, r)
	rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

	settings.win.blit(rotated_image, rotated_image_rect)

	buttons = pygame.mouse.get_pressed()
	if buttons[0]:
		shot()

def initGunP1():
	settings.GunP1 = pygame.Surface((25, 50))
	settings.GunP1.set_colorkey("black")
	settings.GunP1.fill((144, 172, 233))