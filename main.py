from pathlib import Path
import pygame
pygame.init()


# File paths
FONT_PATH = Path(__file__).resolve().parent / "assets" / "freesansbold.ttf"


# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)


# Class definitions
class Button:
    buttons = {}

    def __init__(self, name, text, font, x, y, width, height, color, text_color):
        self.text = text
        self.font = font
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        Button.buttons[name] = self

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        screen.blit(text, text.get_rect(center=self.rect.center))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)


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


# Helper functions
def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def draw_text_center(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Draws the title screen.
play_button = None


def titlesetup(font):
    global play_button
    play_button = Button("play", "Play", font, 260, 180, 200, 60, GRAY, WHITE)


def titlemain(screen, font):
    draw_text_center(screen, "Bullet Tide", font, WHITE, 360, 70)
    play_button.draw(screen)


# Main game loop
screen = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
pygame.display.set_caption("Bullet Tide")

titlesetup(game.bigfont)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if game.game_state == "title":
        titlemain(screen, game.bigfont)
        if play_button.clicked(event):
            game.game_state = "playing"

    if game.game_state == "playing":
        print()
    pygame.display.flip()

pygame.quit()