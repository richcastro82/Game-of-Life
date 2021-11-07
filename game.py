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
Width=1920
Height=1080
Size=(Width, Height)
Grey =(90,90,90)
White=(255,255,255)
Black=(0,0,0)
Scale=30
Offset=1
