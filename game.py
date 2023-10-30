'''
The Game class responsible for managing the game state.
'''
import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
class Game:
    def __init__(self, window):
        self.window = window
        self.player = Player(400, 500)
        self.enemies = []
        self.bullets = []
        # Create enemies
        for row in range(5):
            for col in range(10):
                enemy = Enemy(100 + col * 60, 50 + row * 60)
                self.enemies.append(enemy)
        # Load images
        self.background_image = pygame.image.load("background.png")
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))
        self.button_pause_image = pygame.image.load("button_pause.png")
        self.button_pause_image = pygame.transform.scale(self.button_pause_image, (50, 50))
        self.button_quit_image = pygame.image.load("button_quit.png")
        self.button_quit_image = pygame.transform.scale(self.button_quit_image, (50, 50))
        self.button_resume_image = pygame.image.load("button_resume.png")
        self.button_resume_image = pygame.transform.scale(self.button_resume_image, (50, 50))
        self.button_sound_off_image = pygame.image.load("button_sound_off.png")
        self.button_sound_off_image = pygame.transform.scale(self.button_sound_off_image, (50, 50))
        self.button_sound_on_image = pygame.image.load("button_sound_on.png")
        self.button_sound_on_image = pygame.transform.scale(self.button_sound_on_image, (50, 50))
        self.button_start_image = pygame.image.load("button_start.png")
        self.button_start_image = pygame.transform.scale(self.button_start_image, (50, 50))
    def update(self):
        # Update player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_SPACE]:
            bullet = self.player.shoot()
            self.bullets.append(bullet)
        # Update enemies
        for enemy in self.enemies:
            enemy.move()
        # Update bullets
        for bullet in self.bullets:
            bullet.move()
    def render(self):
        # Draw background
        self.window.blit(self.background_image, (0, 0))
        # Draw player
        self.window.blit(self.player.image, self.player.rect)
        # Draw enemies
        for enemy in self.enemies:
            self.window.blit(enemy.image, enemy.rect)
        # Draw bullets
        for bullet in self.bullets:
            self.window.blit(bullet.image, bullet.rect)
        # Draw buttons
        self.window.blit(self.button_pause_image, (10, 10))
        self.window.blit(self.button_quit_image, (70, 10))
        self.window.blit(self.button_resume_image, (130, 10))
        self.window.blit(self.button_sound_off_image, (190, 10))
        self.window.blit(self.button_sound_on_image, (250, 10))
        self.window.blit(self.button_start_image, (310, 10))