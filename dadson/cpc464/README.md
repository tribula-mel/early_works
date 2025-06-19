# Conversion

This proved to be a very tricky process due to my inexperirence. I used
following equipment:

1. Nordmende Monocorder 1560
2. Dell Optiplex 7040
3. Audio cable (3.5 mm mono jack to 3.5 mm four piece jack):
   T - unconnected, R - unconnected, R - microphone, S - ground

Connections:

1. 3.5 mm mono jack was plugged into the speaker out connector (adjucent
   to the DIN connector) on the Monocorder end
2. 3.5 mm TRRS jack was plugged into the headset connector located at the
   front of Optiplex

On the software side I used Audacity. The configuration was ALSA / Headset
Mic0 / 2 (Stereo) Recording Channels, microphone level at the max, with the
44100 Hz rate. Exported file was WAV Signed 16-bit PCM.
The output audio level on the Monocorder side was varied from around 85% to
50%. Microphone volume level on the system side was vaired from around 33%
to 67% with PulseAudio Volume Control. Basically, initial conversions were
tried with 85%/33% speaker/microphone levels, with some success, and gradually
shifted to 50%/67% levels. While the later combo gave good results (not 100%),
I am not sure which is a better approach.
For conversion from WAV to CDT I used:

https://monocrun.com/cpc-tape-to-cdt

# Code collection

The most interesting code is:

1. editor-bin.cdt - unfinished text editor (z80)
2. filelist-v3-0.cdt plus filelist_v3.0-bin.cdt plus example.cdt (text file
   viewer, Basic + z80)
3. sortiranje.cdt plus sortiranje-bin.cdt - number sorting (Basic + z80)
4. memorija.cdt - memory game for two players (Basic)

From the orange cassete I still have to try to get:

1. reci 1.1
2. rotacija 1.2
3. permutacije
