from psychopy import event, core

from stimulus import *

class section:
    global_timer = core.Clock()
    section_timer = core.Clock()
    num = 0

    def __init__(self,stimuli):
        section.num += 1
        self.section_num = section.num
        self.stimuli = stimuli
        self.frame = 0
        self.data = []

    def pause(self):
        for component in self.stimuli:
            component.pause()
        self.data.append({
            'global_time': section.global_timer.getTime(),
            'section_time': section.section_timer.getTime(),
            'section_id': self.section_num,
            'frame': self.frame,
            'type': 'pause',
            'val': 98,
            })

    def resume(self):
        for component in self.stimuli:
            component.resume()
        self.data.append({
            'global_time': section.global_timer.getTime(),
            'section_time': section.section_timer.getTime(),
            'section_id': self.section_num,
            'frame': self.frame,
            'type': 'resume',
            'val': 99,
            })

    def space(self):
        for stim in self.stimuli:
            stim.space()
        self.data.append({
            'global_time': section.global_timer.getTime(),
            'section_time': section.section_timer.getTime(),
            'section_id': self.section_num,
            'frame': self.frame,
            'type': 'space',
            'val': 97,
            })

    def run_section(self,screen,port):
        section.section_timer.reset()
        event.globalKeys.add(key='p',       func=self.pause,    name='pause')
        event.globalKeys.add(key='r',       func=self.resume,   name='resume')
        event.globalKeys.add(key='space',   func=self.space,    name='space')

        done = False
        while not done:
            self.frame += 1
            total  = sum([stimulus.expose() for stimulus in self.stimuli])
            done = sum([stimulus.done for stimulus in self.stimuli]) > 0
            screen.flip()
            if total != 0:
                self.data.append({
                    'global_time': section.global_timer.getTime(),
                    'section_time': section.section_timer.getTime(),
                    'section_id': self.section_num,
                    'frame': self.frame,
                    'type': 'frame',
                    'val': total,
                    })
                if port:
                    port.write({total})

        event.globalKeys.remove(key='p')
        event.globalKeys.remove(key='r')
        event.globalKeys.remove(key='space')
