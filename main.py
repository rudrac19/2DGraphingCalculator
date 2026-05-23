import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
GRAY  = (128,128,128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graphing Calculator")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()