import pygame
import settings

from _thread import *

class UI():
	def __init__(self):
		self.GunImage = pygame.image.load('GUN.jpg')
		self.Ppressed = False
		self.offsetX = 7
		self.offsetY = 37
		self.defaultSize = 60
		self.grandSize = 75
		self.inv1Size = self.grandSize
		self.inv2Size = self.defaultSize
		self.Inv1 = {
			'Size': self.inv1Size,
			'PosX': (settings.ScreenSize[0] / 2) - (self.inv1Size + self.offsetX),
			'PosY': settings.ScreenSize[1] - ((self.inv1Size/2) + self.offsetY),
			'Color': (150, 150, 150, 200)
		}
		self.Inv2 = {
			'Size': self.inv2Size,
			'PosX': (settings.ScreenSize[0] / 2) + self.offsetX,
			'PosY': settings.ScreenSize[1] - ((self.inv2Size/2) + self.offsetY),
			'Color': (150, 150, 150, 200)
		}
	
	def ChangeValues(self, size, id):
		if id == 1:
			self.inv1Size = size
			self.inv2Size = self.defaultSize
		elif id == 2:
			self.inv2Size = size
			self.inv1Size = self.defaultSize

		self.Inv1 = {
			'Size': self.inv1Size,
			'PosX': (settings.ScreenSize[0] / 2) - (self.inv1Size + self.offsetX),
			'PosY': settings.ScreenSize[1] - ((self.inv1Size/2) + self.offsetY),
			'Color': (150, 150, 150, 200)
		}
		self.Inv2 = {
			'Size': self.inv2Size,
			'PosX': (settings.ScreenSize[0] / 2) + self.offsetX,
			'PosY': settings.ScreenSize[1] - ((self.inv2Size/2) + self.offsetY),
			'Color': (150, 150, 150, 200)
		}

	def WaponChange(self, wapon):
		if wapon == 'GUN':
			self.ChangeValues(self.grandSize, 1)
			settings.currentWapon = "GUN"
		
		if wapon == 'je':
			self.ChangeValues(self.grandSize, 2)
			settings.currentWapon = "je"

	def DrawUI(self):
		self.DrawInv()
		#self.DrawWaponsInv()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_p]:
			if settings.mode == "PLAY" and not self.Ppressed:
				hud.OpenMenu()
				self.Ppressed = True

			if settings.mode == "MENU" and not self.Ppressed:
				settings.mode = "PLAY"
				self.Ppressed = True
			
		if not keys[pygame.K_p] and self.Ppressed == True:
			self.Ppressed = False
		
		if keys[pygame.K_1]:
			self.WaponChange('GUN')
		
		if keys[pygame.K_2]:
			self.WaponChange('je')

	def DrawWaponsInv(self):
		settings.win.blit(self.GunImage, (100,100))

	def DrawInv(self):
		self.AAfilledRoundedRect(settings.win,(self.Inv1['Size'], self.Inv1['Size'], self.Inv1['Size'], self.Inv1['Size']),self.Inv1['Color'], (self.Inv1['PosX'], self.Inv1['PosY']), 0.5)
		self.AAfilledRoundedRect(settings.win,(self.Inv2['Size'], self.Inv2['Size'], self.Inv2['Size'], self.Inv2['Size']),self.Inv2['Color'], (self.Inv2['PosX'], self.Inv2['PosY']), 0.5)

	def AAfilledRoundedRect(self, surface, rect, color, pos, radius=0.4):
		rect = pygame.Rect(rect)
		color = pygame.Color(*color)
		alpha = color.a
		color.a = 0
		rect.topleft = 0,0
		rectangle = pygame.Surface(rect.size, pygame.SRCALPHA)

		circle = pygame.Surface([min(rect.size)*3]*2, pygame.SRCALPHA)
		pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
		circle = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

		radius = rectangle.blit(circle,(0,0))
		radius.bottomright = rect.bottomright
		rectangle.blit(circle,radius)
		radius.topright = rect.topright
		rectangle.blit(circle,radius)
		radius.bottomleft = rect.bottomleft
		rectangle.blit(circle,radius)

		rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
		rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

		rectangle.fill(color,special_flags = pygame.BLEND_RGBA_MAX)
		rectangle.fill((255,255,255,alpha),special_flags = pygame.BLEND_RGBA_MIN)

		return surface.blit(rectangle, pos)

class HUD():
	def __init__(self):
		pass
	
	def OpenMenu(self):
		settings.mode = "MENU"
		self.DrawMenu()
	
	def DrawMenu(self):
		pygame.draw.rect(settings.win, (0, 0, 255), (0, 0, settings.ScreenSize[0]/3.5, settings.ScreenSize[1]))

def initHUD():
	global inv1, gui, hud
	gui = UI()
	hud = HUD()