import pygame
import math

# Initialization
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

# Setup Variables
ivel = 20
angle = math.radians(45)
g = 25
x = 50
y = screen.get_height() - 50
r = 50

xvel = ivel * math.cos(angle)
yvel = ivel * math.sin(angle)
tick = 0

# Run Loop
while running:
    # Stops when program exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Resets Screen
    screen.fill("black")

    pygame.draw.circle(screen, "red", (x, y), r)

    x += xvel
    y -= yvel -  (g * tick/60)

    if x <= r or x >= screen.get_width() - r:
        xvel *= -1
    if y <= r or y >= screen.get_height() -r:
        tick = 0

    pygame.display.flip()

    clock.tick(60)
    tick += 1

pygame.quit