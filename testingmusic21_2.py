from music21 import *
#setting up the environment, connecting music21 to sheet music generator and MIDI player
us = environment.UserSettings()
us['musicxmlPath'] = '/home/joanna/.local/bin/MuseScore-3.0.5-x86_64.AppImage'
us['midiPath'] = '/usr/bin/timidity'

#testing built in classes and methods
f = note.Note("F5")
print(f.name)
print(f.octave)
print(f.pitch)

#testing sheet music generator
#f.show()
#testing MIDI player
#f.show('midi')
