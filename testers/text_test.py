import pygame
import ptext
from pygame.locals import *
from pygame import gfxdraw

# INTIALIZE VARIABLES
w,h = 900,600
BLACK = (0,0,0)
WHITE = (255,255,255)
instructions = """In this experiment you will listen to a language made up of nonsense words.\nPlease pay attention and listen carefully.\nLater in the experiment you will be tested on the words that you have learned.\n\nPress any key to start the experiment."""

# SET UP PYGAME
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))

# SHOW INSTRUCTIONS
while pygame.KEYDOWN not in [event.type for event in pygame.event.get()]:
    screen.fill(BLACK)
    ptext.draw(instructions, centerx = 450, centery = 300, align = "center", lineheight = 1.5, color = WHITE, fontsize = 32, sysfontname ="Helvetica")
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
