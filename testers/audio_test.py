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
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 2)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))

test_sound = pygame.mixer.Sound("ba.wav")

# SHOW INSTRUCTIONS
while pygame.KEYDOWN not in [event.type for event in pygame.event.get()]:
    screen.fill(BLACK)
    pygame.mixer.Sound.play(test_sound)
    clock.tick(60)

pygame.quit()
exit()
