import pygame
from pathlib import Path
import code.titlescreen as titlescreen
pygame.init()


FONT_PATH = Path(__file__).resolve().parent / "assets" / "freesansbold.ttf"

class Game:
    def __init__(self):
        # Window variables and default FPS
        self.bigfont = pygame.font.Font(str(FONT_PATH), 36)
        self.SCREEN_WIDTH = 720
        self.SCREEN_HEIGHT = 480
        self.FPS = 60
        # Game Variables
        self.score = 0
        self.game_state = "title"
        self.player_health = 100
game = Game()

screen = pygame.display.set_mode((Game().SCREEN_WIDTH, Game().SCREEN_HEIGHT))
pygame.display.set_caption("Bullet Tide")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if game.game_state == "title":
        titlescreen.setup(game.bigfont)
        titlescreen.main(screen, game.bigfont)
    pygame.display.flip()
pygame.quit()