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

Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHNT),pygame.HWSURFACE)

# we have use hw surface which stands for hardware surface rafers to using memory on the video xcard for storing
# draw as opposed to main memory


#resources
scrole_font = pygame.font.Font(None,38)
scrole_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = scrole_numb_font
score_msg = score_font.render('Score : ',1,pygame.Color('green'))
score_msg_size = score_font.size('Score')
background_color = pygame.Color(0,0,0) 
black = pygame.Color(0,0,0)


# for clock at the left corner
gameClock = pygame.time.Clock()

