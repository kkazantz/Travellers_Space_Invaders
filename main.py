'''
The main entry point of the Space Invaders game.
'''
import pygame
from game import Game
# Initialize Pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")
# Create the game instance
game = Game(window)
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update game state
    game.update()
    # Render game
    game.render()
    # Update display
    pygame.display.flip()
# Quit the game
pygame.quit()