import pygame, sys
from pygame.locals import*


pygame.init()
clock = pygame.time.Clock()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("progetto Massa-Valtolina Breakout")
colore_sfondo = (214, 190, 200)
rosso = (255,0,0)
verde = (0,255,0)
blu = (0,0,255)


colonne = 6
righe = 6


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(colore_sfondo)

    clock.tick(60)
    pygame.display.flip()

