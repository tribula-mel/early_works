# Conversion

This proved to be a very tricky process due to my inexperience. I used
following equipment:

1. Nordmende Monocorder 1560
2. Dell Optiplex 7040
3. Audio cable (3.5 mm mono jack to 3.5 mm four piece jack):
   T - unconnected, R - unconnected, R - microphone, S - ground

Connections:

1. 3.5 mm mono jack was plugged into the speaker out connector (adjacent
   to the DIN connector) on the Monocorder end
2. 3.5 mm TRRS jack was plugged into the headset connector located at the
   front of Optiplex

On the software side I used Audacity. The configuration was ALSA / Headset
Mic0 / 2 (Stereo) Recording Channels, microphone level at 0.73, with the
44100 Hz rate. Exported file was `WAV Signed 16-bit PCM`.
The output audio level on the Monocorder side was varied from around 85% to
50%. Microphone volume level on the system side was varied from around 33%
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

The orange cassette A side is all converted apart from Fruity Frank game, while the B side has the following titles:

1. Yie-ar Kung-Fu (no header so can't be converted with the `monocrun`)
2. Maxam2 and Maxam3 (partial files, basically lost)
3. Hisoft Pascal (converted)
4. Label Basic (block 2 problematic)
5. the rest of the side is blank
