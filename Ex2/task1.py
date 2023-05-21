import pygame
from pygame.locals import *
import sys
from random import *

# initialize game
pygame.init()
screen = pygame.display.set_mode((1024, 780))
pygame.display.set_caption("Task 1")

c_ocean = (80, 170, 255)
c_red = (200, 100, 100)

island = pygame.image.load("island.png").convert_alpha()
island_size = 150
island = pygame.transform.scale(island, (island_size, island_size))
island_pos_1 = (randint(0+island_size,1024-island_size), randint(0+island_size,780-island_size))
island_pos_2 = (randint(0+island_size,1024-island_size), randint(0+island_size,780-island_size))
island_pos_3 = (randint(0+island_size,1024-island_size), randint(0+island_size,780-island_size))
island_pos_4 = (randint(0+island_size,1024-island_size), randint(0+island_size,780-island_size))
island_pos_5 = (randint(0+island_size,1024-island_size), randint(0+island_size,780-island_size))

boat = pygame.image.load("boat.png").convert_alpha()
boat = pygame.transform.scale(boat, (150, 50))
x = 0
y = 0
new_x = 0
new_y = 0

path = []

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_x, new_y = pygame.mouse.get_pos()
            new_x = new_x - boat.get_width() / 2
            new_y = new_y - boat.get_height() / 2
    
    screen.fill(c_ocean)
    screen.blit(island, island_pos_1)
    screen.blit(island, island_pos_2)
    screen.blit(island, island_pos_3)
    screen.blit(island, island_pos_4)
    screen.blit(island, island_pos_5)

    screen.blit(boat, (x,y))

    if new_x > x:
        x = x + 1
    if new_x < x:
        x = x - 1

    if new_y > y:
        y = y + 1
    if new_y < y:
        y = y - 1

    path.append((x + boat.get_width() / 2, y + boat.get_height() / 2))
    
    for i in range(len(path)-1):
        pygame.draw.line(screen, (255,255,255), path[i], path[i+1], 2)

    pygame.display.update()

