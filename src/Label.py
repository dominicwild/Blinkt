import pygame
from Color import Color


class Label():

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        rend = self.font.render(self.text, True, Color.WHITE.value)
        width, height = rend.get_size()
        rect = pygame.Rect(self.x, self.y, width, height)
        rect.center = rect.center

        screen.blit(rend, rect)

    def action(self, event):
        pass

    def setText(self, text):
        self.text = text
