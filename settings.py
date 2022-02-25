import pygame

def init():
	global Xpos, Ypos, Xpos2, Ypos2, PlayerID, win,	moveUp, moveDown, moveLeft, moveRight, size, ScreenSize, GunP1, striking, showGunP1, FPScap, hpP1, hpP2, GUIscale, currentWapon, mode, settings, scroll, getTicksLastFrame, P2angle
	size = 50
	Xpos = 130
	Ypos = 70
	Xpos2 = int()
	Ypos2 = int()
	hpP1 = int()
	hpP2 = int()
	PlayerID = int()
	win = 'je vais te m_ng_r'
	moveUp = True
	moveDown = True
	moveLeft = True
	moveRight = True
	ScreenSize = 40923
	GunP1 = 8
	striking = False
	showGunP1 = False
	FPScap = 60
	GUIscale = 100
	currentWapon = "GUN"
	mode = "PLAY"
	scroll = 0
	getTicksLastFrame = 0
	P2angle = 0

	settings = {
		"FPScap": 600,
		"GUIscale": 100,
		"ScreenSize": {
			"X": 536, 
			"Y": 266
		},
		"MouvementKeys": {
			"Forward": pygame.K_UP,
			"Back": pygame.K_DOWN,
			"Right": pygame.K_RIGHT,
			"Left": pygame.K_LEFT
		},
		"MouvementKeysDisplay": {
			"Forward": "Arrow UP",
			"Back": "Arrow Down",
			"Right": "Arrow Right",
			"Left": "Arrow Left"
		}
	}