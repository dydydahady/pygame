#Import pygame module
import pygame

#Import pygame.locals for easier access to key coordinates
#Updated to conform to flake8 and black standards
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Initialise the game
pygame.init()

#CREATE DISPLAY
#Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Create the screen object
#The size is determined by the constatnts SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#GAME LOOP
#Variable to keep main loop running
running_flag = True

#Main Loop
while running_flag:
    #Look at every event in game
    for event in pygame.event.get():
        #Did the user hit a key?
        if event.type == KEYDOWN:
            #Was it ESC key? If yes, exit loop
            if event.key == K_ESCAPE:
                running_flag = False
        
        #Did the user click the close button? If yes, exit loop
        elif event.type == QUIT:
            running_flag = False

#Fill the screen with white
screen.fill((255,255,255))

#Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50,50))

#Give the surface a colour to seperate it from the background
surf.fill((0,0,0))
rect = surf.get_rect()