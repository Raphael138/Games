import pygame, sys
import random
import time
from blue_tetrimino import blue_tetrimino
from green_tetrimino import green_tetrimino
from light_blue_tetrimino import light_blue_tetrimino
from orange_tetrimino import orange_tetrimino
from purple_tetrimino import purple_tetrimino
from red_tetrimino import red_tetrimino
from yellow_tetrimino import yellow_tetrimino
from grid import Grid 

#initialize game
pygame.init()
clock = pygame.time.Clock()

#color variables
white = (255,255,255)
black = (0,0,0)

#create screen related variables
rows = 20
columns = 10
pixel_size = 30
screen_width = 10*pixel_size+100
screen_height = 20*pixel_size + 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

#Defining drawing functions
def drawScreen ():
    for i in range(0,rows+1):
        pygame.draw.aaline(screen, white, (50, 100+i*pixel_size), (screen_width-50, 100+i*pixel_size))
    for i in range(0, columns+1):
        pygame.draw.aaline(screen, white, (50+i*pixel_size, 100), (50+i*pixel_size, screen_height-100))

#Getting random bloks
def getRandomTetrimino():
    n = random.randrange(0,7)
    if n==0:
        return yellow_tetrimino(4,0, pixel_size)
    elif n==1:
        return red_tetrimino(4, 1, 0,pixel_size)
    elif n==2:
        return green_tetrimino(4 , 1, 0, pixel_size)
    elif n==3:
        return light_blue_tetrimino(3, 0, 1, pixel_size)
    elif n==4:
        return orange_tetrimino(3, 1, 0, pixel_size)
    elif n==5:
        return blue_tetrimino(3,1,0, pixel_size)
    else:
        return purple_tetrimino(3,1,0, pixel_size)

#Temporary function to print the grid
def printMat(mat):
    for i in mat:
        for j in i:
            print(0 if j==0 else 1, end=" ")
        print()

#Creating grid
grid = Grid(columns, rows, pixel_size)

#creating beginning variable
current_block = getRandomTetrimino()
block_speed = 0
counter = 0

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            current_block.determine(event, grid)
            pygame.display.update()

    #initializing screen
    screen.fill(black)

    #drawing the rows an columns
    drawScreen()

    #drawing every past block
    grid.draw(screen)
    #drawing the blocks
    counter+=1
    if counter%20==0:
        current_block.y += 1

    printMat(grid.mat)
    print()

    current_block.draw(screen)
    if current_block.collision(grid):
        grid.update(current_block)
        current_block = getRandomTetrimino()

    clock.tick(15)
    pygame.display.update()
