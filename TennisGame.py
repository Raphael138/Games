import pygame, sys
import time
import random
import math


def ball_animation():
    global  x_ball_speed, y_ball_speed, player_score, opponent_score, score_time
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        y_ball_speed = -y_ball_speed
    if ball.left <= 0:
        opponent_score+=1
        pygame.mixer.Sound.play(score_sound)
        #restarting the ball at its initial position and giving a random velocity
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        player_score += 1
        pygame.mixer.Sound.play(score_sound)
        #restarting the ball at its initial position and giving a random velocity
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and x_ball_speed <0:
        pygame.mixer.Sound.play(pong_sound)
        x_ball_speed = -x_ball_speed
    if ball.colliderect(opponent) and x_ball_speed > 0:
        pygame.mixer.Sound.play(pong_sound)
        x_ball_speed = -x_ball_speed

    ball.x += x_ball_speed
    ball.y += y_ball_speed

def player_animation():
    if player.top <= 0:
        player.y = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    player.y += player_speed

def opponent_ai():
    global opponent_speed
    if ball.x > screen_width/2:
        if opponent.y > ball.y-60+15:
            opponent_speed = -5
        elif opponent.y < ball.y-60+15:
            opponent_speed = 5
        else:
            opponent_speed = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    if opponent.y <= 0:
        opponent.y = 0
    opponent.y += opponent_speed

#initiate pygame
pygame.mixer.pre_init(44100, -16, 2, 500)
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(int(screen_width/2-15), int(screen_height/2-15),30,30)
player = pygame.Rect(10,int(screen_height/2 -60) ,10,120)
opponent = pygame.Rect(int(screen_width-10),int(screen_height/2 -60) ,10,120)

#important variables
player_speed = 0
opponent_speed = 0
x_ball_speed = 7
y_ball_speed = 7
opponent_score = 0
player_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 50)

#timer variable
score_time  = True

#sound
pong_sound = pygame.mixer.Sound("bouncing_ball.ogg")
score_sound = pygame.mixer.Sound("win_sound.ogg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 7
            if event.key == pygame.K_UP:
                player_speed = -7
        if event.type == pygame.KEYUP:
            player_speed = 0

    #game mechanics
    ball_animation()
    player_animation()
    opponent_ai()

    #visuals
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255), player)
    pygame.draw.rect(screen,(255,255,255), opponent)
    pygame.draw.ellipse(screen,(255,255,255), ball)
    pygame.draw.aaline(screen, (255,255,255), (screen_width/2, 0), (screen_width/2, screen_height))
    player_text = game_font.render(str(player_score), False, (255,255,255))
    opponent_text = game_font.render(str(opponent_score), False, (255,255,255))
    if score_time:
        current_time = pygame.time.get_ticks()
        ball.center = (int(screen_width / 2), int(screen_height / 2))

        #write timer on game
        if (current_time - score_time) < 700:
            number_three = game_font.render("3", False, (255,255,255))
            screen.blit(number_three, (screen_width/2 - 13, screen_height/2 + 20))
        if 700 < (current_time - score_time) < 1400:
            number_two = game_font.render("2", False, (255, 255, 255))
            screen.blit(number_two, (screen_width / 2 - 13, screen_height / 2 + 20))
        if  1400 <(current_time - score_time) < 2100:
            number_one = game_font.render("1", False, (255, 255, 255))
            screen.blit(number_one, (screen_width / 2 - 13, screen_height / 2 + 20))

        #make time work
        if (current_time - score_time) <2100:
            x_ball_speed, y_ball_speed = 0,0
        else:
            score_time = None
            y_ball_speed = 7*random.choice((1, -1))
            x_ball_speed = 7*random.choice((1, -1))

    screen.blit(player_text, (screen_width/2 - 50 - math.log10(1+player_score)*20, 0))
    screen.blit(opponent_text, (screen_width/2 + 25 + math.log10(1+opponent_score)*20, 0))

    pygame.display.flip()
    clock.tick(60)
