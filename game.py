# Richard Castro
# November 5th, 2021

# Conway's Game of Life
# Referred to as "Life" or the zero player game,
# this application runs a set of rules against a
# prearranged or completely random set of variables
# until the model reaches a solid or stable state.

#Import libraries
import os
import time
import numpy as np
import random
import pygame
import rules

#Variables for quick changes to visuals
ScreenFill=(255,255,255)
LifeBlocks=(0,0,0)
Width=840
Height=600
Scale=15
Offset=1
fps = 15

#Initialize Pygame
Size=(Width, Height)
pygame.init()
pygame.display.set_caption("GAME OF LIFE - Richard Castro")
screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()

#Import the rules and run environment
Grid=rules.Board(Width, Height, Scale, Offset)
Grid.board_seeding()
pause=False
run = True
while run:
    clock.tick(fps)
    screen.fill(ScreenFill)

#Event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.Conway(off_color=ScreenFill, on_color=LifeBlocks, surface=screen, pause=pause)

#Mouse click events
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.mousePush(mouseX, mouseY)
    pygame.display.update()

pygame.quit()
