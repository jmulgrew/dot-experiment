from psychopy import event

from stimulus import *

class section:

    def __init__(self,stimuli):
        self.stimuli = stimuli
        self.clock = False

    def pause(self):
        for component in self.stimuli:
            component.pause()

    def resume(self):
        for component in self.stimuli:
            component.resume()

    def next(self):
        for component in self.stimuli:
            component.next()

    def run_section(self,screen):
        event.globalKeys.add(key='p', func=self.pause, name='pause')
        event.globalKeys.add(key='r', func=self.resume, name='resume')
        event.globalKeys.add(key='space', func=self.next, name='next')
        while True:
            for stimulus in self.stimuli:
                stimulus.expose()
            screen.flip()
