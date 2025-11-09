# Richard Castro
# November 5th, 2021

# Conway's Game of Life
# Referred to as "Life" or the zero player game,
# this application runs a set of rules against a
# prearranged or completely random set of variables
# until the model reaches a solid or stable state.

# Novenber 2025 UPDATE - fixing some things that I left incomplete.
# Also, making a version that will display well on the Hackberry's 720p screen.
# WE ALSO NEED TO STANDARDIZE OUR MAIN PROGRAM FILENAMES. USE 'MAIN.PY' FOR ALL OF THEM.
# LETS ADD A PAUSE MENU TRIGGERED BY CLICKING 'P'
# BUT WE'LL KEEP THE CURRENT 'SPACEBAR' TO FREEZE STATE


#Import libraries
import os, time, pygame, rules

current_path = os.path.dirname(__file__)
#2025 UPDATE TO PORT TO HACKBERRY
Hackberry = False

# GENERAL SETTINGS
LifeBlocks=(216,251,60)
DeadBlock=(0,0,0)
Offset=1


def main():
    #Initialize Pygame
    pygame.init()
    fps=15
    ScreenFill=pygame.image.load(current_path+'/assets/Game_BG.png')
    Screen_Detect = pygame.display.Info()
    if Screen_Detect.current_w == 720:
        Hackberry = True
        Width = Screen_Detect.current_w
        Height = Screen_Detect.current_h
        Scale = 10
        bg = pygame.image.load(current_path+"/assets/hackberry_bg.jpg")

    else:
        Width=1600
        Height=900
        Scale=15
        bg = pygame.image.load(current_path+"/assets/gameoflife.jpg")




    Size=(Width, Height)
    pygame.display.set_caption("Conway's Game of Life by King Castro")
    screen = pygame.display.set_mode(Size)
    clock = pygame.time.Clock()
    black=(0,0,0)
    end_it=False

    while (end_it==False):
        myfont=pygame.font.SysFont("Britannic Bold", 40)
        # nlabel=myfont.render("Slow", 1, (255, 255, 255))
        # nlabel1=myfont.render("Start Game", 1, (255, 255, 255))
        for event in pygame.event.get():
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    fps=10
                    end_it=True
                if event.key==pygame.K_SPACE:
                    end_it=True
        screen.blit(bg,(0,0))
        # screen.blit(nlabel,(625,625))
        # screen.blit(nlabel1,(725,725))
        pygame.display.flip()


    #Import the rules and run environment
    Grid=rules.Board(Width, Height, Scale, Offset)
    Grid.board_seeding()
    pause=False
    run = True
    def mouseDef():
     #Mouse click events
         if pygame.mouse.get_pressed()[0]:
             mouseX, mouseY = pygame.mouse.get_pos()
             Grid.mousePush(mouseX, mouseY)

    while run:
        clock.tick(fps)
        screen.blit(ScreenFill, (0,0))

    #Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_SPACE:
                    pause = not pause

        Grid.Conway(off_color=DeadBlock, on_color=LifeBlocks, surface=screen, pause=pause)
        mouseDef()
        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()
