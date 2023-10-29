'''
This file contains the Enemy class for the Space Invaders game.
'''
import pygame
from bullets import Bullet
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
    def update(self):
        self.rect.y += 2
    def check_collision(self, sprite_group):
        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, True)
        for sprite in collided_sprites:
            if isinstance(sprite, Bullet):
                # Handle collision with bullet
                pass