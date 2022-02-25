import settings
import pygame
import InitMap

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
        for i in range(len(InitMap.Rectangles)):
            self.rectangle_present = pygame.Rect((settings.Xpos + 257) + InitMap.Rectangles[i][0], (settings.Ypos + 243) + InitMap.Rectangles[i][1], InitMap.Rectangles[i][2], InitMap.Rectangles[i][3])
            pygame.draw.rect(settings.win, self.color, self.rectangle_present)
            self.rectangles.append(self.rectangle_present)

def initMap():
    global m
    m = Map(settings.Xpos, settings.Ypos, 50, 50)