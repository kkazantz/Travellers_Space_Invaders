'''
This file contains the main game loop for the Space Invaders game.
'''
import pygame
from player import Player
from enemy import Enemy
from bullets import Bullet
# Initialize pygame
pygame.init()
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
# Create game objects
player = Player(screen_width, screen_height)
enemy = Enemy(100, 100, screen_width, screen_height)
bullet = Bullet(400, 500)
# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, bullet)
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update game objects
    all_sprites.update()
    # Check for collisions
    player.check_collision(all_sprites)
    enemy.check_collision(all_sprites)
    bullet.check_collision(all_sprites)
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw game objects
    all_sprites.draw(screen)
    # Update the display
    pygame.display.flip()
# Quit the game
pygame.quit()