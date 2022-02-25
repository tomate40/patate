import pygame
import settings

from _thread import *


class UI():
	def __init__(self):
		self.Ppressed = False
		self.offsetX = 7
		self.offsetY = 37
		self.defaultSize = 60
		self.grandSize = 75
		self.inv1Size = self.grandSize
		self.inv2Size = self.defaultSize
		self.Inv1 = {
			'Size': self.inv1Size,
			'PosX': 
					(settings.ScreenSize[0] / 2) - 
					(self.inv1Size + self.offsetX),
			'PosY':
          settings.ScreenSize[1] - 
					((self.inv1Size / 2) + self.offsetY),
			'Color': (150, 150, 150, 200)
		}
		self.Inv2 = {
			'Size': self.inv2Size,
			'PosX': 
					(settings.ScreenSize[0] / 2) + self.offsetX,
			'PosY':
          settings.ScreenSize[1] - 
					((self.inv2Size / 2) + self.offsetY),
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
				'PosX':
          	(settings.ScreenSize[0] / 2) - 
						(self.inv1Size + self.offsetX),
				'PosY':
          	settings.ScreenSize[1] - 
						((self.inv1Size / 2) + self.offsetY),
				'Color': (150, 150, 150, 200)
			}
			self.Inv2 = {
				'Size': self.inv2Size,
				'PosX': 
						(settings.ScreenSize[0] / 2) + self.offsetX,
				'PosY':
            settings.ScreenSize[1] - 
						((self.inv2Size / 2) + self.offsetY),
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
				Hud.OpenMenu()
				self.Ppressed = True

			if settings.mode == "MENU" and not self.Ppressed:
				settings.mode = "PLAY"
				self.Ppressed = True

		if not keys[pygame.K_p] and self.Ppressed == True:
			self.Ppressed = False

		if keys[pygame.K_1] and settings.mode == "PLAY":
			self.WaponChange('GUN')

		if keys[pygame.K_2] and settings.mode == "PLAY":
			self.WaponChange('je')

	def DrawWaponsInv(self):
		settings.win.blit(self.GunImage, (100, 100))

	def DrawInv(self):
		self.AAfilledRoundedRect(
			settings.win,
			(self.Inv1['Size'], self.Inv1['Size'], 
			 self.Inv1['Size'], self.Inv1['Size']),
			self.Inv1['Color'], 
			(self.Inv1['PosX'], 
			self.Inv1['PosY']), 
		0.5)

		self.AAfilledRoundedRect(
					settings.win,
					(self.Inv2['Size'], self.Inv2['Size'],
					 self.Inv2['Size'], self.Inv2['Size']),
					self.Inv2['Color'],
					(self.Inv2['PosX'], self.Inv2['PosY']), 
					0.5)

	def AAfilledRoundedRect(self, surface, rect, color, pos, radius=0.4):
		rect = pygame.Rect(rect)
		color = pygame.Color(*color)
		alpha = color.a
		color.a = 0
		rect.topleft = 0, 0
		rectangle = pygame.Surface(
			rect.size, pygame.SRCALPHA)

		circle = pygame.Surface(
			[min(rect.size) * 3] * 2, pygame.SRCALPHA)
		pygame.draw.ellipse(
			circle, (0, 0, 0), circle.get_rect(), 0)
		circle = pygame.transform.smoothscale(
			circle, [int(min(rect.size) * radius)] * 2)

		radius = rectangle.blit(circle, (0, 0))
		radius.bottomright = rect.bottomright
		rectangle.blit(circle, radius)
		radius.topright = rect.topright
		rectangle.blit(circle, radius)
		radius.bottomleft = rect.bottomleft
		rectangle.blit(circle, radius)

		rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
		rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

		rectangle.fill(color,
									 special_flags=pygame.BLEND_RGBA_MAX)
		rectangle.fill((255, 255, 255, alpha),
                    special_flags=pygame.BLEND_RGBA_MIN)

		return surface.blit(rectangle, pos)


class HUD():
	def __init__(self):
		self.currentTab = "Graphics"
		self.buttonslist = []
		self.methodlist = []

	def OpenMenu(self):
		settings.mode = "MENU"
		self.DrawMenu()

	def DrawMenu(self):
		pygame.draw.rect(settings.win, (0, 0, 255),
										 (0, 0, settings.ScreenSize[0] / 3,
											settings.ScreenSize[1]))
		foggyThing = pygame.Surface(
			((settings.ScreenSize[0] / 3) * 2,
			 settings.ScreenSize[1]),
			pygame.SRCALPHA)

		color = (155, 155, 155, 150)

		color = pygame.Color(*color)
		alpha = color.a
		color.a = 150

		foggyThing.fill(color,
										special_flags=pygame.BLEND_RGBA_MAX)
		foggyThing.fill((255, 255, 255, alpha),
										special_flags=pygame.BLEND_RGBA_MIN)

		settings.win.blit(foggyThing, 
											(settings.ScreenSize[0] / 3, 0))

	def OpenSettings(self):
		settings.mode = "SETTINGS"

		self.SettingsButtons = {
			"Graphics": {
				"ScreenSize": {
					"Number1": {
						"Title": "Screen Size (X)",
						"Content": 
						settings.settings["ScreenSize"]["X"],
						"Infos": {
							"Method": "Slider",
              "Start": 300,
              "End": 2000
                        }
                    },
                    "Number2": {
                        "Title": "Screen Size (Y)",
                        "Content": settings.settings["ScreenSize"]["Y"],
                        "Infos": {
                            "Method": "Slider",
                            "Start": 100,
                            "End": 1000
                        }
                    }
                },
                "FPScap": {
                    "Number1": {
                        "Title": "FPS Cap",
                        "Content": settings.settings['FPScap'],
                        "Infos": {
                            "Method": "Options",
                            "Options": [30, 60, 120]
                        }
                    }
                },
                "GUIscale": {
                    "Number1": {
                        "Title": "GUI Scale",
                        "Content": settings.settings["GUIscale"],
                        "Infos": {
                            "Method": "Slider",
                            "Start": 50,
                            "End": 150
                        }
                    }
                }
            },
            "Controls": {
                "MouvementKeys": {
                    "Number1": {
                        "Title":
                        "Forward",
                        "Content":
                        settings.settings["MouvementKeysDisplay"]["Forward"],
                        "Info": {
                            "Method": "KeyInput"
                        }
                    },
                    "Number2": {
                        "Title":
                        "Backward",
                        "Content":
                        settings.settings["MouvementKeysDisplay"]["Back"],
                        "Info": {
                            "Method": "KeyInput"
                        }
                    },
                    "Number3": {
                        "Title":
                        "Right",
                        "Content":
                        settings.settings["MouvementKeysDisplay"]["Right"],
                        "Info": {
                            "Method": "KeyInput"
                        }
                    },
                    "Number4": {
                        "Title":
                        "Left",
                        "Content":
                        settings.settings["MouvementKeysDisplay"]["Left"],
                        "Info": {
                            "Method": "KeyInput"
                        }
                    }
                }
            },
            "TabsOrder": ["Graphics", "Controls"],
            "GraphicsOrder": ["ScreenSize", "FPScap", "GUIscale"],
            "ControlsOrder": ["MouvementKeys"]
        }

		self.DrawSettings()

	def DrawSettings(self):
		global buttonsInSettings
        #pygame.draw.rect(settings.win, (0, 0, 255), (0, 0, settings.ScreenSize[0], settings.ScreenSize[1]))
		ButtonY = 100
		orderid = 0
		for Tab in self.SettingsButtons['TabsOrder']:
			buttonsInSettings.append(
				SettingsButtonsDrawer(Tab,
			((settings.ScreenSize[0] / 2) - 10, 55),
			((orderid * (settings.ScreenSize[0] / 2)) + 5, 5),
      (0, 155, 250)))
			orderid += 1

		for sets in self.SettingsButtons[self.currentTab]:
			
			for NumberNum in self.SettingsButtons[
			self.currentTab][sets]:
				
				for ButtonsSettings in self.SettingsButtons[
				self.currentTab][sets][NumberNum]:

					if ButtonsSettings == "Title":
						self.CurrentTitle = self.SettingsButtons[
						self.currentTab][sets][NumberNum]
						[ButtonsSettings]

					if ButtonsSettings == "Content":
						self.CurrentContent = self.SettingsButtons[
						self.currentTab][sets][NumberNum]
						[ButtonsSettings]
							
						if ButtonsSettings == "Info":
							
							self.methodlist.append((
								self.SettingsButtons[Tab][sets][
								NumberNum][ButtonsSettings]["Info"]
							))

				#quand bouton fini --> ajouter a la liste
				buttonsInSettings.append(
					SettingsButtonsDrawer(self.CurrentTitle, 
					(200, 25),(20, ButtonY), (0, 155, 250)))
							
				ButtonY += 35
			ButtonY += 10

	def drawSettingsButtons(self):
		for button in buttonsInSettings:
			print(button.text)
			button.DrawRect()


class Methods():
	def __init__(self, infos):
		self.infos = infos

		self.initmethod()

	def initmethod(self):
		if self.infos["Method"] == "Slider":
			self.Slider(self.infos["Start"],self.infos["End"])
	
	def Slider(self, start, end):
		pass

	def Options(self):
		pass

	def KeyInput(self):
		pass


class SettingsButtonsDrawer:
    def __init__(self,
                 text,
                 rectsize,
                 rectpos,
                 rectcolor,
                 reactiontype=None,
                 reactiondata=None,
                 textsize=25,
                 textcolor=(0, 0, 0),
                 textfont=None):
        self.text = text
        self.rectsize = rectsize
        self.rectpos = rectpos
        self.rectcolor = rectcolor
        self.reactiontype = reactiontype
        self.textsize = textsize
        self.textcolor = textcolor
        self.textfont = textfont

    def DrawRect(self):
        rect = pygame.Rect(self.rectpos[0], self.rectpos[1], self.rectsize[0], self.rectsize[1])
        chose = pygame.draw.rect(settings.win, self.rectcolor, (rect))
        text_object = pygame.font.SysFont( self.textfont, self.textsize).render(self.text, True, self.textcolor)
        text_rect = text_object.get_rect(center=chose.center)

        settings.win.blit(text_object, text_rect)
        self.checkForClick(text_rect)
        return text_rect

    def checkForClick(self, rect):
        mousepos = pygame.mouse.get_pos()
        if self.reactiontype != None:
            if rect.collidepoint(mousepos):
                if self.reactiontype == "Bigger":
                    pass


buttons = []


class Button:
    def __init__(self, text, width, height, pos, elevation, chose):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.gui_font = pygame.font.Font(None, 30)

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        #text
        self.text = text
        self.text_surf = self.gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)
        self.chose = chose

    def change_text(self, newtext):
        self.text_surf = self.gui_font.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, b):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(settings.win,
                         self.bottom_color,
                         self.bottom_rect,
                         border_radius=12)
        pygame.draw.rect(settings.win,
                         self.top_color,
                         self.top_rect,
                         border_radius=12)
        settings.win.blit(self.text_surf, self.text_rect)
        self.check_click(b)

    def check_click(self, b):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    if b == buttonToSettings:
                        print("clicked button1")
                        self.chose.OpenSettings()
                    print('click')
                    self.pressed = False
                    self.change_text(self.text)
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'


def buttons_draw():
    for b in buttons:
        b.draw(b)


def initHUD():
    global inv1, gui, Hud, gui_font, Button, buttonToSettings, buttonToJoinParty, buttonToCreateParty, buttonsInSettings
    gui = UI()
    Hud = HUD()
    buttonToSettings = Button('Settings', 150, 30, (14, 20), 5, Hud)
    buttonToJoinParty = Button('Join Party', 150, 30, (14, 70), 5, Hud)
    buttonToCreateParty = Button('Create Party', 150, 30, (14, 120), 5, Hud)
    buttonsInSettings = []