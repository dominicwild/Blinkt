import pygame
from Color import Color

class Canvas:
    drawables = []  # All objects that have a "draw" method
    fps = 60
    clock = pygame.time.Clock()
    bg = Color.WHITE.value

    def __init__(self, screen, drawables=[]):
        self.screen = screen
        self.drawables = drawables

    def add(self, drawable):
        if (drawable == None):
            return
        if (isinstance(drawable, list)):
            for o in drawable:
                self.drawables.append(o)
        else:
            self.drawables.append(drawable)

    def draw(self):
        self.screen.fill(self.bg)
        for drawable in self.drawables:
            drawable.draw()

        pygame.display.update()
        self.clock.tick(self.fps)
