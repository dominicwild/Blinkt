import pygame
import sys
from Button import Button
from Color import Color

pygame.init()
clock = pygame.time.Clock()
fps = 60
size = width, height = [1000, 900]
midpoint = (width / 2, height / 2)
bg = [255, 255, 255]

screen = pygame.display.set_mode(size)

buttonHeight = height/2
buttonWidth = width/2

rect1 = pygame.Rect(midpoint[0], midpoint[1], buttonWidth, buttonHeight)
rect2 = pygame.Rect(midpoint[0] - buttonWidth, midpoint[1], buttonWidth, buttonHeight)
rect3 = pygame.Rect(midpoint[0] - buttonWidth, midpoint[1] - buttonHeight, buttonWidth, buttonHeight)
rect4 = pygame.Rect(midpoint[0], midpoint[1] - buttonHeight, buttonWidth, buttonHeight)

button1 = Button(Color.RED, [0])
button1.setDraw(screen, rect1)
button2 = Button(Color.BLUE, [0])
button2.setDraw(screen, rect2)
button3 = Button(Color.YELLOW, [0])
button3.setDraw(screen, rect3)
button4 = Button(Color.GREEN, [0])
button4.setDraw(screen, rect4)

buttons = [button1, button2, button3, button4]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print("Button pressed: " + button.color.name)
                    button.pressed()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button
            for button in buttons:
                button.resetGUIColor()
                if button.rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print("Button released: " + button.color.name)

    screen.fill(bg)
    for button in buttons:
        pygame.draw.rect(screen, button.getGUIColor(), button.rect)  # draw button
        # print(button.color)
    # pygame.draw.rect(screen, [255, 0, 0], button1)
    # pygame.draw.rect(screen, [0, 255, 0], button2)
    # pygame.draw.rect(screen, [0, 0, 255], button3)
    # pygame.draw.rect(screen, [0, 255, 255], button4)

    pygame.display.update()
    clock.tick(fps)
