# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/10 19:28
# File : 时间之差 贪吃蛇.py
import pygame
import time

# Initialize Pygame
pygame.init()

# Set window size
size = (400, 400)

# Create window
window = pygame.display.set_mode(size)

# Set clock
clock = pygame.time.Clock()

# Set block size
block_size = 10

# Set initial position of snake
snake_position = [100, 100]

# Set initial direction of snake
snake_direction = "right"

# Set the initial speed of the snake
speed = 10

# Set the initial time
last_move = time.time()

# Start game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = time.time()

    # Check if the time difference between the current time and the last move time is greater than the speed
    if current_time - last_move > 1 / speed:
        # Update last move time
        last_move = current_time

        # Move the snake in the specified direction
        if snake_direction == "right":
            snake_position[0] += block_size
        elif snake_direction == "left":
            snake_position[0] -= block_size
        elif snake_direction == "up":
            snake_position[1] -= block_size
        elif snake_direction == "down":
            snake_position[1] += block_size

    # Fill the window with white
    window.fill((255, 255, 255))

    # Draw the snake
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(snake_position[0], snake_position[1], block_size, block_size))

    # Update display
    pygame.display.update()

    # Set clock tick rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
