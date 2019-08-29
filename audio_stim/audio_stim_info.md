### Audio stim info
The stimuli order text file includes the exact order in which the audio stimuli will be presented.

There are 4 different "nonsense" words that are made up of three syllables each... and each syllable is identified by a specific number. These numbers are what appear in the stimuli order text file.

# pautoki (12, 7, 2)
12 = wave.open('audio_stim/pau.wav', 'r')
7 = wave.open('audio_stim/to.wav', 'r')
2 = wave.open('audio_stim/ki.wav', 'r')
# nurafi (11, 1, 8)
11 = wave.open('audio_stim/nu.wav', 'r')
1 = wave.open('audio_stim/ra.wav', 'r')
8 = wave.open('audio_stim/fi.wav', 'r')
# mailone (5, 4, 9)
5 = wave.open('audio_stim/mai.wav', 'r')
4 = wave.open('audio_stim/lo.wav', 'r')
9 = wave.open('audio_stim/ne.wav', 'r')
# gabalu (10, 3, 6)
10 = wave.open('audio_stim/ga.wav', 'r')
3 = wave.open('audio_stim/ba.wav', 'r')
6 = wave.open('audio_stim/lu.wav', 'r')
