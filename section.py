from psychopy import event, core

from stimulus import *

class section:

    def __init__(self,stimuli):
        self.stimuli = stimuli

    def pause(self):
        for component in self.stimuli:
            component.pause()

    def resume(self):
        for component in self.stimuli:
            component.resume()

    def space(self):
        for stim in self.stimuli:
            stim.space()

    def run_section(self,screen,d):
        event.globalKeys.add(key='p',       func=self.pause,    name='pause')
        event.globalKeys.add(key='r',       func=self.resume,   name='resume')
        event.globalKeys.add(key='space',   func=self.space,    name='space')
        # timer = core.Clock()

        done = False
        while not done:
            total  = sum([stimulus.expose() for stimulus in self.stimuli])
            # d[timer.getTime()] = total.val
            done = sum([stimulus.done for stimulus in self.stimuli]) > 0
            screen.flip()

        # return d

        event.globalKeys.remove(key='p')
        event.globalKeys.remove(key='r')
        event.globalKeys.remove(key='space')
