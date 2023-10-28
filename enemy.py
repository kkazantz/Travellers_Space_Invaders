'''
This file contains the Enemy class.
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
    def update(self):
        self.rect.y += 2
    def draw(self, screen):
        screen.blit(self.image, self.rect)