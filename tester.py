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
    message = visual.TextStim(win, text=config['instructions'], pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .09, wrapWidth = None)
    message.draw()
    win.flip()
    key = event.waitKeys(keyList = ['space'])
    if key:
        message = visual.TextStim(win, text=config['instructions2'], pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .09, wrapWidth = None)
        message.draw()
        win.flip()
        key = event.waitKeys(keyList = ['space'])
        if key:
            instruction_done = instruct()
