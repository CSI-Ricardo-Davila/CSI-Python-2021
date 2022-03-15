import pygame           #This line of code imports pygame and the functions that come with it
pygame.init()           # This line of code initializes the game

dis=pygame.display.set_mode((400,300))      #This line of code creates the screen that will be used for the game
pygame.display.update()                     #This line of code updates the screen

pygame.display.set_caption('Snake game by Edureka')      #This line of code gives the name 'Snake game by Edureka' to the screen
game_over=False                                          #This line of code creates a booleang variale that is set to False, meaning that the game is not over unitl this variable is true.
while not game_over:                                     #This line of code is a loop that says that the screen will not go away until the game_over variable is set to True
    for event in pygame.event.get():                     #This line of code runs a forloop over every event that will be in a set list. 
        # print(event)   #prints out all the actions that take place on the screen
        if event.type==pygame.QUIT:                      #This line of code says that when the program detects an attempt to close the program, it will change the game_over variable to True, and this will end the game.
            game_over=True                               #This line of code gives the variable 'game_over' a True value, which then causes the game to end.



pygame.quit()           #This line of code unitializes the game that has been started
quit()                  #This line of code unitializes everything

