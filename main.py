'''
This is the main file for the Space Invaders game.
'''
import pygame
import sys
# Initialize pygame
pygame.init()
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.display.update()
game_loop()