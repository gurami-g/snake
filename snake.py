from re import X
import sys
from tkinter import SEPARATOR
from turtle import Screen, speed
import pygame
import sys
import os
import random
import math


pygame.imit()
pygame.display.set_caption('Snake Game')
pygame.font.init()
random.speed()


#we will declare global constant definitions

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE # we will keep both food and size of snake same
SEPARATION = 10 #separarion between two pixels
SCREEN_HEIGHNT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {'UP':1,'DOWN':2,'LEFT':3, 'RIGTH':4}



# we will initialise screen

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHNT),pygame.HWSURFACE)

# we have use hw surface which stands for hardware surface rafers to using memory on the video xcard for storing
# draw as opposed to main memory


#resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color('green'))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0) 
black = pygame.Color(0,0,0)


# for clock at the left corner
gameClock = pygame.time.Clock()

def checkCollision(posA,As ,posB , Bs): # As is the size ofa and Bs is the size of b
    if(posA.x <posB.x+Bs and posA+As > posB.x and posA.y <posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

# to Chek the boundaries rere we are not limiting boundaries like it can pass throught screen  an came for after

def cheklimite(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0):
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if snake.y > (SCREEN_HEIGHNT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0):
        snake.y - SCREEN_HEIGHNT - SNAKE_SIZE


# we will make class for food 

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color('orange') #color of food


    def draw(self,screen:
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)


class segment:
    self.x = x
    self.y = y
    self.direction = KEY['up']
    self.color = "white"




# we will define keys

def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY['UP']
            elif event.key == pygame.K_DOWN:
                return KEY['DOWN']
            elif event.key == pygame.K_LEFT:
                return KEY['LEFT']
            elif event.key == pygame.K_RIGHT:
                return KEY['RIGHT']
            #for exit
            elif event.key == pygame.K_ESCAPE:
                return KEY['exit']
            # if we want tocontinue playing again
            elif event.key == pygame.K_y:
                return KEY['yes']
            # if we don`t want to play game
            elif event.key == pygame.K_n:
                return KEY['no']
        if event.type == pygame.QUIT:
            sys.exit(0)


def endGame():
    message = game_over_font.render('Game Over',1,pygame.Color('white'))
    message_play_again = play_again_font.render('Play Again ?',1,pygame.Color('green'))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

    pygame.dispaly.flip()
    pygame.dispaly.update()

    mKey = getKey()
    while(mKey != 'exit'):
        if(mKey =='yes'):
            main()
        elif(mKey == 'no'):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color('red'))
    screen.blit(score_msg,(SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH - 45,14))

def drawGameTime(gameTime):
    game_time = score_font.render('Time:',1,pygame.Color('white'))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color('white'))
    screen.blit(game_time,(30,10))
    screen.blit(game_time_numb,(105,14))

def exitScreen():
    pass



def main():
   score = 0
        

