# Stimulus class
class stimulus:

    def __init__(self,array,render,while_paused=False):
        self.array = array
        self.render = render
        self.curr_item = 0
        self.paused = False
        self.while_paused = while_paused

    def expose(self):
        '''Reveals the next item in the array (whether image or sound) as long
        as the experiment is not paused. It then increments the current item
        to continue going through the array.
        '''
        item = self.array[self.curr_item]
        if item is not None:
            if not self.paused or self.while_paused:
                self.render(item)
        if not self.paused:
            self.curr_item = (self.curr_item + 1) % len(self.array)
        return 0

    def pause(self):
        '''Pauses the experiment according to a key press.
        '''
        self.paused = True

    def resume(self):
        '''Resumes the experiment after a pause, according to a key press.
        '''
        self.paused = False
