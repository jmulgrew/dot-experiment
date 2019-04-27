from queue import Queue
import ptext
from pygame.locals import *
from pygame import gfxdraw

# Instructions
class instructions:
    def __init__(self,config,sub_comps=[]):
        self.done = False
        self.t0 = None
        self.t = None
        # Unpack config
        self.clr = config['clr']
        # Attach components
        self.components = sub_comps

    def update(self,game):
        '''Draws the instruction screen
        '''
        t = game.time.get_ticks()/1000
        self.t0 = t if not self.t0 else self.t0
        self.t = t - self.t0
        # Update display
        game.display.get_surface().fill(self.clr)
        # Set status
        self.status = {}
        # Update components
        for component in self.components:
            component.update(game)

    def status():
        return self.status

class text:
    def __init__(self,config,sub_comps=[]):
        self.t0 = None
        self.t = None
        self.text = config['text']
        self.clr = config['clr']
        self.fontsize = config['fontsize']
        self.rel_w = config['rel_w']
        self.rel_h = config['rel_h']
        # Attach components
        self.components = sub_comps

    def update(self,game):
        t = game.time.get_ticks()/1000
        self.t0 = t if not self.t0 else self.t0
        self.t = t - self.t0
        # Update display
        w,h = game.display.get_surface().get_size()
        ptext.draw( self.text,
                    centerx = w*self.rel_w,
                    centery = h*self.rel_h,
                    width = w,
                    align = "center",
                    lineheight = 1.5,
                    color = self.clr,
                    fontsize = self.fontsize ,
                    sysfontname ="Helvetica")
        # Set status
        self.status = {}
        for component in self.components:
            component.update(game)
    def status():
        return self.status

# Stimulus
class stimulus:
    def __init__(self,config,sub_comps=[]):
        self.done = False
        self.t0 = None
        self.t = None
        # Unpack config
        self.time = config['time']
        self.clr = config['clr']
        # Attach components
        self.components = sub_comps
    # Main functionality
    def update(self,game):
        t = game.time.get_ticks()/1000
        self.t0 = t if not self.t0 else self.t0
        self.t = t - self.t0
        # Update display
        game.display.get_surface().fill(self.clr)
        # Set status
        self.status = {}
        # Update components
        for component in self.components:
            component.update(game)

        # Check if step is done
        self.done = False if t < self.time else True

    def status():
        return self.status

class fixation:
    def __init__(self,config,sub_comps=[]):
        # fixation start time
        self.t0 = None
        self.t = None
        # Dot attributes
        self.clr =  config['clr']
        self.bg = config['bg']
        self.rel_h = config['rel_h']
        self.rel_w = config['rel_w']
        self.dot_size = config['dot_size']
        self.line_width = config['line_width']
        # Attach components
        self.components = sub_comps

    def update(self,game):
        t = game.time.get_ticks()/1000
        self.t0 = t if not self.t0 else self.t0
        self.t = t - self.t0
        # Update dipslay
        surface = game.display.get_surface()
        w,h = game.display.get_surface().get_size()
        self.x = round(w*self.rel_w)
        self.y = round(h*self.rel_h)
        game.draw.line(surface,self.clr,(0,self.y),(w,self.y),self.line_width)
        game.draw.line(surface,self.clr,(self.x,0),(self.x,h),self.line_width)
        # draw fixation dot
        game.gfxdraw.aacircle(surface,self.x,self.y,self.dot_size,self.clr)
        game.gfxdraw.filled_circle(surface,self.x,self.y,self.dot_size,self.clr)
        # bg inner part
        game.gfxdraw.aacircle(surface,self.x,self.y,self.dot_size-self.line_width,self.bg)
        game.gfxdraw.filled_circle(surface,self.x,self.y,self.dot_size-self.line_width,self.bg)
        # Set status
        self.status = {}
        # Update components
        for component in self.components:
            component.update(game)

    def status():
        return self.status

class dot:
    num = 0
    def __init__(self,config,sub_comps=[]):
        # Times
        self.t0 = None
        self.t = None
        # Attributes
        dot.num += 1
        self.n = dot.num
        # Config Attributes
        self.r = config['r']
        self.clr =  config['clr']
        self.rel_h = config['rel_h']
        self.spacing = config['spacing']
        self.freq = eval(config['freq'])
        # Attach components
        self.components = sub_comps


    def update(self,game):
        '''
        Draws the moving dots if within the display
        '''
        t = game.time.get_ticks()/1000
        self.t0 = t if not self.t0 else self.t0
        self.t = t - self.t0
        # Get display size & dot position
        w,h = game.display.get_surface().get_size()
        self.x,self.y = self.dot_posn(game)
        # Draw the dot only if it exists on the screen
        if self.x in range(-self.r,w+self.r) and self.y in range(-self.r,h+self.r):
            surface = game.display.get_surface()
            game.gfxdraw.aacircle(surface, self.x, self.y, self.r, self.clr)
            game.gfxdraw.filled_circle(surface, self.x, self.y, self.r, self.clr)
        # Set status
        self.status = {}
        # Update components
        for component in self.components:
            component.update(game)

    def dot_posn(self,game):
        w,h = game.display.get_surface().get_size()
        x = round(w + self.spacing*(self.n-self.freq*self.t))
        y = round(self.rel_h*h)
        return (x,y)

    def status():
        return self.status

class audio:
    def __init__(self,config,sub_comps=[]):
        self.t0 = None
        self.t = None
        self.played = 0
        self.next_sound = 0
        # Unpack config
        self.stim_file = config['stim_file']
        self.stim_size = config['stim_size']
        self.stim_freq = config['stim_freq']
        self.files = config['files']
        # Attach components
        self.components = sub_comps


        with open(self.stim_file, 'r') as stim_order:
            data = list(map(int,stim_order.read().split()))
        self.stim_group = [data[x:x+self.stim_size] for x in range(0, len(data), self.stim_size)]
        self.audio_q = Queue()

    def update(self,game):
        t = game.time.get_ticks()/1000
        self.t0 = t if not self.t0 else self.t0
        self.t = t - self.t0
        # Update audio
        if min(self.t*self.stim_freq,len(self.stim_group)) >= self.played:
            self.played += 1
            for k in self.stim_group[self.played]:
                self.audio_q.put({'sound_n': self.played, 'sound': game.mixer.Sound(self.files[k])})
        # Play audio
        if not game.mixer.get_busy() and not self.audio_q.empty():
            sound = self.audio_q.get()
            sound['sound'].play()
            self.status = {'audio_time': self.t, 'sound_n': sound['sound_n']}
        else:
            self.status = {}
        for component in self.components:
            component.update(game)

    def status():
        return self.status

# class logfile:
# what it needs to do: write critical dot times, every third audio onset time and syllable identity, subject number?
    # logfile = {}
    # def get_time(game)
        #for i in range(num_dots):
            #if dot_posn[i][0] <= left_position and times[i] is None:
            # times[i] = t
            # logfile[?,1] = self.t ???
    # write the dot times to csv file
    #def write_time(game)
        #with open('time_list.csv', 'w') as f:
            #for key in time_dict.keys():
                #f.write("%s,%s\n"%(key,time_dict[key]))
