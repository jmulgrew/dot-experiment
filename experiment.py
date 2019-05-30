# -*- coding: utf-8 -*-
"""
Created on Mon Apr 1, 2019
@author: jmulgrew
"""
import glob
import os

import csv
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
    '''Creates a dialogue box to get the subject number and to choose the
    condition that will be run. Based on the condition specified, the
    function finds the correct set of dot images to use.
    '''
    my_gui = gui.DlgFromDict(config['user_input'],order=config['order'])
    if my_gui.OK:
        return my_gui.data
    quit()

def main():
    event.globalKeys.add(key='q', func=core.quit, name='shutdown') # global shutdown
    user_input = get_input() # get subject  information using the gui
    screen = visual.Window(monitor = "testMonitor", size = [800, 450], fullscr = True, color = (-1.0,-1.0,-1.0)) # set screen
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
    # figure out number of intro frames based on condition selected
    if user_input[2] == 1:
        intro_frames = 375
    elif user_input[2] == 2:
        intro_frames = 281
    else:
        intro_frames = 188

    waiting = visual.TextStim(screen, text='Please wait while we prepare the experiment...')
    waiting.draw()
    screen.flip()

    ### Prep Sections ###
    section1 = section([create_instructions(config['instructions'])])
    section2 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[1]}/set{user_input[2]}/intro/*.jpg')),False),
    ])
    section3 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[1]}/set{user_input[2]}/dot-to-dot/*.jpg')),True,frames = (900 - intro_frames)),
    ])
    section4 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[1]}/set{user_input[2]}/dot-to-dot/*.jpg')),True),
        create_sounds(yaml.safe_load(open('audio_stim/audio.yml','r')),open('audio_stim/audio_stim_order.txt','r').read().split(),18),
    ])

    ### Run sections
    # create a master list for dictionaries
    dict_list = []

    # Section 1: INSTRUCTIONS
    section1.run_section(screen)
    # screen.recordFrameIntervals = True
    # screen.refreshThreshold = 1/60 + 0.004 # based on 60hz refresh
    # logging.console.setLevel(logging.WARNING)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    # Section 2: INTRO DOTS
    sec2_dict = section2.run_section(screen)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    # Section 3: DOT-TO-DOT IMAGES WITHOUT AUDIO
    sec3_dict = section3.run_section(screen)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    # Section 4: DOT-TO-DOT IMAGES WITH AUDIO
    sec4_dict = section4.run_section(screen)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    dict_list.append(sec2_dict)
    dict_list.append(sec3_dict)
    dict_list.append(sec4_dict)

    # write out dictionaries to csv file
    final_dict = {}
    for list_item in dict_list:
        for key, value in list_item.items():
            if key in list(final_dict):
                for entry in value:
                    final_dict[key].append(entry)
            else:
                final_dict[key] = value
    df = pd.DataFrame.from_dict(final_dict)
    df = df[df.val != 0] # we only want to look at frames where something occurred (not zero)
    df.to_csv(f'sub_files/Subject_{user_input[0]}_{user_input[1]}{user_input[2]}.csv', index_label = 'frame')

if __name__ == '__main__':
    main()
