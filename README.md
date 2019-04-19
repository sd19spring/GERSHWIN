Final Project: Software Design Spring 2019

Team Members: Eriel, Madi, Annie, Joanna

Project Name: GERSHWIN   

GERSHWIN is a music generator software that takes lyrical and genre input and outputs a melody in audio and visual form (sheet music). GERSHWIN works by taking the lyrical input, counting the number of syllables, and connecting each syllable to a note (generally notes from a major or minor scale). The output of notes will adhere to standard music convention (so it won't sound like random notes strung together) and a specific genre of music (jazz, pop, etc.). Artists and music enthusiasts can use this program to get inspiration for song creation.

Download the music21 python library:
pip install music21

Download MuseScore python library:
sudo snap install musescore
or 
install AppImage on the MuseScore website

Download MIDI Player Timidity:
sudo apt-get install timidity

To use MuseScore with music21, connect musicxmlPath key to application path


