# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:50:17 2019
@author: Jerrica Mulgrew
"""
import pygame
from pygame.locals import *
from pygame import gfxdraw

# FUNCTIONS
def draw_bg(game, w = 900, h = 600, bg = (255,255,255), fg = (0,0,0), line = 4):
    '''draw_bg
    Draws the background of the animation (horizontal and vertical lines, fixation dot).
    '''
    # draw background
    window_surface.fill(bg)
    # draw lines
    game.draw.line(window_surface, fg,(0,h/2),(w,h/2),line) # horizontal line
    game.draw.line(window_surface, fg,(left_position,0),(left_position,h),line) # vertical line
    # draw fixation dot (always same spot)
    # fg outline
    game.gfxdraw.aacircle(window_surface, left_position, half_height, dot_size, fg)
    game.gfxdraw.filled_circle(window_surface, left_position, half_height, dot_size, fg)
    # bg inner part
    game.gfxdraw.aacircle(window_surface, left_position, half_height, dot_size - line, bg)
    game.gfxdraw.filled_circle(window_surface, left_position, half_height, dot_size - line, bg)

def draw_dots(game,posn, dot_size = 36, cl = (0,0,0)):
    '''draw_dots
    Draws the moving dots.
    '''
    for (x,y) in posn:
        game.gfxdraw.aacircle(window_surface, x, y, dot_size, cl)
        game.gfxdraw.filled_circle(window_surface, x, y, dot_size, cl)

# INTIALIZE VARIABLES
# duration, dot frequency, & frame rate
w,h = 900,600
#freq = 1 # probably going to have user defined freq
freq = float(input("Type in the frequency:"))
frame_rate = 45

# positioning
half_height = int(h/2) # half of the screen height
left_position = 180 # how far the fixation dot should be to the left

# dots
num_dots = 12
dot_space = 180 # space between dots
dot_size = 36 # size of dots

dot_start = [(w+dot_space*i,half_height) for i in range(num_dots)] # starting dot positions
dot_posn = dot_start
times = [None for dot in dot_posn]

# setup animation length
t,t_fin = 0,(num_dots+w/dot_space)/freq

# SET UP PYGAME
pygame.init()
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((w,h),pygame.FULLSCREEN)

# MAIN LOOP
while t <= t_fin and pygame.KEYDOWN not in [event.type for event in pygame.event.get()]:

    # calculate change in time/position
    clock.tick(frame_rate)
    t = pygame.time.get_ticks()/1000
    move = int(freq*dot_space*t)
    dot_posn = [(x - move,half_height) for (x,y) in dot_start]

    # draw new animation
    pygame.display.set_caption(f'Dot Animation: {t}')
    draw_bg(pygame)
    draw_dots(pygame,dot_posn)
    pygame.display.update()

    # temporary, remove later
    for i in range(num_dots):
        if dot_posn[i][0] <= left_position and times[i] is None:
            times[i] = t
# finished
print(times)
exit()
