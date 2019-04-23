from music21 import *
#setting up the environment, connecting music21 to sheet music generator and MIDI player
musicxmlpath = '/var/lib/snapd/snaps/musescore_68.snap'

midipath = '/usr/bin/timidity' #static path using

us = environment.UserSettings()
#us['musicxmlPath'] = musicxmlpath
us['midiPath'] = midipath

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

Db = note.Note("D-4", type='quarter')
Eb = note.Note("E-4", type='quarter')
Gb = note.Note("G-4", type='quarter')
Ab = note.Note("A-4", type='quarter')
Bb = note.Note("B-4", type='quarter')

C5 = note.Note("C5", type = "quarter")
D5 = note.Note("D5", type='quarter')
E5 = note.Note("E5", type='quarter')
F5 = note.Note("F5", type='quarter')
G5 = note.Note("G5", type='quarter')
A5 = note.Note("A5", type='quarter')
B5 = note.Note("B5", type='quarter')

Db5 = note.Note("D-5", type='quarter')
Eb5 = note.Note("E-5", type='quarter')
Gb5 = note.Note("G-5", type='quarter')
Ab5 = note.Note("A-5", type='quarter')
Bb5 = note.Note("B-5", type='quarter')

rest = note.Rest()

#chords
Cmajor_c = chord.Chord([A, E, G], type='quarter')
# print(Cmajor_c)

#scales:major
Cmajor_s = [C, D, E, F, G, A, B, C5]
Dbmajor_s = [Db, Eb, F, Gb, Ab, Bb, C5, Db5]
Dmajor_s = [D, E, Gb, G, A, B, Db5, D5]
Ebmajor_s = [Eb, F, G, Ab, Bb, C5, D5, Eb5]
Emajor_s = [E, Gb, Ab, A, B, Db5, Eb5, E5]
Fmajor_s = [F, G, A, Bb, C5, D5, E5, F5]
Gbmajor_s = [Gb, Ab, Bb, B, Db5, Eb5, F5, Gb5]
Gmajor_s = [G, A, B, C, D5, E5, Gb5, G5]
Abmajor_s = [Ab, Bb, C5, Db5, Eb5, F5, G5, Ab5]
Amajor_s = [A, B, Db5, E5, Gb5, Ab5, A5]
Bbmajor_s = [Bb, C5, D5, Eb5, F5, G5, A5, Bb5]
Bmajor_s = [B5, Db5, Eb5, E5, Gb5, Ab5, B5]

#scales:minor
Cminor_s = [C, D, Eb, F, G, Ab, Bb, C5]
Dminor_s = [D, E, F, G, A, Bb, C5, D5]
Eminor_s = [E, Gb, G, A, B, C5, D5, E5]
Fminor_s = [F, G, Ab, Bb, C5, Db5, Eb5, F5]
Gminor_s = [G, A, Bb, C5, D5, Eb5, F5, G5]
Aminor_s = [A, B, C5, D5, E5, F5, G5, A5]
Bminor_s = [B, Db5, D5, E5, Gb5, G5, A5, B5]
Dbminor_s = [Db, Eb, E, Gb, Ab, A, B, Db5]
Ebminor_s = [Eb, F, Gb, Ab, Bb, B5, Db5, Eb5]
Gbminor_s = [Gb, Ab, A, B, Db5, D, E, Gb5]
Abminor_s = [Ab, Bb, B, Db5, Eb5, E5, Gb5, Ab5]
Bbminor_s = [Bb, C5, Db5, Eb5, F5, Gb5, Ab5, Bb5]

bluesmajor_s = [C, D, Eb, E, G, A]
bluesminor_s = [C, Eb, F, Gb, G, Bb, C5]

#testing out streams
s1 = stream.Stream()
for note in Cmajor_s:
    s1.append(note)
#print(s1.show('text'))
s2 = stream.Stream()
s2.append(Cmajor_c)

s3 = stream.Stream()
for note in bluesminor_s:
    s3.append(note)
#testing sheet music generator
#f.show()
#testing MIDI player
# s1.show('midi')
# s2.show('midi')
s3.show('midi')
