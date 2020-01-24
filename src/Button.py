import pygame
from ReactiveButton import ReactiveButton
from DrawableButton import DrawableButton


class Button(DrawableButton):
    screen = None
    rect = None

    # isPressed = False

    def __init__(self, color, leds, game):
        DrawableButton.__init__(self, color, game)
        self.color = color
        self.leds = leds
        # self.guiColor = color.value
        self.hoverColor = [i * 0.75 for i in color.value]

    def toString(self):
        "Color: " + self.color.name + "\n" + self.leds.toString()

    def setDraw(self, screen, rect):
        self.screen = screen
        self.rect = rect

    def addColor(self, list):
        list.append(self.color)

    def action(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = event.pos  # gets mouse position

            if self.rect.collidepoint(mousePos):
                print("Button released: " + self.color.name)
                if (self.game.getPressedButton() and self.game.getPressedButton() == self):
                    self.addColor(self.game.getGuess())
                    print(self.game.getGuess())

        DrawableButton.action(self, event)
