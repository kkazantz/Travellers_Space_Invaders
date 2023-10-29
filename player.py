'''
This file contains the Player class for the Space Invaders game.
'''
import pygame
from bullets import Bullet
from enemy import Enemy
class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player_health = 3
        self.moving_left = False
        self.moving_right = False
    def update(self, running):
        if self.moving_left:
            self.rect.x -= 5
        if self.moving_right:
            self.rect.x += 5
        # Prevent player from going off the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.player_health <= 0:
            running = False
        return running
    def check_collision(self, sprite_group, screen_width, screen_height):
        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, True)
        for sprite in collided_sprites:
            if isinstance(sprite, Enemy):
                # Handle collision with enemy
                self.rect.center = (screen_width // 2, screen_height - 50)
                self.player_health -= 1
                if self.player_health <= 0:
                    return False
        return True