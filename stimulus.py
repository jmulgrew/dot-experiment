# Stimulus class
class stimulus:

    def __init__(self,items,render,while_paused=False,manual_next=False):
        self.aoi = items
        self.render = render
        self.pause = pause
        self.resume = resume
        self.next = next

    def expose(self):
        '''Reveals the next item in the array (whether image or sound) as long
        as the experiment is not paused. It then increments the current item
        to continue going through the array.
        '''
        item = self.array[self.curr_item]
        if item is not None:
            if not self.paused or self.while_paused:
                self.render(item)
        if not self.paused and not self.manual_next:
            print(curr_item)
            self.curr_item = (self.curr_item + 1)
        return 0

    def pause(self):
        '''Pauses the experiment according to a key press.
        '''
        self.paused = True

    def resume(self):
        '''Resumes the experiment after a pause, according to a key press.
        '''
        self.paused = False

    def next(self):
        '''Goes to next screen
        '''
        if self.manual_next:
            self.curr_item = (self.curr_item + 1)
