### Dot Experiment Fundamentals & Resources

##### Next steps:
- Fix up/ edit dictionaries that store stimuli information for each section.
  - Master list holds all dictionaries and writes them to CSV at the end of the experiment.
    - Looks messy when trying to load into excel. Need to be able to seperate the values within the dictionaries so they are on their own rows.
    - Also, should probably ditch values that are 0 as they are meaningless. We only care about screen flips that have a value.
  - Currently the dictionary keys are time and val. Time stores the time of each screen flip and val the corresponding stimuli value (e.g., syllable code). 
    - Needs to be able to store PAUSE and RESUME as values as well. We can make up an arbitrary number... e.g., pause = 999... resume = 777
  - Need to add third key "event" to dictionaries (to classify event as stimuli or user input).
- Right now section 3 is showing 900 frames, to represent 15 seconds before audio... this needs to be fixed. It should be 900 frames minus however many frames are in the intro... because the 15 second wait time should include the intro dots.
- Add pyserial to [experiment.yml](https://pyserial.readthedocs.io/en/latest/pyserial.html#requirements).
- Add serial port code that sends value of the audio stimuli (which syllable was presented) and if the critical dot frame appeared with that syllable (add 100 to code).
- Fix timing issues, check to ensure frames are not being dropped.
- Splice naturalistic video into frames, similiar to dot stimuli, for all frequencies.
  - I've added another option in the get input GUI that asks what image set (D for dots, N for natural).
  - I've got code working that can extract frames using openCV but the math/logic for how to get the right amount of images for each frequency needs to be figured out.

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
