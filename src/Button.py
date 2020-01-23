import pygame
from ReactiveButton import ReactiveButton

class Button(ReactiveButton):
    screen = None
    rect = None
    # isPressed = False

    def __init__(self, color, leds, screen=None):
        ReactiveButton.__init__(self,color.value)
        self.color = color
        self.leds = leds
        # self.guiColor = color.value
        self.hoverColor = [i * 0.75 for i in color.value]
        self.screen = screen

    def toString(self):
        "Color: " + self.color.name + "\n" + self.leds.toString()

    def setDraw(self, screen, rect):
        self.screen = screen
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, self.guiColor, self.rect)

    def getGUIColor(self):
        return self.guiColor

    def addColor(self, list):
        list.append(self.color)

    def reset(self):
        self.resetGUIColor()
        self.isPressed = False

    def resetGUIColor(self):
        self.guiColor = self.color.value

    # def pressed(self):
    #     self.guiColor = [i * 0.5 for i in self.color.value]  # Darken the colour
    #     self.isPressed = True
    #
    # def hovering(self):
    #     if (not self.isPressed):
    #         self.guiColor = self.hoverColor
