import pygame
from code.window import window
pygame.init()

screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Bullet Tide")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    window()
    pygame.display.flip()
pygame.quit()