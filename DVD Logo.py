import pygame
import math
import pyautogui

# Initialization
pygame.init()
screen = pygame.display.set_mode(pyautogui.size(), pygame.SCALED, vsync = 1)
clock = pygame.time.Clock()
running = True

logo = pygame.image.load(r"src/DVD_logo.svg.png") 
logo = logo.convert_alpha()
logo = pygame.transform.scale(logo, (400, 204))

colorlist = ["white", "red", "darkorange", "yellow", "green", "aqua", "blue", "purple", "hotpink"]
logolist = []

w = logo.get_width()
h = logo.get_height()

index = 0
for color in colorlist:
    logolist.append(logo.copy())
    for x in range(w):
        for y in range(h):
            if logolist[index].get_at((x,y)).a >= 1:
                logolist[index].set_at((x, y), color)
    index += 1


index = 0
def nextlogo():
    global index
    global logo
    if index < len(logolist) - 1:
        index += 1
        logo = logolist[index]
    else:
        index = 0
        logo = logolist[index]

logo = logolist[0]

x = screen.get_width() / 2 - logo.get_width() / 2
y = screen.get_height() / 2 - logo.get_height() / 2
xvel = 5
yvel = 5

# Run Loop
while running:
    # Stops when program exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Resets Screen
    screen.fill("black")

    screen.blit(logo, (x, y))
    x += xvel
    y += yvel

    if x <= 0 or x >= screen.get_width() - logo.get_width():
        xvel *= -1
        nextlogo()
    if y <= 0 or y >= screen.get_height() - logo.get_height():
        yvel *= -1
        nextlogo()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()