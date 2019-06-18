# -*- coding: utf-8 -*-
"""
Created on Mon Apr 1, 2019
@author: jmulgrew
"""
import glob
import os

import yaml
import pandas as pd
import serial

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

def main():
    user_input = get_input() # get subject  information using the gui
    screen = visual.Window(monitor = "testMonitor", size=[1024,768], fullscr = False, color = (-1.0,-1.0,-1.0)) # set screen
    if False: # if this port does exist (TO-DO)
        port = serial.Serial('COM5', 115200, timeout= 1)
    else:
        port = None
    ############################################################################
    # Exit
    sections = []
    def endexp():
        # Collect & write out dictionaries to csv file
        data = list()
        for s in sections:
            data += s.data
        df = pd.DataFrame(data)
        sub_num = len(glob.glob('sub_files/Subject_*.csv')) + 1
        df.to_csv(f'sub_files/Subject_{sub_num}_{user_input[0]}{user_input[1]}.csv', index = False)
        core.quit()
    event.globalKeys.add(key='q', func=endexp, name='shutdown') # global shutdown
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
    config['instructions'][1]['img'] = config['instructions'][1]['img'].format(f'set{user_input[0]}')
    sections.append(section([create_instructions(config['instructions'])]))
    sections.append(section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/intro/*.jpg')),False),
    ]))
    intro_frames = len(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/intro/*.jpg'))
    sections.append(section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/cycle/*.jpg')),True,frames = (900 - intro_frames)),
    ]))
    sections.append(section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[0]}/set{user_input[1]}/cycle/*.jpg')),True),
        create_sounds(yaml.safe_load(open('audio_stim/audio.yml','r')),open('audio_stim/audio_stim_order.txt','r').read().split(),18),
    ]))
    sections.append(section([create_instructions(config['endscreen'])]))

    ### Run sections
    for s in sections:
        s.run_section(screen,port)
    endexp()

if __name__ == '__main__':
    main()
