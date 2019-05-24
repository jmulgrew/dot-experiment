import glob
import yaml
from psychopy import visual, event, core
instruction_done = False

with open('experiment.yml', 'r') as yamlFile:
    config = yaml.load(yamlFile.read())

def instruct():
    instruction_done = True
    return instruction_done

while instruction_done == False:
    win = visual.Window([1280,800],fullscr = True, color = (-1,-1,-1))
    image = visual.ImageStim(win, image = (f'img_stim/set1/intro/dot_058.jpg'))
    image.pos = (0.0,0.0)
    image.size = (0.8,0.8)
    message = visual.TextStim(win, text=config['instructions'][0], pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .09, wrapWidth = 0.7)
    message.draw()
    win.flip()
    key = event.waitKeys(keyList = ['space'])
    if key:
        message = visual.TextStim(win, text=config['instructions'][1], pos = (0.0, -0.6), color = (1.0,1.0,1.0), height = .09, wrapWidth = 0.7)
        image.draw()
        message.draw()
        win.flip()
        key = event.waitKeys(keyList = ['space'])
        if key:
            instruction_done = instruct()
