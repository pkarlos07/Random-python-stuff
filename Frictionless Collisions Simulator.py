import pygame
import math
import random

# Initialization
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

# Text Setup
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)

class dot:
    dotlist = []
    def __init__(self, mass, color, rad, xvel, yvel, xpos, ypos):
        self.mass = mass
        self.color = color
        self.rad = rad
        self.xvel = xvel
        self.yvel = yvel
        self.xpos = xpos
        self.ypos = ypos
        dot.dotlist.append(self)
    def update(self):
        self.xpos += self.xvel
        self.ypos += self.yvel
    def collision(d1, d2):
        # Angle between centers
        angle = math.atan((d1.ypos - d2.ypos) / (d1.xpos - d2.xpos))
        # Turn velocities into how much they affect eachother
        xscalar = math.cos(angle)
        yscalar = math.sin(angle)
        # Collision
        d1xinivel = d1.xvel
        d1yinivel = d1.yvel
        d1.xvel = ((d1.mass - d2.mass) / (d1.mass + d2.mass)) * d1.xvel + ((2 * d2.mass) / (d1.mass + d2.mass)) * d2.xvel
        d2.xvel = ((2 * d1.mass) / (d1.mass + d2.mass)) * d1xinivel - ((d1.mass - d2.mass) / (d1.mass + d2.mass)) * d2.xvel
        d1.yvel = ((d1.mass - d2.mass) / (d1.mass + d2.mass)) * d1.yvel + ((2 * d2.mass) / (d1.mass + d2.mass)) * d2.yvel
        d2.yvel = ((2 * d1.mass) / (d1.mass + d2.mass)) * d1yinivel - ((d1.mass - d2.mass) / (d1.mass + d2.mass)) * d2.yvel
    # def separation(d1, d2):
        

# Change these for different setups name = dot(mass, color, radius, xvel, yvel, xpos, ypos)
# dot1 = dot(10, "red", 50, 3, 7, screen.get_width() / 3, screen.get_height() / 2)
# dot2 = dot(10, "blue", 50, -5, -5, screen.get_width() * (2/3), screen.get_height() / 2)
# dot3 = dot(20, "green", 75, 4, 4, screen.get_width() / 2, screen.get_height() / 2)
dot1 = dot(10, "white", 50, 4, 0, screen.get_width() / 3, screen.get_height() / 2)
dot2 = dot(10, "white", 50, 0, 0, screen.get_width() * (2/3), screen.get_height() / 2)
dot3 = dot(10, "white", 50, 0, 0, screen.get_width() * (2/3) + 100, screen.get_height() / 2 + 75)
dot4 = dot(10, "white", 50, 0, 0, screen.get_width() * (2/3) + 100, screen.get_height() / 2 - 75)

# Run Loop
while running:
    # Stops when program exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Resets Screen
    screen.fill("black")

    # Drawing Circles
    for d in dot.dotlist:
        pygame.draw.circle(screen, d.color, (d.xpos, d.ypos), d.rad)

    pygame.display.flip()

    # Collision
    x = 0
    for d1 in dot.dotlist:
        x += 1
        for d2 in dot.dotlist[x:]:
            if math.sqrt(math.pow(d2.xpos - d1.xpos, 2) + math.pow(d2.ypos - d1.ypos, 2)) <= d1.rad + d2.rad:
                d1.collision(d2)
                # d1.separation(d2)

    # Check for wall hit
    for d in dot.dotlist:
        if d.xpos <= d.rad or d.xpos >= screen.get_width() - d.rad:
            d.xvel *= -1
        if d.ypos <= d.rad or d.ypos >= screen.get_height() - d.rad:
            d.yvel *= -1

    # Updates all dots position
    for d in dot.dotlist:
        d.update()

    # 144 fps (Note: Program speed is dependent on fps)
    clock.tick(144)

pygame.quit()

#fix collision
#fix separation