'''
The Player class representing the player's spaceship.
'''
import pygame
class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.y)
        return bullet