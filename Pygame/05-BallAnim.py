import pygame

pygame.init()

red = 255,0,0
white = 255,255,255

width = 800
height = 600

screen = pygame.display.set_mode((width,height))

move_x = 2
move_y = 2

x = 0
y = 0

clock = pygame.time.Clock()
FPS = 50

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.circle(screen,red,[x,y],50)

    x += move_x
    y += move_y

    if x > width - 50:
        move_x = -2
    elif y > height - 50:
        move_y = -2
    elif x < 50:
        move_x = 2
    elif y < 50:
        move_y = 2

    pygame.display.update()
    # clock.tick(FPS)




