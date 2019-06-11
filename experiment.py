# -*- coding: utf-8 -*-
"""
Created on Mon Apr 1, 2019
@author: jmulgrew
"""
import glob
import os

import yaml
import numpy as np
import pandas as pd

from psychopy import core, visual, logging, event, gui, prefs
from psychopy.sound import Sound

from section import *
from stimulus import *

prefs.general['audioLib'] = ['pygame']

config = yaml.load(open('experiment.yml', 'r').read(),Loader=yaml.Loader)

def get_input():
    '''Creates a dialogue box to get the condition number and stimuli type. Based on
    this information, the function finds the correct set of images to use.
    '''
    my_gui = gui.DlgFromDict(config['user_input'],order=config['order'])
    if my_gui.OK:
        return my_gui.data
    quit()

def record_data():
    '''Eventually, this function will record data from the experiment, even if "q"
    is pressed and the experiment ends early. It collects and writes out dictionaries
    to a CSV file. The subject number is based on how many files exist in subject folder
    already.
    '''

def main():
    event.globalKeys.add(key='q', func=core.quit, name='shutdown') # global shutdown
    user_input = get_input() # get subject  information using the gui
    screen = visual.Window(monitor = "testMonitor", size=[1024,768], fullscr = True, color = (-1.0,-1.0,-1.0)) # set screen
    ############################################################################
    def do_nothing(stim):
        pass
    ############################################################################
    # instructions
    def create_instructions(instructions):
        def render(stim):
            if stim.done:
                return 0
            else:
                item = stim.items[stim.i]
                for i in item['content']:
                    i.draw()
                return item['value']

        def next(stim):
            if stim.i+1 == len(stim.items):
                stim.done = True
            stim.i += 0 if stim.done else 1

        # Create items
        items = list()
        for instruct in instructions:
            content = list()
            if instruct['text'] and instruct['img']: # second instruction screen
                content.append(visual.TextStim(screen, text=instruct['text'], alignHoriz='center', alignVert='center', pos = (0.0, -0.65), color = (1.0,1.0,1.0), height = .08, wrapWidth = 0.97))
                content.append(visual.ImageStim(screen,image = instruct['img'], pos = (0.0, 0.1), size=(0.85,0.9)))
            else: # first instruction screen
                content.append(visual.TextStim(screen, text=instruct['text'], alignHoriz='center', alignVert='center', pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .08, wrapWidth = 0.97))
            items.append({ 'content': content, 'value': 0})

        return stimulus(items,render,do_nothing,next)
    ############################################################################
    # images
    def create_images(files,repeat,frames = float('inf')):
        def render(stim):
            if stim.done:
                return 0
            else:
                item = stim.items[stim.i%len(stim.items)]
                item['content'].draw()
                return item['value']

        def move(stim,loop=repeat,max_frames = frames):
            if loop and not stim.paused:
                if stim.i+1 >= max_frames and (stim.i+1)%len(stim.items) == 0:
                    stim.done = True
                stim.i += 0 if stim.done else 1

            elif not stim.paused:
                if stim.i+1 == len(stim.items):
                    stim.done = True
                stim.i += 0 if stim.done else 1

        # Create items
        items = [{  'content': visual.ImageStim(screen,image = file),
                    'value': 100 if file == files[0] else 0
                } for file in files]
        return stimulus(items,render,move,do_nothing)
    ############################################################################
    # audio
    def create_sounds(audio_dict,order,freq):
        def render(stim):
            item = stim.items[stim.i]
            if not stim.paused and item is not None:
                item['content'].play()
                return item['value']
            else:
                return 0

        def move(stim):
            if not stim.paused:
                if stim.i+1 == len(stim.items):
                    stim.done = True
                else:
                    stim.i += 1
        # Create items
        items = []
        for k in order:
            items += [{
                'content': Sound(audio_dict['files'][int(k)],secs=0.3),
                'value': int(k)
            }] + [None for i in range(freq-1)]

        return stimulus(items,render,move,do_nothing)
    ############################################################################

    waiting = visual.TextStim(screen, text='Please wait while we prepare the experiment...')
    waiting.draw()
    screen.flip()

    ### Prep Sections ###
    section1 = section([create_instructions(config['instructions'])])
    section2 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/intro/*.jpg')),False),
    ])
    intro_frames = len(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/intro/*.jpg'))
    section3 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/cycle/*.jpg')),True,frames = (900 - intro_frames)),
    ])
    section4 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/cycle/*.jpg')),True),
        create_sounds(yaml.safe_load(open('audio_stim/audio.yml','r')),open('audio_stim/audio_stim_order.txt','r').read().split(),18),
    ])

    ### Run sections

    # Section 1: INSTRUCTIONS
    section1.run_section(screen)

    # Section 2: INTRO ANIMATION
    section2.run_section(screen)

    # Section 3: CYCLE IMAGES WITHOUT AUDIO
    section3.run_section(screen)

    # Section 4: CYCLE IMAGES WITH AUDIO
    section4.run_section(screen)

    # Collect & write out dictionaries to csv file
    data = list()
    data += section1.data
    data += section2.data
    data += section3.data
    data += section4.data
    df = pd.DataFrame(data)
    sub_num = len(glob.glob('sub_files/Subject_*.csv')) + 1
    df.to_csv(f'sub_files/Subject_{sub_num}_{user_input[0]}{user_input[1]}.csv', index = False)

if __name__ == '__main__':
    main()
