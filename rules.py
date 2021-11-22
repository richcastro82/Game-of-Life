#Richard Castro
#Game of life - Game rules file

# Import libraries
import pygame
import numpy as np
import random

class Board:
#   Initial Board setup class
    def __init__(self, Width, Height, Scale, Offset):
        self.scale = Scale
        self.columns = int(Height/Scale)
        self.rows=int(Width/Scale)
        self.size=(self.rows, self.columns)
        self.grid_array=np.ndarray(shape=(self.size))
        self.offset=Offset

#   Random seeding of the Board
    def board_seeding(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y]=random.randint(0,1)

#   Determine neighbor status
    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

#   Game of Life rules
    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                purp=(147,64,246)
                # random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, purp, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next


#   Mouse event handler
    def mousePush(self, x, y):
        _x=x//self.scale
        _y=y//self.scale
        if self.grid_array[_x][_y]!=None:
            self.grid_array[_x][_y]=1
