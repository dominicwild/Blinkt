import pygame
from Color import Color
from ReactiveButton import ReactiveButton
from DrawableButton import DrawableButton


class TextButton(DrawableButton):

    def __init__(self, text, x, y, game, padding=50, color=Color.LIGHT_GREY):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.guiColor = color.value
        self.font = pygame.font.Font(None, 40)
        self.padding = padding
        # self.rect = self.createRect()
        DrawableButton.__init__(self, color, game, self.createRect())

    def draw(self, screen):
        rend = self.font.render(self.text, True, Color.BLACK.value)
        width, height = rend.get_size()
        rect = pygame.Rect(0, 0, width, height)
        rect.center = self.rect.center

        DrawableButton.draw(self, screen)
        screen.blit(rend, rect)

    def createRect(self):
        rend = self.font.render(self.text, True, Color.BLACK.value)
        width, height = rend.get_size()
        btnWidth, btnHeight = width + self.padding, height + self.padding
        return pygame.Rect(self.x - btnWidth / 2, self.y - btnHeight / 2, btnWidth, btnHeight)

    def action(self, event):
        DrawableButton.action(self, event)

        if event.type == pygame.MOUSEBUTTONUP:
            if (self.rect.collidepoint(event.pos)):
                self.onClick()

    def onClick(self):
        pass