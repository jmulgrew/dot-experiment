# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:53:18 2019
@author: jmulgrew
"""
import glob
import os

import yaml
from psychopy import core, event, gui, prefs, visual
from psychopy.sound import Sound

from stimulus import *
from section import *

prefs.general['audioLib'] = ['pygame']

with open('experiment.yml', 'r') as yamlFile:
    config = yaml.load(yamlFile.read())

def render_draw(image):
    image.draw()

def render_sound(sound):
    sound.play()

def get_info():
    '''Creates a dialogue box to get the subject number and to choose the
    condition that will be run. Based on the condition specified, the
    function finds the correct set of dot images to use.
    '''
    my_gui = gui.DlgFromDict(config['user_input'],order=config['order'])
    if my_gui.OK:
        return my_gui.data
    quit()

def main():
    event.globalKeys.add(key='q', func=core.quit, name='shutdown')
    user_input = get_info()
    screen = visual.Window(monitor = "testMonitor", fullscr = True, rgb=(-1,-1,-1))

    los = list()
    ###Section 1###
    messages = [visual.TextStim(screen, text=instruction, pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .09, wrapWidth = None) for instruction in config['instructions']]
    los.append(section([stimulus(messages,render_draw,while_paused=True,manual_next=True)]))

    ###Section 2###
    # sort images
    images = [visual.ImageStim(screen, image = file) for file in sorted(glob.glob(f'img_stim/set{user_input[1]}/dot-to-dot/*.jpg'))] # list comprehension for each image file
    # sounds
    order = open('audio_stim/audio_stim_order.txt','r').read().split()
    audio_dict = yaml.safe_load(open('audio_stim/audio.yml','r'))
    sounds = [Sound(file,secs=0.3) for file in [audio_dict['files'][int(k)] for k in order]]
    audio = []
    for sound in sounds:
        audio += [sound] + [None for i in range(17)]

    los.append(section([stimulus(images,render_draw,while_paused=True,manual_next=True),stimulus(audio,render_sound,manual_next=True)]))

    clock = core.Clock()
    for sect in los:
        sect.run_section(screen)

if __name__ == '__main__':
    main()
