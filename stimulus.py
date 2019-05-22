# Stimulus class
class stimulus:

    def __init__(self,items,render,move,next):
        self.items = items
        self.render = render
        self.move = move
        self.next = next

        self.i = 0
        self.paused = False
        self.done = False

    def expose(self):
        '''Reveals the next item in the array (whether image or sound) as long
        as the experiment is not paused.
        '''
        val = self.render(self)
        self.move(self)
        return val

    def pause(self):
        '''Pauses the experiment according to a key press.
        '''
        self.paused = True

    def resume(self):
        '''Resumes the experiment after a pause, according to a key press.
        '''
        self.paused = False

    def space(self):
        '''Manually go to next screen
        '''
        self.next(self)
