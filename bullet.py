'''
The Bullet class representing the bullets fired by the player and the enemies.
'''
import pygame
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 20))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    def move(self):
        self.rect.y -= self.speed