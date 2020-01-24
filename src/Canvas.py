import pygame
from Color import Color

class Canvas:
    drawables = []  # All objects that have a "draw" method
    fps = 60
    clock = pygame.time.Clock()
    bg = Color.BLACK.value

    def __init__(self, screen, game,drawables=[]):
        self.screen = screen
        self.drawables = []
        self.game = game

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
            drawable.draw(self.screen)

        pygame.display.update()
        self.clock.tick(self.fps)

    def action(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.exit()
                break

            for actionable in self.drawables:
                actionable.action(event)

    def exit(self):
        pygame.display.set_mode([1, 1])
        self.drawables = []
        self.game.setPlaying(False)
