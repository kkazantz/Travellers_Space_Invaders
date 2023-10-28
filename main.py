'''
This is the main file for the Space Invaders game.
'''
import pygame
import sys
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
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Create player object
player = Player(screen_width, screen_height)
# Create enemy objects
enemies = pygame.sprite.Group()
for i in range(5):
    enemy = Enemy(100 + i * 150, 100, screen_width, screen_height)
    enemies.add(enemy)
# Create bullet objects
bullets = pygame.sprite.Group()
# Game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)
        player.update()
        enemies.update()
        bullets.update()
        # Check for collisions between bullets and enemies
        for bullet in bullets:
            if pygame.sprite.spritecollide(bullet, enemies, True):
                bullets.remove(bullet)
        screen.fill(BLACK)
        player.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        pygame.display.update()
game_loop()