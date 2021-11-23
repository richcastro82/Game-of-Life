# Richard Castro
# November 5th, 2021

# Conway's Game of Life
# Referred to as "Life" or the zero player game,
# this application runs a set of rules against a
# prearranged or completely random set of variables
# until the model reaches a solid or stable state.

#Import libraries
import time
import pygame
import rules

#Variables for quick changes to visuals
ScreenFill=pygame.image.load('Game_BG.png')
LifeBlocks=(216,251,60)
DeadBlock=(0,0,0)
Width=1600
Height=900
Scale=15
Offset=1
fps = 15


# def game_intro():
#
#     intro = True
#
#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         screen.fill(ScreenFill)
#         # largeText = pygame.font.Font('freesansbold.ttf',115)
#         # TextSurf, TextRect = text_objects("A bit Racey", largeText)
#         # TextRect.center = ((display_width/2),(display_height/2))
#         # gameDisplay.blit(TextSurf, TextRect)
#         pygame.display.update()
#         clock.tick(15)


def main():
    #Initialize Pygame
    Size=(Width, Height)
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life by King Castro")
    screen = pygame.display.set_mode(Size)
    clock = pygame.time.Clock()
    bg = pygame.image.load("gameoflife.jpg")
    black=(0,0,0)
    end_it=False
    while (end_it==False):
        # screen.fill(ScreenFill)
        myfont=pygame.font.SysFont("Britannic Bold", 40)
        nlabel=myfont.render("Start Game", 1, (255, 255, 255))
        for event in pygame.event.get():
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    end_it=True
        screen.blit(bg,(0,0))
        screen.blit(nlabel,(725,725))
        pygame.display.flip()


    #Import the rules and run environment
    Grid=rules.Board(Width, Height, Scale, Offset)
    Grid.board_seeding()
    pause=False
    run = True
    while run:
        clock.tick(fps)
        screen.blit(ScreenFill, (0,0))

    #Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pause = not pause

        Grid.Conway(off_color=DeadBlock, on_color=LifeBlocks, surface=screen, pause=pause)

    #Mouse click events
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            Grid.mousePush(mouseX, mouseY)
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()
