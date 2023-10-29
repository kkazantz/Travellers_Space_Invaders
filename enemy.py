'''
This file contains the Enemy class for the Space Invaders game.
'''
import pygame
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
        self.direction = "right"
    def move(self):
        if self.direction == "right":
            self.rect.x += 2
        elif self.direction == "left":
            self.rect.x -= 2
    def update(self, running):
        self.move()
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            self.direction = "down"
            self.rect.y += 50
        if player.player_health <= 0:
            running = False
        return running
    def check_collision(self, sprite_group, screen_width, screen_height):
        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, True)
        for sprite in collided_sprites:
            if isinstance(sprite, Bullet):
                # Handle collision with bullet
                pass
        return True