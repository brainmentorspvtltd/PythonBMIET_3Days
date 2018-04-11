import pygame

pygame.init()

width = 800
height = 600

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((width,height))

x = 10
y = 10

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    # x,y,width,height
    pygame.draw.rect(screen,black,[x,y,50,50])

    x += 0.5


    pygame.display.update()





