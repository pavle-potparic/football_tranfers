import pygame
import random

pygame.init()

WHITE = (255, 255, 255)

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Football transfers")

square_size = 100
square_x = (window_width - square_size) // 2
square_y = (window_height - square_size) // 2

square_color = (0, 128, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if square_x < mouse_x < square_x + square_size and square_y < mouse_y < square_y + square_size:
                square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill(WHITE)

    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    pygame.display.flip()

pygame.quit()
