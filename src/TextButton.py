import pygame
from Color import Color
from ReactiveButton import ReactiveButton


class TextButton(ReactiveButton):

    def __init__(self, screen, text, x, y, padding=50,color=[217, 207, 206]):
        ReactiveButton.__init__(self,color)
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.color = color
        self.font = pygame.font.Font(None, 40)
        self.padding = padding

    def draw(self):
        rend = self.font.render(self.text, True, Color.BLACK.value)
        width, height = rend.get_size()
        btnWidth, btnHeight = width + self.padding, height + self.padding
        self.rect = pygame.Rect(self.x - btnWidth/2, self.y - btnHeight/2, btnWidth, btnHeight)
        rect = pygame.Rect(0, 0, width, height)
        rect.center = self.rect.center


        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(rend, rect)
