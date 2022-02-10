def init():
	global Xpos, Ypos, Xpos2, Ypos2, PlayerID, win,	moveUp, moveDown, moveLeft, moveRight, size, ScreenSize, GunP1, striking, showGunP1, FPScap, hpP1, hpP2, GUIscale, currentWapon, mode
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