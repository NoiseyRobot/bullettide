# Draws the title screen.
import pygame
import code.draw as draw

play_button = None

def setup(font):
    global play_button
    play_button = draw.Button("play", "Play", font, 260, 180, 200, 60, draw.GRAY, draw.WHITE)

def main(screen, font):
    draw.draw_text_center(screen, "Bullet Tide", font, draw.WHITE, 360, 70)
    play_button.draw(screen)