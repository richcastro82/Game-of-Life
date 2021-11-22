![Game of Life](https://kingcastro.com/gameoflife_github.jpg)
I first learned about this algorithm in school but only after seeing it in a YouTube video and learning that Dr. Conway passed away from COVID in 2020 did I decide to code the game out in python. 
 
 
 # Game of Life
Here is a link to the video that kick started this little project in my mind: https://www.youtube.com/watch?v=HeQX2HjkcNo


#The Game

The rules are simple. Each tile on the grid is alive or dead. 
1. Any dead tile with exactly 3 live neighbors will come to life. 
2. Any living tile with 2-3 living neighbors will remain alive. 
3. Any living tile with 0-1 living neighbors dies from under population.
4. Any living tile with 4-8 living neighbors dies from over population. 

The grid tiles will be populated at random with 50/50 odds of any tile starting in a living state. The game continues until the board finds itself in a stable state. 
