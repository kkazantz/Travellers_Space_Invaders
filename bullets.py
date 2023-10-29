'''
This file contains the Bullet class for the Space Invaders game.
'''
import pygame
from enemy import Enemy
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.y -= 5
    def check_collision(self, sprite_group):
        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, True)
        for sprite in collided_sprites:
            if isinstance(sprite, Enemy):
                # Handle collision with enemy
                pass