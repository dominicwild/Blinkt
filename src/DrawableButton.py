import pygame


class DrawableButton():
    color = None
    hovering = False
    pressed = False

    def __init__(self, color, game, rect=None):
        self.color = color
        self.rect = rect
        self.game = game

    def draw(self, screen):
        if (self.hovering and not self.pressed):
            color = [i * 0.75 for i in self.color.value]
        elif (self.pressed):
            color = [i * 0.5 for i in self.color.value]
        else:
            color = self.color.value

        pygame.draw.rect(screen, color, self.rect)
        # self.reset()

    def reset(self):
        self.hovering = False
        self.pressed = False

    def isPressed(self, state):
        self.pressed = state

    def isHovering(self, state):
        self.hovering = state

    def action(self, event):

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            if (self.rect.collidepoint(mousePos) and not self.game.getPressedButton()):
                self.hovering = True
            else:
                self.hovering = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if self.rect.collidepoint(mousePos):
                self.pressed = True
                self.game.setPressedButton(self)
            else:
                self.pressed = False

        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
            self.game.setPressedButton(None)

        # If mouse has left screen
        if not bool(pygame.mouse.get_focused()):
            self.hovering = False
            self.pressed = False
