import pygame


class ColorPanel():
    widthColor = 41
    heightColor = 41
    padding = 5

    def __init__(self, game, x, y, width, height):
        self.game = game
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, screen):
        guesses = self.game.getGuess()
        midY = (self.y + (self.y + self.height)) / 2
        endX = self.x + self.width + self.padding
        rects = []

        for i in range(len(guesses)):
            # if(i == 0):
            #     rect = pygame.Rect(endX + (self.widthColor + self.padding), midY, self.widthColor,self.heightColor)
            # else:
            rect = pygame.Rect(endX + (self.widthColor + self.padding)*i+1, midY, self.widthColor, self.heightColor)

            rect = rect.move(-self.width, 0)

            if(self.width < (self.widthColor + self.padding)*(len(guesses))):
                rect = rect.move(-(((self.widthColor + self.padding)*len(guesses)) - self.width + self.padding), 0)

            rects.append(rect)

        for i in range(len(rects)):
            pygame.draw.rect(screen,guesses[i].value,rects[i])

    def action(self,event):
        pass
