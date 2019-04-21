from music21 import *
#setting up the environment, connecting music21 to sheet music generator and MIDI player
# us = environment.UserSettings()
# us['musicxmlPath'] = '/home/joanna/.local/bin/MuseScore-3.0.5-x86_64.AppImage'
# us['midiPath'] = '/usr/bin/timidity'

#testing built in classes and methods
f = note.Note("F5")
print(f.name)
print(f.octave)
print(f.pitch)

"""
INITIATING NOTES
"""
C = note.Note("C4", type = "quarter")
D = note.Note("D4", type='quarter')
E = note.Note("E4", type='quarter')
F = note.Note("F4", type='quarter')
G = note.Note("G4", type='quarter')
A = note.Note("A4", type='quarter')
B = note.Note("B4", type='quarter')

Dflat = note.Note("D-4", type='quarter')
print(Dflat.octave)
Eflat = note.Note("E-4", type='quarter')
Gflat = note.Note("G-4", type='quarter')
Aflat = note.Note("A-4", type='quarter')
Bflat = note.Note("B-4", type='quarter')

rest = note.Rest()

#chords
Cmajor_c = chord.Chord([A, E, G])
print(Cmajor)

#scales
Cmajor_s = [C, D, E, F, G, A, B]
#testing out streams
s1 = stream.Stream()
for note in Cmajor_s:
    s1.append(note)
print(s1.show('text'))


#testing sheet music generator
#f.show()
#testing MIDI player
#f.show('midi')
