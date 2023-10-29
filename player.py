'''
This file contains the Player class for the Space Invaders game.
'''
import pygame
from enemy import Enemy
from bullets import Bullet
class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
    def check_collision(self, sprite_group):
        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, False)
        for sprite in collided_sprites:
            if isinstance(sprite, Enemy):
                # Handle collision with enemy
                pass
            elif isinstance(sprite, Bullet):
                # Handle collision with bullet
                pass