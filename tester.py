import yaml
from psychopy import visual, event, core
instruction_done = False

with open('experiment.yml', 'r') as yamlFile:
    config = yaml.load(yamlFile.read())

def instruct():
    instruction_done = True

while instruction_done == False:
    win = visual.Window([1280,800],fullscr = True, color = (-1,-1,-1))
    message = visual.TextStim(win, text=config['instructions'], pos = (0.0, 0.0), color = (1.0,1.0,1.0), height = .09, wrapWidth = None)
    message.draw()
    win.flip()
    event.waitKeys() # this pauses the whole thing and waits for any key press which isn't what i want... but otherwise the text "blinks" every frame refresh
    event.globalKeys.add(key=['k'], func=instruct, name='done')
