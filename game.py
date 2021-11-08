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

run = True
while run:
    clock.tick(fps)
    screen.fill(Grey)


pygame.quit()
