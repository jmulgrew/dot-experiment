# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:53:18 2019
@author: jmulgrew
"""
import os
import glob
import yaml
from psychopy import prefs,core,event,visual, gui
prefs.general['audioLib'] = ['pygame']
from psychopy.sound import Sound

from stimulus import *

def render_image(image):
    image.draw()

def render_sound(sound):
    sound.play()

def pause(loc):
    for component in loc:
        component.pause()

def resume(loc):
    for component in loc:
        component.resume()

def get_info():
    # dialogue box to get experiment info
    my_gui = gui.Dlg(title = "Subject Information", screen =-1)
    my_gui.addField('Subject ID:')
    my_gui.addField('Condition Number:', choices = ["1","2","3"])
    ok_data = my_gui.show()

    if my_gui.OK: # user has hit OK..
        subj_id = my_gui.data[0]
        condition = int(my_gui.data[1])
        # figure out what condition was selected and pick corresponding imgs
        if condition == 1:
            filenames = glob.glob('img_stim/set1/dot-to-dot/*.jpg')
        elif condition == 2:
            filenames = glob.glob('img_stim/set2/dot-to-dot/*.jpg')
        else:
            filenames = glob.glob('img_stim/set3/dot-to-dot/*.jpg')
        return filenames
    else: # user has hit cancel...
        quit()

def instructions(screen):
    instruct = visual.TextStim(screen, text = "Welcome to the experiment.", color = (255,255,255), pos = (0,0))
    instruct.draw()
    screen.flip()
    instructions = False
    return instructions

def main():
    filenames = get_info()
    screen = visual.Window(monitor = "testMonitor", fullscr = True, rgb=(-1,-1,-1))
    clock = core.Clock()

    # sort images
    images = [visual.ImageStim(screen, image = file) for file in sorted(filenames)] # list comprehension for each image file

    # sounds
    order = open('audio_stim/audio_stim_order.txt','r').read()
    audio_dict = yaml.safe_load(open('audio_stim/audio.yml','r'))
    sound_files = [audio_dict['files'][int(k)] for k in order.split()]
    sounds = [Sound(file,secs=0.3) for file in sound_files]
    audio = []
    for sound in sounds:
        audio += [sound] + [None for i in range(17)]

    components = [stimulus(images,render_image,while_paused=True),stimulus(audio,render_sound)]
    event.globalKeys.add(key='q', func=core.quit, name='shutdown')
    event.globalKeys.add(key='p', func=pause, func_args=[components], name='pause')
    event.globalKeys.add(key='r', func=resume, func_args=[components], name='resume')

    while True:
        for component in components:
            component.expose()
        screen.flip()

if __name__ == '__main__':
    main()
