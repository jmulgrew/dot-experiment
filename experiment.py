# -*- coding: utf-8 -*-
"""
Created on Mon Apr 1, 2019
@author: jmulgrew
"""
import glob
import os
import csv

import yaml
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
    screen = visual.Window(monitor = "testMonitor", size = [800, 450], fullscr = False, color = (-1.0,-1.0,-1.0)) # set screen
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
                content.append(visual.TextStim(screen, text=instruct['text'], pos = (0.0, -0.6), color = (1.0,1.0,1.0), height = .09, wrapWidth = None))
                content.append(visual.ImageStim(screen,image = instruct['img'], pos = (0.0, 0.0), size=(0.8,0.8)))
            else: # first instruction screen
                content.append(visual.TextStim(screen, text=instruct['text'], pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .09, wrapWidth = None))
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
        create_images(sorted(glob.glob(f'img_stim/set{user_input[1]}/intro/*.jpg')),False),
    ])
    section3 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[1]}/dot-to-dot/*.jpg')),True,frames = 900),
    ])
    section4 = section([
        create_images(sorted(glob.glob(f'img_stim/set{user_input[1]}/dot-to-dot/*.jpg')),True),
        create_sounds(yaml.safe_load(open('audio_stim/audio.yml','r')),open('audio_stim/audio_stim_order.txt','r').read().split(),18),
    ])

    ### Run sections
    keyList = ["Sec2","Sec3","Sec4"]
    d = {key: None for key in keyList}

    section1.run_section(screen)
    # screen.recordFrameI ntervals = True
    # screen.refreshThreshold = 1/60 + 0.004 # based on 60hz refresh
    # logging.console.setLevel(logging.WARNING)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    sec2_dict = section2.run_section(screen)
    d.update(Sec2 = sec2_dict)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    sec3_dict = section3.run_section(screen)
    d.update(Sec3 = sec3_dict)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    sec4_dict = section4.run_section(screen)
    d.update(Sec4 = sec4_dict)
    # print('Overall, %i frames were dropped.' % screen.nDroppedFrames)

    # write out dictionaries to csv file
    with open('testdict.csv','w') as f:
        for key in d.keys():
            f.write("%s,%s\n"%(key,d[key]))
    f.close()
    print(d)

if __name__ == '__main__':
    main()
