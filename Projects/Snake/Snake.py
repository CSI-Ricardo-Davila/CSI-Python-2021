from time import time       #This line of code imports time and the functions that come with it
import pygame           #This line of code imports pygame and the functions that come with it
import time
pygame.init()           # This line of code initializes the game

blue=(0,0,255)#Establishes the snakes color with its RGB number. 
white = (255, 255, 255)
black = (0, 0, 0)
red=(255,0,0)#Establishes the color with its RGB number.

dis_width =800                      #This line of code sets the width of the display screen
dis_height = 600                     #This line of code sets the height of the display screen
dis= pygame.display.set_mode((dis_width,dis_width))      #This line of code creates the screen that will be used for the game

pygame.display.set_caption('Snake game by Edureka')      #This line of code gives the name 'Snake game by Edureka' to the screen


 

game_over=False                                          #This line of code creates a booleang variale that is set to False, meaning that the game is not over unitl this variable is true.

x1 = dis_width/2                                               #This line of code sets the starting x coordinate position for the head of the snake 
y1 = dis_height/2                                              #This line of code sets the starting y coordinate position for the head of the snake 

snake_block = 10                                        #This line of code sets the size of the snake block


x1_change = 0                                           #This line of code holds the updating values of the x coordinate. 
y1_change = 0                                           #This line of code holds the updating values of the y coordinate.

clock = pygame.time.Clock()                          #This line of code is to see the time frame while the snake is moving

snake_speed = 30                                        #This line of code sets the speed of the snake

font_style = pygame.font.SysFont(None,50)               #This line of code sets the font for the game

def message(msg,color):                                 #This line of code defines the function called message, which displays messages to on the playing screen
    mesg = font_style.render(msg,True,color)            #This line of code sets the parameters of the variable called mesg
    dis.blit(mesg, [dis_width/2, dis_height/2])         #This line of code sets the coordinates will the text will appear

while not game_over:                                     #This line of code is a loop that says that the screen will not go away until the game_over variable is set to True
    for event in pygame.event.get():                     #This line of code runs a forloop over every event that will be in a set list. 
        # print(event)   #prints out all the actions that take place on the screen
        if event.type==pygame.QUIT:                      #This line of code says that when the program detects an attempt to close the program, it will change the game_over variable to True, and this will end the game.
            game_over=True                               #This line of code gives the variable 'game_over' a True value, which then causes the game to end.
        if event.type == pygame.KEYDOWN:                 #This line of code uses the functions of KEYDOWN to move the snake
            if event.key == pygame.K_LEFT:               #This line of code moves the snake to the left.
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:            #This line of code moves the snake to the right.
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:              #This line of code moves the snake up.
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:            #This line of code moves the snake down.
                y1_change = 10
                x1_change = 0
    
    if  x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #This line of code is saying that if the snake block hits any of the edges of the screen, the game will end.
        game_over = True

    x1 += x1_change                                     #This line of code holds the updating values of the x coordinate.
    y1 += y1_change                                     #This line of code holds the updating values of the y coordinate.
    dis.fill(white)                                     #This line of code says that the display screen will be white
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])      #This line of code draws a rectangle in the display at the given cordinates
 
    pygame.display.update()                             #This line of code updates the screen
 
    clock.tick(snake_speed)                                      #This line of code sets the speed for the snake
 
    # pygame.draw.rect(dis,blue,[200,150,10,10])           #This line of code draws a rectangle in the display at the given cordinates
    
message("You lost", red)                                   #This lines of code display a message saying "You Lost" after the player has lost.
pygame.display.update()                                   #This lines of code display a message saying "You Lost" after the player has lost.
time.sleep(2)                                   #This lines of code display a message saying "You Lost" after the player has lost.

pygame.quit()           #This line of code unitializes the game that has been started
quit()                  #This line of code unitializes everything
