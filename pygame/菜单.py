# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/10 17:20
# File : 菜单.py
import pygame

pygame.init()

# Set screen size and title
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Game Menu")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load font
font = pygame.font.Font(None, 36)

# Render text for buttons
start_text = font.render("Start Game", True, BLACK)
settings_text = font.render("Settings", True, BLACK)
quit_text = font.render("Quit Game", True, BLACK)

# Get rectangles for buttons
start_rect = start_text.get_rect()
settings_rect = settings_text.get_rect()
quit_rect = quit_text.get_rect()

# Position buttons
start_rect.center = (200, 100)
settings_rect.center = (200, 150)
quit_rect.center = (200, 200)

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Get mouse position
            pos = pygame.mouse.get_pos()
            # Check if start button was clicked
            if start_rect.collidepoint(pos):
                print("Start Game")
            # Check if settings button was clicked
            if settings_rect.collidepoint(pos):
                print("Settings")
            # Check if quit button was clicked
            if quit_rect.collidepoint(pos):
                running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw buttons
    screen.blit(start_text, start_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)

    pygame.display.update()

pygame.quit()
