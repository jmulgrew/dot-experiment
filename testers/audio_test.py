# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:03:39 2019

@author: jerrica
"""

import pygame
from pygame.locals import *
from pygame import gfxdraw

# INTIALIZE VARIABLES
w,h = 900,600
BLACK = (0,0,0)
WHITE = (255,255,255)

# SET UP PYGAME
#pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))

test_sound = pygame.mixer.Sound('../audio_stim/jay.wav') # dot dot makes you go up one folder (bc not in parent folder)

# SHOW INSTRUCTIONS
for i in range(5):
    pygame.mixer.Sound.play(test_sound)
    while pygame.mixer.get_busy():
        clock.tick(45)
pygame.quit()
exit()
