# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:53:18 2019
@author: jmulgrew
"""
import os
import glob
from psychopy import core,event,visual
from stimulus import *

def render_image(image):
    image.draw()
    screen.flip()

def main():
    screen = visual.Window([1024,576], monitor = "testMonitor", fullscr = True)
    clock = core.Clock()
    # list comprehension for each image file
    filenames = glob.glob('imgs/dotSets/secondSet/*.jpg')
    images = [visual.ImageStim(screen, image = file) for file in sorted(filenames)]
    event.globalKeys.add(key='q', func=core.quit, name='shutdown')

    while True:
        components = [stimulus(images,render_image)]
        for component in components:
            component.expose()

if __name__ == '__main__':
    main()



#
#
# # set screen
# screen = visual.Window([1024,576], monitor = "testMonitor", fullscr = True)
# # import images (these are not the actual images, these are just for now)
# clock = core.Clock()
# # list comprehension for each image file
# filenames = glob.glob('imgs/dotSets/secondSet/*.jpg')
# images = [visual.ImageStim(screen, image = file) for file in sorted(filenames)]
#
# event.globalKeys.add(key='q', func=core.quit, name='shutdown')
# paused = False
#
# # need to pause if p pressed
# # also needs to figure out at which frame and/or sylable it was paused at
# def pause():
#     pause = not(pause)
# event.globalKeys.add(key='p', func=pause, name='pause/play')
#
# # loop through images
# for image in images:
#     image.draw()
#     screen.flip()
#     core.wait(0.1) # just for testing purposes
# core.quit()
