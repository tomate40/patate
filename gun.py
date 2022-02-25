import pygame
import time
import math
import settings
from _thread import *

class GunP():
	def __init__(self):
		self.GunP1 = pygame.Surface((25, 50))
		self.GunP1.set_colorkey("black")
		self.GunP1.fill((144, 172, 233))

	def findAngle(self):
		mousePos = pygame.mouse.get_pos()

		vector2Y = mousePos[1] - (settings.ScreenSize[1]/2)
		vector2X = mousePos[0] - (settings.ScreenSize[0]/2)

		vector1X = settings.ScreenSize[0]/2
		vector1Y = settings.ScreenSize[1]/2

		v1_theta = math.atan2(vector1Y, vector1X)
		v2_theta = math.atan2(vector2Y, vector2X)

		r = (v1_theta - v2_theta) * (180.0 / math.pi)
		r += 425

		image_rect = self.GunP1.get_rect(
			midtop = (settings.ScreenSize[0]/2, 
								settings.ScreenSize[1]/2))
		offset_center_to_pivot = pygame.math.Vector2(
			settings.ScreenSize[0]/2, 
			settings.ScreenSize[1]/2) - image_rect.center

		rotated_offset = offset_center_to_pivot.rotate(-abs(r))

		rotated_image_center = (settings.ScreenSize[0]/2 - rotated_offset.x, settings.ScreenSize[1]/2 - rotated_offset.y)

		rotated_image = pygame.transform.rotate(self.GunP1, r)
		rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

		settings.win.blit(rotated_image, rotated_image_rect)

		buttons = pygame.mouse.get_pressed()
		if buttons[0]:
			self.shot()

	def shot(self):
		global angle
		if settings.striking == False:
			settings.striking = True
			angle = 0

class Gun():
	def __init__(self):
		self.Gun = pygame.Surface((25, 50))
		self.Gun.set_colorkey("black")
		self.Gun.fill((144, 172, 233))

	def findAngle(self):

		r = settings.P2angle
		r += 425

		image_rect = self.Gun.get_rect(
			midtop = (settings.ScreenSize[0]/2, 
								settings.ScreenSize[1]/2))
		offset_center_to_pivot = pygame.math.Vector2(
			settings.ScreenSize[0]/2, 
			settings.ScreenSize[1]/2) - image_rect.center

		rotated_offset = offset_center_to_pivot.rotate(
			-abs(r))

		rotated_image_center = (settings.ScreenSize[0]/2 - 
														rotated_offset.x, 
														settings.ScreenSize[1]/2 - 
														rotated_offset.y)

		rotated_image = pygame.transform.rotate(self.Gun, r)
		rotated_image_rect = rotated_image.get_rect(
			center = rotated_image_center)

		settings.win.blit(rotated_image, rotated_image_rect)


def DrawGun():
	if settings.currentWapon == "GUN":
		GunP1.findAngle()

	for gun in Gunslist:
		pass
		

def initGunP1():
	global GunP1, Gunslist
	Gunslist = []
	GunP1 = GunP()
	Gun2 = GunP()
	Gunslist.append(Gun2)