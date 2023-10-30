'''
The Enemy class representing the enemy invaders.
'''
import pygame
class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
    def move(self):
        self.rect.y += self.speed