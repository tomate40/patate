import settings
import pygame
from _thread import *


class Map():
    def __init__(self, x, y, Width, Height):
        self.x = settings.Xpos
        self.y = settings.Ypos
        self.width = Width
        self.height = Height
        self.color = (255, 0, 255)
        self.rectangles = []
        self.rectangle_present = str()

    def draw(self, win):
        global Maph
        mapX = 1
        mapY = 1
        for i in range(0, 200):
          loc = Maph[(((mapY*20) - 20) + mapX) - 1]
          if loc == 1:
              self.rectangle_present = pygame.Rect((settings.Xpos - 257) + (mapX*self.width),(settings.Ypos - 243) + (mapY*self.height), self.width, self.height)
              pygame.draw.rect(settings.win, self.color, self.rectangle_present)
              self.rectangles.append(self.rectangle_present)
              self.rectangle_present = str()
          if mapX == 20:
              mapY += 1
              mapX = 1
          else:
              mapX += 1
          i += 1

def initMap():
    global m, Maph
    Maph=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
          1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
          1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
          1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
          1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,
          1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,
          1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
          1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,
          1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    m = Map(settings.Xpos, settings.Ypos, 50, 50)

#rectToDraw = []
#run = True
#checkID = 1 
#liste = []
#Xline = 1
#Yline = 1
#while run:
 #   if checkID - 1 == liste[checkID - 1]:
  #      if Maph[checkID] == 1:
   #         liste.append(checkID)
    #        Xline + 1
      #  elif checkLine == False:
     #       checkID += 19 - len(liste)
       #     checkLine = True
        #    Yline + 1
        #else:
         #   rectToDraw.append((liste, Yline*50, 50, 50))

    #checkID += 1
    #print(rectToDraw)