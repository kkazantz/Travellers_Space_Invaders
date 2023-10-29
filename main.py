'''
This file contains the main game loop for the Space Invaders game.
'''
import pygame
from player import Player
from enemy import Enemy
from bullets import Bullet
# Initialize pygame
pygame.init()
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
# Create game objects
player = Player(screen_width, screen_height)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Game loop
running = True
clock = pygame.time.Clock()  # Create a clock object
enemy_spawn_timer = pygame.time.get_ticks()  # Timer for enemy spawning
game_over = False  # Flag to track game over state
game_won = False  # Flag to track game win state
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_RIGHT:
                player.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_RIGHT:
                player.moving_right = False
    if not game_over and not game_won:
        # Player movement
        running = player.update(running)
        # Player shooting
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)
        # Update game objects
        all_sprites.update()
        bullets.update()
        # Check for collisions
        if not player.check_collision(all_sprites, screen_width, screen_height):
            game_over = True
        for enemy in enemies:
            if not enemy.check_collision(all_sprites, screen_width, screen_height):
                game_over = True
            enemy.update(running, player)
        for bullet in bullets:
            bullet.check_collision(all_sprites, screen_width, screen_height)
        # Check for bullet-enemy collisions
        collided_bullets = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for bullet, collided_enemies in collided_bullets.items():
            # Handle collision with enemy
            # Update game state, e.g. increase score or remove enemy from the game
            # For example:
            # score += len(collided_enemies)
            pass
        # Spawn new enemies
        current_time = pygame.time.get_ticks()
        if current_time - enemy_spawn_timer >= 2000:  # Spawn a new enemy every 2 seconds
            enemy_spawn_timer = current_time
            new_enemy = Enemy(100, 100, screen_width, screen_height)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # Check game over condition
        if player.player_health <= 0:
            game_over = True
        # Check win condition
        if len(enemies) == 0:
            game_won = True
            game_over = True
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw game objects
    all_sprites.draw(screen)
    if game_over:
        if game_won:
            # Display win message
            win_text = pygame.font.SysFont(None, 48).render("You Win!", True, (255, 255, 255))
            screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2))
        else:
            # Display game over message
            game_over_text = pygame.font.SysFont(None, 48).render("Game Over", True, (255, 255, 255))
            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Set the frame rate to 60 frames per second
# Quit the game
pygame.quit()