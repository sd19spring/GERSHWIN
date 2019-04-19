from music21 import *
us = environment.UserSettings()
us['musicxmlPath'] = '/home/joanna/.local/bin/MuseScore-3.0.5-x86_64.AppImage'
us['midiPath'] = '/usr/bin/timidity'

f = note.Note("F5")
f.show('midi')
