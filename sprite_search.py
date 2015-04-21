import pygame, sys, random, time
from pygame.locals import *

pygame.init()

maxx = 500
maxy = 200

goalx = random.randrange(0,maxx-30)
goaly = random.randrange(0,maxy-30)

Black = pygame.Color(0,0,0)
White = pygame.Color(255,255,255)
Red = pygame.Color(255,0,0)
sheet = pygame.image.load('sprites/char2.png')


char_right1 = (200,67,21,30)
char_right2 = (231,67,21,30)
char_right3 = (263,67,21,30)
char_left1 = (200,35,21,30)
char_left2 = (231,35,21,30)
char_left3 = (263,35,21,30)

char_up1 = (200,100,21,30)
char_up2 = (231,100,21,30)
char_up3 = (263,100,21,30)
char_down1 = (200,3,21,30)
char_down2 = (231,3,21,30)
char_down3 = (263,3,21,30)

goal = (163,133,25,28)
sheet.set_clip(pygame.Rect(goal[0],goal[1],goal[2],goal[3]))
draw_goal = sheet.subsurface(sheet.get_clip())

sheet.set_clip(pygame.Rect(char_right1[0],char_right1[1],char_right1[2],char_right1[3]))
draw_char_right1 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_right2[0],char_right2[1],char_right2[2],char_right2[3]))
draw_char_right2 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_right3[0],char_right3[1],char_right3[2],char_right3[3]))
draw_char_right3 = sheet.subsurface(sheet.get_clip())


sheet.set_clip(pygame.Rect(char_left1[0],char_left1[1],char_left1[2],char_left1[3]))
draw_char_left1 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_left2[0],char_left2[1],char_left2[2],char_left2[3]))
draw_char_left2 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_left3[0],char_left3[1],char_left3[2],char_left3[3]))
draw_char_left3 = sheet.subsurface(sheet.get_clip())

sheet.set_clip(pygame.Rect(char_up1[0],char_up1[1],char_up1[2],char_up1[3]))
draw_char_up1 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_up2[0],char_up2[1],char_up2[2],char_up2[3]))
draw_char_up2 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_up3[0],char_up3[1],char_up3[2],char_up3[3]))
draw_char_up3 = sheet.subsurface(sheet.get_clip())

sheet.set_clip(pygame.Rect(char_down1[0],char_down1[1],char_down1[2],char_down1[3]))
draw_char_down1 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_down2[0],char_down2[1],char_down2[2],char_down2[3]))
draw_char_down2 = sheet.subsurface(sheet.get_clip())
sheet.set_clip(pygame.Rect(char_down3[0],char_down3[1],char_down3[2],char_down3[3]))
draw_char_down3 = sheet.subsurface(sheet.get_clip())



Window = pygame.display.set_mode((maxx,maxy))
    
count = 0
Dir = 1 #0=North, 1=East, 2=South, 3=West
charx = 0
chary = 0

#returns unused locations for random blocks
def init_board():
    blocks = []
    while len(blocks) < 25:
        i = random.randint(0,maxx-30)
        j = random.randint(0,maxx-30)
        blocks.append(pygame.Rect(i,j,10,10))


    
    
    return blocks
    



def walk(charx,chary,goalx,goaly):
    if charx < goalx:
        if chary < goaly:
            return charx+1,chary+1,3    #moving down & right
        elif chary > goaly:
            return charx+1,chary-1,1    #moving up & right
        else:
            return charx+1,chary,2      #moving right

    if charx > goalx:
        if chary < goaly:
            return charx-1,chary+1,5    #moving down & left
        elif chary > goaly:
            return charx-1,chary-1,7    #moving up & left
        else:
            return charx-1,chary,6      #moving left

    if chary < goaly:
       return charx, chary+1, 4         #moving down
    if chary > goaly:
        return charx, chary-1, 0        #moving up

        
    return charx,chary,4


def draw(Dir,count,blocks):


    #for b in blocks:
    #    pygame.draw.rect(Window,Red,b)


    
    if Dir == 0 or Dir == 1 or Dir == 7:                #moving up
        if count < 10:
            Window.blit(draw_char_up1,(charx,chary))
        elif count < 20:
            Window.blit(draw_char_up2,(charx,chary))
        else:
            Window.blit(draw_char_up3,(charx,chary))

    if Dir == 5 or Dir == 4 or Dir == 3:                #moving down
        if count < 10:
            Window.blit(draw_char_down1,(charx,chary))
        elif count < 20:
            Window.blit(draw_char_down2,(charx,chary))
        else:
            Window.blit(draw_char_down3,(charx,chary))

    if Dir == 6:
        if count < 10:                                  #moving left
            Window.blit(draw_char_left1,(charx,chary))
        elif count < 20:
            Window.blit(draw_char_left2,(charx,chary))
        else:
            Window.blit(draw_char_left3,(charx,chary))

    if Dir == 2:
        if count < 10:                                  #moving right
            Window.blit(draw_char_right1,(charx,chary))
        elif count < 20:
            Window.blit(draw_char_right2,(charx,chary))
        else:
            Window.blit(draw_char_right3,(charx,chary))
            
blocks = []
blocks = init_board()
while 1:

    for event in pygame.event.get():    #check for exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    Window.fill(Black)

    if charx == goalx and chary == goaly:       # if goal reached reset goal
        goalx = random.randrange(0,maxx-30)
        goaly = random.randrange(0,maxy-30)
        blocks = init_board()
    else:
        Window.blit(draw_goal,(goalx,goaly))

    charx,chary,Dir = walk(charx,chary,goalx,goaly) #update char & dir
    draw(Dir,count,blocks)
    
    if count > 30:          # time between char images delay
        count = 0
    else:
        count += 1
    
    pygame.time.delay(10)   # slow down drawing 
    pygame.display.update()
