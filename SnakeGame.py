import pygame, sys
import random
import time

"""NOTE: SOMEBITS OF CODES HAVE BEEN DELETED BUT THE SNAKEAI FILE SHOULD HAVE A FINISHED VERSION OF THE GAME"""

#defining the class apple
class Apple:
    def create(self):
        self.x = random.randrange(0, columns)
        self.y = random.randrange(0, rows)
        self.rect = pygame.Rect(self.x * 30 + 100, self.y * 30 + 50, pixel_wl, pixel_wl)
    def draw(self):
        pygame.draw.ellipse(screen, (255,0,0), self.rect)
    def check(self):
        global score
        if self.x == snake[0].x and self.y == snake[0].y:
            #should add something to make sure that the apple does form itself in the snake's body
            self.create()
            z = True
            while z:
                z = False
                for i in snake:
                    if i.x == self.x and i.y == self.y:
                        self.create()
                        z = True
            self.draw()

            #add 1 to score
            score +=1

            # adding a block to the snake body
            if snake_velocity[0] == 1:
                snake.insert(1, Snake(snake[0].x-1, snake[0].y))
            if snake_velocity[0] == -1:
                snake.insert(1, Snake(snake[0].x+1, snake[0].y))
            if snake_velocity[1] == 1:
                snake.insert(1, Snake(snake[0].x, snake[0].y-1))
            if snake_velocity[1] == -1:
                snake.insert(1, Snake(snake[0].x, snake[0].y+1))

#defining the class for the body of the snake
class Snake:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    def draw(self):
        self.rect = pygame.Rect(self.x * 30 + 100, self.y * 30 + 50, pixel_wl, pixel_wl)
        pygame.draw.rect(screen, (0,255,0), self.rect)

#updating and drawing score
def write_score_record():
    score_write = font.render("Score: "+ str(score), False, (255,255,255))
    screen.blit(score_write, (0,0))
    record_write = font.render("Record: " + str(record), False, (255, 255, 255))
    screen.blit(record_write, (columns*pixel_wl, 0))

# defining function
def move_snake_body():
    global snake
    for i in snake:
        i.draw()
    self_collision()
    for i in range(0,len(snake)):
        if i>0:
            j = len(snake) - i
            snake[j].x = snake[j-1].x
            snake[j].y = snake[j-1].y
#defining a game over function
def game_over():
    if record < score:
        #updating record
        Snake_game_record = open("Snake_game_record.txt", "w")
        Snake_game_record.write(str(score))
        Snake_game_record.close()
        #putting congratulation sign
        font1 = pygame.font.Font("freesansbold.ttf", 100)
        screen.fill((0, 0, 0))
        new_record = font1.render("NEW RECORD !!", True, (255, 255, 255))
        screen.blit(new_record, (round(columns / 2) * pixel_wl - 300, round(rows / 2) * pixel_wl - 100))
        record_write = font.render("Record: " + str(score), False, (255, 255, 255))
        screen.blit(record_write, (round(columns / 2) * pixel_wl + 10, round(rows / 2) * pixel_wl + 100))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    else:
        font1 = pygame.font.Font("freesansbold.ttf", 100)
        screen.fill((0, 0, 0))
        #game over sign
        game_over = font1.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (round(columns / 2) * pixel_wl - 200, round(rows / 2) * pixel_wl - 100))
        score_write = font.render("Score: " + str(score), False, (255, 255, 255))
        screen.blit(score_write, (round(columns / 2) * pixel_wl + 25, round(rows / 2) * pixel_wl + 50))
        record_write = font.render("Record: " + str(record), False, (255, 255, 255))
        screen.blit(record_write, (round(columns / 2) * pixel_wl +10, round(rows / 2) * pixel_wl + 100))
        pygame.display.flip()
        #exiting pygame after 3 seconds of waiting
        time.sleep(3)
        pygame.quit()
        sys.exit()

#function which finds collision
def wall_collision():
    #wall collision
    if snake[0].x ==-1  and snake_velocity[0] == -1:
        game_over()
    if snake[0].x == columns and snake_velocity[0] == 1:
        game_over()
    if snake[0].y == -1 and snake_velocity[1] == -1:
        game_over()
    if snake[0].y == rows and snake_velocity[1] == 1:
        game_over()

def self_collision():
    #self collision
    for i in range(0, len(snake)):
        if i>1:
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                game_over()


def movement():
    global snake_direction
    if event.key == pygame.K_DOWN:
        snake_direction = "down"
    if event.key == pygame.K_UP:
        snake_direction = "up"
    if event.key == pygame.K_RIGHT:
        snake_direction = "right"
    if event.key == pygame.K_LEFT:
        snake_direction = "left"

def move_snake_head():
    global snake_velocity, snake, last_direction
    #determine the snake head velocity
    if snake_direction == "right" and last_direction != "left":
        last_direction = snake_direction
        snake_velocity[0] = 1
        snake_velocity[1] = 0
    if snake_direction == "left" and last_direction!="right":
        last_direction = snake_direction
        snake_velocity[0] = -1
        snake_velocity[1] = 0
    if snake_direction == "up" and last_direction != "down":
        last_direction = snake_direction
        snake_velocity[0] = 0
        snake_velocity[1] = -1
    if snake_direction == "down" and last_direction!="up":
        last_direction = snake_direction
        snake_velocity[0] = 0
        snake_velocity[1] = 1

    #determine the snake head position
    snake[0].x += snake_velocity[0]
    snake[0].y += snake_velocity[1]


#initializing pygame
pygame.init()
clock = pygame.time.Clock()

#storing the record
Snake_game_record = open("Snake_game_record.txt", "r")
record = int(Snake_game_record.readline())
Snake_game_record.close()

#starting screen
rows = 20
columns = 30
pixel_wl = 30
screen_height = rows*pixel_wl+100
screen_width = columns*pixel_wl + 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

#definit the font used
font = pygame.font.Font("freesansbold.ttf", 30)

#defing the snake velocity
snake_velocity = [1,0]

#defining beginning variables
apple = Apple()
apple.create()
snake = [Snake(round(columns/2), round(rows/2)), Snake(round(columns/2), round(rows/2)),Snake(round(columns/2)-1, round(rows/2))]
snake_direction = "right"
last_direction = "right"
score = 0

#game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            movement()

    #making sure screen is reinitialized
    screen.fill((0,0,0))

    #chekcing self collision
    self_collision()

    #updating snake head position based on velocity
    move_snake_head()

    #drawing apple
    apple.draw()

    #checking for apple and snake colusion
    apple.check()

    #updating snake body position and drawing
    move_snake_body()

    #Updating score board
    write_score_record()

    #find collision
    wall_collision()

    #drawing the lines
    for i in range(100, screen_width-99, pixel_wl):
        pygame.draw.aaline(screen, (255,255,255), (i, 50), (i, screen_height-50))
    for i in range(50, screen_height-49, pixel_wl):
        pygame.draw.aaline(screen, (255,255,255), (100, i), (screen_width-100, i))

    #updating screen
    pygame.display.flip()
    clock.tick(6)
    
if __name__== "__main__":
    main()
