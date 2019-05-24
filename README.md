### Dot Experiment Fundamentals & Resources

##### Next steps:
- Add dictionaries that store stimuli information for each section.
  - Master dictionary will contain dictionaries for each section.
  - Each dictionary will have two or three keys (tbd): Time, Event, Value...
    -  Values for the keys will be time according to core.clock, event type (stimuli or user), and then corresponding value (e.g., syllable codes). Needs to be able to store pause and resume as values. We can make up an arbitrary number... e.g., pause = 999... resume = 777
  - This should be written to a csv file at the end of the experiment, with the subject number, img stimulus type (nat or dot), and condition number as the filename.
      - E.g., "Subject_1_N1" "Subject_2_D1" "Subject_3_N2" "Subject_4_D2", etc.
- Right now section 3 is showing 900 frames, to represent 15 seconds before audio... this needs to be fixed. It should actually be 900 frames minus however many frames are in the intro... because the intro dots count into that 15 second time window.
- Add pyserial to [experiment.yml](https://pyserial.readthedocs.io/en/latest/pyserial.html#requirements).
- Add serial port code that sends value of the audio stimuli (which syllable was presented) and if the critical dot frame appeared with that syllable (add 100 to code).
- Fix timing issues, check to ensure frames are not being dropped.
- Find video for "naturalistic" visual stimuli presentation.
  - Splice video into frames similar to dot stimuli, for all frequencies.
  - Add images to img stim folder.  

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
