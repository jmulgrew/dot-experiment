# Stimulus class
class stimulus:

    def __init__(self,array,render):
        self.array = array
        self.render = render
        self.curr_item = 0
        self.paused = False

    def expose(self):
        if not self.paused:
            item = self.array[self.curr_item]
            self.curr_item += 1
            if item is not None:
                self.render(item)
        return 0

    def pause(self):
        '''Pauses the experiment according to a key press.
        '''
        self.paused = True

    def resume(self):
        '''Resumes the experiment after a pause, according to a key press.
        '''
        self.paused = False
