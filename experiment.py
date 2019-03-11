# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:50:17 2019
@author: Jerrica Mulgrew
"""
import yaml
import pygame
from components import *

with open('experiment.yml', 'r') as yamlFile:
    config = yaml.load(yamlFile.read())

class stim_game:
    def __init__(self,steps):
        # Initialize a game, display, mixer and clock
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_mode((config['w'],config['h']),pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.steps = steps
    def run(self):
        for step in self.steps:
            while not step.done and pygame.KEYDOWN not in [event.type for event in pygame.event.get()]:
                self.clock.tick(config['frame_rate'])
                step.update(pygame)
                pygame.display.update()
            # Step finished & clear events
            pygame.event.clear(pygame.KEYDOWN)
        # Done all steps so quit the game
        pygame.quit()

def main():
    steps = [
        instructions(
            config['instructions'],
            sub_comps = [text(config['instructions']['title']),
                        text(config['instructions']['instruct'])
                        ]),
        stimulus(
            config['stimulus'],
            sub_comps = [audio(config['stimulus']['audio'])] +
                        [fixation(config['stimulus']['fixation'])] +
                        [dot(config['stimulus']['dot']) for i in range(round(config['stimulus']['time']*config['stimulus']['dot']['freq']))])
    ]
    stim_game(steps).run()
    exit()

if __name__ == '__main__':
    main()
