import pygame, sys

# initialize pygame and create simple screen
pygame.init()
screen = pygame.display.set_mode((400, 500))

# create object to track time
clock = pygame.time.Clock()

while True:
    # check for these things at the beginning of each game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quit pygame and end current instance in system
            pygame.quit()
            sys.exit()

    # fill a screen with color and draw a surface on a screen
    screen.fill((175, 215, 70))

    # draw all elements in this loop
    pygame.display.update()

    # tick a clock at the end of each game loop, number specifies framerate
    clock.tick(60)
