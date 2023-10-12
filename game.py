import pygame
import sys

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#colors
BLUE = (52,157,227)
BROWN = (227,191,134)

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Miami Beach")

#main loops

running = True #set flag true
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill with blue
    screen.fill(BLUE)

    #add sandy bottom
    rectangle_height= 150
    pygame.draw.rect(screen, BROWN, (0,screen_height-rectangle_height, screen_width, rectangle_height))

    #update the display
    pygame.display.flip()

pygame.quit()