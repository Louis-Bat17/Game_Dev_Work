import pygame
import random
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Set up the game window
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Load game assets
background_image = pygame.image.load("Assets/background.png")
background_image = pygame.transform.scale(background_image, (2000,1050))


player_image = pygame.image.load("Assets/player.png")
player_pos = [320, 240]

ball_image = pygame.image.load("Assets/incoming_ball.png")
ball_rect = ball_image.get_rect()
ball_pos = [600, 240]

ball_speed = -0.150  # Speed at which the ball moves horizontally
clock = pygame.time.Clock()
# Game loop
while True:
    
    framerate = int(clock.get_fps())
    pygame.display.set_caption(f"Running at {framerate} fps.")
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Update game state
    keys = pygame.key.get_pressed()
    checker = False
    if keys[pygame.K_LEFT]:
        if player_pos[0] > 0:
            player_pos[0] -= 0.25
    if keys[pygame.K_RIGHT]:
        if player_pos[0] < window_size[0]-player_image.get_width():
            player_pos[0] += 0.25
    if keys[pygame.K_UP]:
        if player_pos[1] > 0:
            player_pos[1] -= 0.25
    if keys[pygame.K_DOWN]:
        if player_pos[1] < window_size[1]-player_image.get_height():
            player_pos[1] += 0.25
    if keys[pygame.K_SPACE]:
        if player_pos[1] > 0:
            player_pos[1] -= 0.25
    # Update ball position
    ball_pos[0] += ball_speed
    if ball_pos[0] < 0:
        ball_pos[0] = window_size[0]
        random_number = random.randint(0, 480)
        ball_pos[1] = random_number

    player_rect = pygame.Rect(player_pos, player_image.get_size())
    ball_rect = pygame.Rect(ball_pos, ball_image.get_size())
    if player_rect.colliderect(ball_rect):
        # Player and ball have collided, end the game
        messagebox.showerror("Oh no!", "The ball caught you! Game Over.")
        player_pos = [320, 240]
        ball_pos = [600, random.randint(0, 480)]
        ball_speed = -0.150

    # Render game
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))  # Draw the background image first
    screen.blit(player_image, player_pos)
    screen.blit(ball_image, ball_pos)
    pygame.display.flip()