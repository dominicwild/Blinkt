import pygame
from Color import Color


class TextButton():

    def __init__(self, screen, text, x, y, padding=50,bg=[217, 207, 206]):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.bg = bg
        self.font = pygame.font.Font(None, 40)
        self.padding = padding

    def draw(self):
        rend = self.font.render(self.text, True, Color.BLACK.value)
        width, height = rend.get_size()
        btnWidth, btnHeight = width + self.padding, height + self.padding
        self.rect = pygame.Rect(self.x - btnWidth/2, self.y - btnHeight/2, btnWidth, btnHeight)
        rect = pygame.Rect(0, 0, width, height)
        rect.center = self.rect.center


        pygame.draw.rect(self.screen, self.bg, self.rect)
        self.screen.blit(rend, rect)
