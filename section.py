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
            
    def run_section(self,screen):
        event.globalKeys.add(key='p',       func=self.pause,    name='pause')
        event.globalKeys.add(key='r',       func=self.resume,   name='resume')
        event.globalKeys.add(key='space',   func=self.space,    name='space')

        new_dict = {}
        new_dict["time"] = []
        new_dict["val"] = []
        timer = core.Clock()

        done = False
        while not done:
            total  = sum([stimulus.expose() for stimulus in self.stimuli])
            done = sum([stimulus.done for stimulus in self.stimuli]) > 0
            screen.flip()
            new_dict["time"].append(timer.getTime())
            new_dict["val"].append(total)

        event.globalKeys.remove(key='p')
        event.globalKeys.remove(key='r')
        event.globalKeys.remove(key='space')

        return new_dict
