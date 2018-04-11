import pygame

pygame.init()

width = 800
height = 600

red = 255,0,0

screen = pygame.display.set_mode((width,height))

screen.fill(red)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()





