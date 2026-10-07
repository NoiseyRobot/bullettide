import pygame
from code.window import window
pygame.init()

width = 720
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bullet Tide")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    window(width, height)
    pygame.display.flip()
pygame.quit()