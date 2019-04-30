from music21 import *
from pygame.locals import *
import pygame
import syllable_counter as sc
import framework as fw
import random
#setting up the environment, connecting music21 to sheet music generator and MIDI player
musicxmlpath = '/usr/bin/musescore' #do sudo apt install musescore

midipath = '/usr/bin/timidity' #static path using
us = environment.UserSettings()
us['musicxmlPath'] = musicxmlpath
us['midiPath'] = midipath

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

#major chords
Cmajor_c = chord.Chord([C, E, G], type='quarter')
Dbmajor_c = chord.Chord([Db, F, Ab], type='quarter')
Dmajor_c = chord.Chord([D, Gb, A], type='quarter')
Ebmajor_c = chord.Chord([Eb, G, Bb], type='quarter')
Emajor_c = chord.Chord([E, Ab, B], type='quarter')
Fmajor_c = chord.Chord([F, A, C5], type='quarter')
Gbmajor_c = chord.Chord([Gb, Bb, Db5], type='quarter')
Gmajor_c = chord.Chord([G, B, D5], type='quarter')
Abmajor_c = chord.Chord([Ab, C5, Eb5], type='quarter')
Amajor_c = chord.Chord([A, Db5, Gb5], type='quarter')
Bbmajor_c = chord.Chord([Bb, D5, F5], type='quarter')
Bmajor_c = chord.Chord([B5, Eb5, Gb5], type='quarter')

# print(Cmajor_c)

#minor chords
Cminor_c = chord.Chord([C, Eb, G], type='quarter')
Dminor_c = chord.Chord([D, F, A], type='quarter')
Eminor_c = chord.Chord([E, G, B], type='quarter')
Fminor_c = chord.Chord([F, Ab,C5], type='quarter')
Gminor_c = chord.Chord([G, Bb, D5], type='quarter')
Aminor_c = chord.Chord([A, C5, E5], type='quarter')
Bminor_c = chord.Chord([B, D5, Gb5], type='quarter')
Dbminor_c = chord.Chord([Db, E, Ab], type='quarter')
Ebminor_c = chord.Chord([Eb, Gb, Bb], type='quarter')
Gbminor_c = chord.Chord([Gb, A, Db5], type='quarter')
Abminor_c = chord.Chord([Ab, B, Eb5], type='quarter')
Bbminor_c = chord.Chord([Bb, Db5, F5], type='quarter')

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

#chord progressions

#pop
#I_V_vi_IV major
Cmajor_cp = [Cmajor_c, Gmajor_c, Aminor_c, Fmajor_c] #most common
Dbmajor_cp = [Dbmajor_c, Abmajor_c, Bbminor_c, Gbmajor_c]
Dmajor_cp = [Dmajor_c, Amajor_c, Bminor_c, Gmajor_c]
Ebmajor_cp = [Ebmajor_c, Bbmajor_c, Cminor_c, Abmajor_c]
Emajor_cp = [Emajor_c, Bmajor_c, Dbminor_c, Amajor_c]
Fmajor_cp = [Fmajor_c, Cmajor_c, Dminor_c, Bbmajor_c]
Gbmajor_cp = [Gbmajor_c, Dbmajor_c, Ebminor_c, Bmajor_c]
Gmajor_cp = [Gmajor_c, Dmajor_c, Eminor_c, Cmajor_c] #most common
Abmajor_cp = [Abmajor_c, Ebmajor_c, Fminor_c, Dbmajor_c]
Amajor_cp = [Amajor_c, Emajor_c, Gbminor_c, Dmajor_c]
Bbmajor_cp = [Bbmajor_c, Fmajor_c, Gminor_c, Ebmajor_c]
Bmajor_cp = [Bmajor_c, Gbmajor_c, Abminor_c, Emajor_c]

#I_V_vi_IV minor
Aminor_cp = [Aminor_c, Fmajor_c, Cmajor_c, Gmajor_c] #most common
Bbminor_cp = [Bbminor_c, Gbmajor_c, Dbmajor_c, Abmajor_c]
Bminor_cp = [Bminor_c, Gmajor_c, Dmajor_c, Amajor_c]
Cminor_cp = [Cminor_c, Abmajor_c, Ebmajor_c, Bbmajor_c]
Dbminor_cp = [Dbminor_c, Amajor_c, Emajor_c, Bmajor_c]
Dminor_cp = [Dminor_c, Bbmajor_c, Fmajor_c, Cmajor_c]
Ebminor_cp = [Ebminor_c, Bmajor_c, Gbmajor_c, Dbmajor_c]
Eminor_cp = [Eminor_c, Cmajor_c, Gmajor_c, Dmajor_c] #most common
Fminor_cp = [Fminor_c, Dbmajor_c, Abmajor_c, Ebmajor_c]
Gbminor_cp = [Gbminor_c, Dmajor_c, Amajor_c, Emajor_c]
Gminor_cp = [Gminor_c, Ebmajor_c, Bbmajor_c, Fmajor_c]
Abminor_cp = [Abminor_c, Emajor_c, Bmajor_c, Gbmajor_c]

def build_jazz(new_song, num_syl):
    change = [-1,1]
    start_note = random.randrange(0, len(bluesmajor_s)-1)
    new_song.append(bluesmajor_s[start_note])
    #print(new_song)
    for i in range(0, num_syl):
        delt = random.choice(change)
        start_note = start_note+delt
        new_song.append(bluesmajor_s[start_note])
    return new_song

def build_pop(new_song, num_syl):
    change = [-2,-1,1,2]
    start_chord = random.randrange(0, len(Gmajor_cp)-1)
    new_song.append(Gmajor_cp[start_chord])
    for i in range(0,num_syl):
        delt = random.choice(change)
        start_chord = start_chord+delt
        new_song.append(Gmajor_cp[start_chord])
    return new_song

def choices(genres, i, new_song, num_syl):
    if fw.jazz.check_clicked(pygame.event.get()) == True:
        return build_jazz(new_song, num_syl)
    elif fw.pop.check_clicked(pygame.event.get()) == True:
        return build_pop(new_song, num_syl)

def input_def():
    i = input("Name your lyric: ")
    num_syl = sc.phrase_syllables(i)
    #s4 = stream.Stream()
    new_song = []
    genres = ['jazz', 'pop']
    fw.main(60,fw.Title())
    x = choices(genres,i, new_song, num_syl)
    print(x)
    # s4.show('text')
    # s4.show('midi')
        #stream.append(note)

    #stream.show('midi')

# F.show()
# F.show('midi')
input_def()
