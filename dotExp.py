# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:50:17 2019

@author: Jerrica Mulgrew
"""

import pygame
from pygame.locals import *
from pygame import gfxdraw

# set up pygame
pygame.init()

# set up the window
windowWidth = 900
windowHeight = 600
windowSurface = pygame.display.set_mode((windowWidth,windowHeight),0,32)
pygame.display.set_caption('Dot Exp')

# set up the colours
BLACK = (0,0,0)
WHITE = (255,255,255)

# draw the white background onto the surface
windowSurface.fill(WHITE)

# intialize  variables
clock = pygame.time.Clock()
x = windowWidth
y = 300
distance = 200
# main loop
running = True

while running:
    # check input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update position
    x -= 1

    # draw stuff
    windowSurface.fill(WHITE)

    # draw lines
    pygame.draw.line(windowSurface, BLACK,(0,windowHeight/2),(windowWidth,windowHeight/2),4) # horizontal line
    pygame.draw.line(windowSurface, BLACK,(windowWidth/5,0),(windowWidth/5,windowHeight),4) # vertical line

    # draw fixation dot
    pygame.gfxdraw.aacircle(windowSurface, 180, 300, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, 180, 300, 40, BLACK)
    pygame.gfxdraw.aacircle(windowSurface, 180, 300, 36, WHITE)
    pygame.gfxdraw.filled_circle(windowSurface, 180, 300, 36, WHITE)

    # moving dot 1
    pygame.gfxdraw.aacircle(windowSurface, x, y, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, x, y, 40, BLACK)
    # moving dot 2
    pygame.gfxdraw.aacircle(windowSurface, x+distance, y, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, x+distance, y, 40, BLACK)
    # moving dot 3
    pygame.gfxdraw.aacircle(windowSurface, x+(distance*2), y, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, x+(distance*2), y, 40, BLACK)
    # moving dot 4
    pygame.gfxdraw.aacircle(windowSurface, x+(distance*3), y, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, x+(distance*3), y, 40, BLACK)
    # moving dot 5
    pygame.gfxdraw.aacircle(windowSurface, x+(distance*4), y, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, x+(distance*4), y, 40, BLACK)
    # moving dot 6
    pygame.gfxdraw.aacircle(windowSurface, x+(distance*5), y, 40, BLACK)
    pygame.gfxdraw.filled_circle(windowSurface, x+(distance*5), y, 40, BLACK)

    # update the screen
    pygame.display.update()

    # here I want to save picture

    # limit to 30 frames per second
    clock.tick(30)

    # three things to figure out
    # how long do you want the animation to go for
    t = 60
    # how fast the dots move (dots per second) - Hz (3 levels)
    hertz = 2.4
    # how often do i want to take screenshots? what's the frame rate?
    frame_rate = 30
