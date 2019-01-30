# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:50:17 2019

@author: Jerrica Mulgrew
"""

import pygame
from pygame.locals import *
from pygame import gfxdraw

# SET UP PYGAME
pygame.init()

# SET UP THE WINDOW
window_width = 900
window_height = 600
window_surface = pygame.display.set_mode((window_width,window_height),0,32)
pygame.display.set_caption('Dot Animation')

# SET UP COLOURS
BLACK = (0,0,0)
WHITE = (255,255,255)

# INTIALIZE VARIABLES
clock = pygame.time.Clock()
half_height = 300 # half of the screen height (center)
left_position = 180 # how far the fixation dot should be to the left
dot_move = window_width # dot movement (starts off the screen at 900 pixels)
dot_space = 200 # space between dots
dot_size = 40 # size of dots

# DRAW BACKGROUND
window_surface.fill(WHITE)

# MAIN LOOP
running = True

while running:
    # check input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update position
    dot_move -= 1

    # draw background
    window_surface.fill(WHITE)

    # draw lines
    pygame.draw.line(window_surface, BLACK,(0,window_height/2),(window_width,window_height/2),4) # horizontal line
    pygame.draw.line(window_surface, BLACK,(left_position,0),(left_position,window_height),4) # vertical line

    # draw fixation dot (always same spot)
    # black outline
    pygame.gfxdraw.aacircle(window_surface, left_position, half_height, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, left_position, half_height, dot_size, BLACK)
    # white inner part
    pygame.gfxdraw.aacircle(window_surface, left_position, half_height, 36, WHITE)
    pygame.gfxdraw.filled_circle(window_surface, left_position, half_height, 36, WHITE)

    # draw moving dots
    # moving dot 1
    pygame.gfxdraw.aacircle(window_surface, dot_move, half_height, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, dot_move, half_height, dot_size, BLACK)
    # moving dot 2
    pygame.gfxdraw.aacircle(window_surface, dot_move+dot_space, half_height, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, dot_move+dot_space, half_height, dot_size, BLACK)
    # moving dot 3
    pygame.gfxdraw.aacircle(window_surface, dot_move+(dot_space*2), v, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, dot_move+(dot_space*2), half_height, dot_size, BLACK)
    # moving dot 4
    pygame.gfxdraw.aacircle(window_surface, dot_move+(dot_space*3), half_height, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, dot_move+(dot_space*3), half_height, dot_size, BLACK)
    # moving dot 5
    pygame.gfxdraw.aacircle(window_surface, dot_move+(dot_space*4), half_height, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, dot_move+(dot_space*4), half_height, dot_size, BLACK)
    # moving dot 6
    pygame.gfxdraw.aacircle(window_surface, dot_move+(dot_space*5), half_height, dot_size, BLACK)
    pygame.gfxdraw.filled_circle(window_surface, dot_move+(dot_space*5), half_height, dot_size, BLACK)

    # update the screen
    pygame.display.update()

    # here I want to save picture

    # limit to 30 frames per second
    clock.tick(30)

    # three things to figure out
    # how long do you want the animation to go for
    t = 60
    # how fast the dots move (dots per second) - Hz (3 levels)
    hertz = [1.5,1,0.75]
    # how often do i want to take screenshots? what's the frame rate?
    frame_rate = 30
