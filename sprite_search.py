import pygame, sys, random, time
from pygame.locals import *

'''
in pygame you must do this step before anything else (pygame.init())
'''
pygame.init()

'''
this is the max window setting / world for our sprites to play in.
feel free to adjust 
'''
maxx = 500
maxy = 200

'''
our goal sprite will teleport around the world waiting for the other sprite to catch it.
goalx/y represent where this sprite is at any given time.  since we want him to randomly 
jump around, we use the random module
'''
goalx = random.randrange(0,maxx-30)
goaly = random.randrange(0,maxy-30)

'''
simply setting the colors we will later use & loading the sprite sheet we want
'''
Black = pygame.Color(0,0,0)
White = pygame.Color(255,255,255)
Red = pygame.Color(255,0,0)
#sheet = pygame.image.load('sprites/char2.png')
sheet = pygame.image.load('char2.png')

'''
looking at the sprite sheets we draw boxes around each sprite we want to grab.
to figure this out open the sprite sheet in any photo editor and put the curser
on the upper left/right & bottom left/right of the image you want to use.  
This creates a box around the sprite.

To animate it we need to grab multiple images of the sprite "moving".  To get
the animation to work, we simple blit (draw) a different motion per x seconds.
eg at time = 0 we draw left leg forward sprite, t = 1 we draw legs together sprite
t = 2 we draw right leg forword sprite, etc (play with the timing to make it look real)
'''
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

'''
these lines simply take the sprite image (stored as our 4 tuples) and creates an interactive 
box within pygame.  Before this all we had was tuples but no link from the sprite image to pygame.
this step links the sprite images to pygame
'''

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


'''
this creates our world (box) of six maxx/maxy
'''
Window = pygame.display.set_mode((maxx,maxy))


count = 0       # used for timing (draw running sprite at count/time = ___)
Dir = 1         #0=North, 1=East, 2=South, 3=West
charx = 0       #where our running sprite is at any given moment
chary = 0

'''
this simply gives us an unused location to draw our sprites (makes sure they do not overlap)
'''
def init_board():
    blocks = []
    while len(blocks) < 25:
        i = random.randint(0,maxx-30)
        j = random.randint(0,maxx-30)
        blocks.append(pygame.Rect(i,j,10,10))


    
    
    return blocks
    


'''
here is the logic for our running sprite.  He simply moves in a linear path from his 
current location to the goal sprite once it appears
'''
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

'''
depending on which dir (direction) our running sprite is going at any given moment,
we need to blit / draw the correct image to the screen.  eg if he is running down
we want his front, if he is running to the right, we want his right image, etc.
'''
def draw(Dir,count,blocks):


    
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

'''
here is our main while loop that never ends.  This will allow our sprites to 
chase each other until the user closes the window
'''
while 1:

    for event in pygame.event.get():    #check for exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Window.fill(Black)                          #fills the screen with black color (backdrop)

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
