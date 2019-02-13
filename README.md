### Dot Experiment Fundamentals & Resources

##### Important Info:
- Monitor will be a CRT monitor
- Code will be run on a PC

##### My Frequencies:
- 1.5 Hz (2 syllable units)
- 1 Hz (3 syllable units) **Actually, apparently this is more like 1.1 Hz**
- 0.75 Hz (4 syllable units)

##### Resources:
- [pygame documentation](https://www.pygame.org/docs/)
- [fix your timestep](https://gafferongames.com/post/fix_your_timestep/)
- [delta time & pygame](https://www.reddit.com/r/pygame/comments/3blsr3/jittering_movement/)
- [sending triggers](https://stackoverflow.com/questions/47019995/how-to-implement-triggers-in-python-script)
  - Need to figure out how we are communicating with EEG (probably serial port).
- [psychopy forum on eeg](https://discourse.psychopy.org/search?q=eeg)
- [pyserial](https://pyserial.readthedocs.io/en/latest/)

##### Ideas/next steps:
- Make dot animation continuous
- Be able to analyze all dot times to ensure approx one min apart
- Send triggers from program to EEG to time lock stimulus presentation
- Implement auditory stimuli
- ~~Be able to input the frequency?~~
- ~~Set up background as fullscreen black window (animation will be in smaller white box)~~
