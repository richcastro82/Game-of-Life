# Richard Castro
# November 5th, 2021

# Conway's Game of Life
# Referred to as "Life" or the zero player game,
# this application runs a set of rules against a
# prearranged or completely random set of variables
# until the model reaches a solid or stable state.

import os
import time
import numpy as np
import random
import pygame
import rules

os.environ["SDL_VIDEO_CENTERED"]='1'

Width=1920
Height=1080
Size=(Width, Height)


pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()
fps = 30


Grey =(90,90,90)
White=(255,255,255)
Black=(0,0,0)
Scale=30
Offset=1
fps = 30

Grid=rules.Board(Width, Height, Scale, Offset)
Grid.board_seeding()
pause=False
run = True
while run:
    clock.tick(fps)
    screen.fill(Black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.Conway(off_color=White, on_color=Grey, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.mousePush(mouseX, mouseY)
    pygame.display.update()


pygame.quit()
