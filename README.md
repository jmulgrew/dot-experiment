### Dot Experiment Fundamentals & Resources

##### Next steps:
- ~~Make dot animation continuous~~
- ~~Add instruction screen before main loop~~
- ~~Implement auditory stimuli~~
- Send triggers from program to EEG to time lock stimulus presentation
- Be able to analyze all dot times + audio stimuli presentations to ensure correct frequency
- Find video for "naturalistic" visual stimuli presentation
  - How to implement video in python?
  - How will we track the frequency of water drops
- ~~Be able to input the frequency?~~
- ~~Set up background as fullscreen black window (animation will be in smaller white box)~~

##### Important Info:
- Monitor will be a CRT monitor
- Code will be run on a PC
- Communication with EEG is USB-to-serial port [(exact info here)](https://www.biosemi.com/faq/USB%20Trigger%20interface%20cable.htm)

##### My Frequencies:
- 1.5 Hz (2 syllable units)
- 1 Hz (3 syllable units) **Apparently this is more like 1.1 Hz**
- 0.75 Hz (4 syllable units)

##### Resources:
- [pygame documentation](https://www.pygame.org/docs/)
- [fix your timestep](https://gafferongames.com/post/fix_your_timestep/)
- [delta time & pygame](https://www.reddit.com/r/pygame/comments/3blsr3/jittering_movement/)
- [sending triggers](https://stackoverflow.com/questions/47019995/how-to-implement-triggers-in-python-script)
- [psychopy forum on eeg](https://discourse.psychopy.org/search?q=eeg)
- [pyserial](https://pyserial.readthedocs.io/en/latest/)
- [serial port triggers](http://forum.cogsci.nl/index.php?p=/discussion/734/open-serial-port-trigger-for-eeg/p1)
- [module for multiple lines of text in pygame](https://github.com/cosmologicon/pygame-text)
- [videos in python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#playing-video-from-file)
[videos in python with moviepy](http://zulko.github.io/moviepy/getting_started/videoclips.html)
