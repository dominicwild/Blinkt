import sys, pygame
pygame.init()

size = width, height = 600, 600
speed = [3.4, 1.5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("G:\\Users\\Dominic\\Documents\\VsCode\\Blinkt\\src\\intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit(0)
        print(event)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()