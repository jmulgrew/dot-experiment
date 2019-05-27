### Dot Experiment Fundamentals & Resources

##### Important Info:
- Given a refresh rate of 16.667 (CRT monitor), we can present 60 images every second.
- Our syllable rate is 3.3 Hz, or 1.1 Hz per word. So we will present a syllable every 18 images (which should be every 300ms).
- Code will be run on a PC.
- Communication with EEG is USB-to-serial port [(exact info here)](https://www.biosemi.com/faq/USB%20Trigger%20interface%20cable.htm).

##### My Frequencies:
- "0.75 Hz" (4 syllable units): condition/image set 1
- "1 Hz" (3 syllable units): condition/image set 2
- "1.5 Hz" (2 syllable units): condition/image set 3

##### Resources:
- [Information on Timing](https://www.psychopy.org/general/timing/timing.html)
- [Images](https://www.psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim)
- [Text](https://www.psychopy.org/api/visual/textbox.html#psychopy.visual.TextBox)
- [Windows](https://www.psychopy.org/api/visual/window.html#psychopy.visual.Window)
- [Core Functions](https://www.psychopy.org/api/core.html)
- [Sound](https://www.psychopy.org/api/sound.html)
- [Pause/Quit: Global Key Events](https://www.psychopy.org/coder/globalKeys.html#adding-a-global-event-key-simple)
- [Sending Triggers with Serial Port](https://pyserial.readthedocs.io/en/latest/)
- [Storing Data](https://www.psychopy.org/api/data.html)
