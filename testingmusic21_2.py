from music21 import *
from pygame.locals import *
import pygame
import syllable_counter as sc
import framework as fw
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#setting up the environment, connecting music21 to sheet music generator and MIDI player
musicxmlpath = '/usr/bin/musescore' #do sudo apt install musescore

midipath = '/usr/bin/timidity' #static path using
us = environment.UserSettings()
us['musicxmlPath'] = musicxmlpath
us['midiPath'] = midipath

"""
INITIATING NOTES
"""
B3 = note.Note("B3", type ='quarter')

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

#diminished chords
B_dim_c = chord.Chord([B3, D, F], type='quarter')
C_dim_c = chord.Chord([C, Eb, Gb], type='quarter')
Db_dim_c = chord.Chord([Db, E, G], type ='quarter')
D_dim_c = chord.Chord([D, F, Ab], type='quarter')
Eb_dim_c = chord.Chord([Eb, Gb, A], type='quarter')
E_dim_c = chord.Chord([E, G, Bb], type='quarter')
F_dim_c = chord.Chord([F, Ab, B5], type='quarter')
Gb_dim_c = chord.Chord([Gb, A, C5], type='quarter')
G_dim_c = chord.Chord([G, Bb, Db5], type='quarter')
Ab_dim_c = chord.Chord([Ab, B, D5], type='quarter')
A_dim_c = chord.Chord([A, C, Eb5], type='quarter')
Bb_dim_c = chord.Chord([Bb, Db5, E5], type='quarter')

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

bluesmajor_s_Gmajor = [G, A, Bb, B, D5, E5]
bluesmajor_s_Fminor = [F, Ab, Bb, B, C5, Eb5]

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

#jazz
#ii_V_I
Cmajor_cp_j = [Dminor_c, Gmajor_c, Cmajor_c]
Dbmajor_cp_j = [Ebminor_c, Abmajor_c, Dbmajor_c]
Dmajor_cp_j = [Eminor_c, Amajor_c, Dmajor_c]
Ebmajor_cp_j = [Fminor_c,Bbmajor_c, Ebmajor_c]
Emajor_cp_j = [Gbminor_c, Bmajor_c, Emajor_c]
Fmajor_cp_j = [Gminor_c, Cmajor_c, Fmajor_c]
Gbmajor_cp_j = [Abminor_c, Dbmajor_c, Gbmajor_c]
Gmajor_cp_j = [Aminor_c, Dmajor_c, Gmajor_c]
Abmajor_cp_j = [Bbminor_c,Ebmajor_c, Abmajor_c]
Amajor_cp_j = [Bminor_c, Emajor_c, Amajor_c]
Bbmajor_cp_j = [Cminor_c, Fmajor_c,Bbmajor_c]
Bmajor_cp_j = [Dbminor_c, Gbmajor_c, Bmajor_c]

#II_V_I minor
Aminor_cp_j = [B_dim_c, Eminor_c, Aminor_c]
Bbminor_cp_j = [C_dim_c, Fminor_c, Bbminor_c]
Bminor_cp_j = [Db_dim_c, Gbminor_c, Bminor_c]
Cminor_cp_j = [D_dim_c, Gminor_c, Cminor_c]
Dbminor_cp_j = [Eb_dim_c, Abminor_c, Dbminor_c]
Dminor_cp_j = [E_dim_c, Aminor_c, Dminor_c]
Ebminor_cp_j = [F_dim_c, Bbminor_c, Ebminor_c]
Eminor_cp_j = [Gb_dim_c, Bminor_c, Eminor_c]
Fminor_cp_j = [G_dim_c, Cminor_c, Fminor_c]
Gbminor_cp_j = [Ab_dim_c, Dbminor_c, Gbminor_c]
Gminor_cp_j = [A_dim_c, Dminor_c, Gminor_c]
Abminor_cp_j = [Bb_dim_c, Ebminor_c, Abminor_c]

#rock
#I_VI_IV_V major
Cmajor_cp_r = [Cmajor_c, Aminor_c, Fmajor_c, Gmajor_c]
Dbmajor_cp_r = [Dbmajor_c, Bbminor_c, Gbmajor_c, Abmajor_c]
Dmajor_cp_r = [Dmajor_c, Bminor_c, Gmajor_c, Amajor_c]
Ebmajor_cp_r = [Ebmajor_c, Cminor_c, Abmajor_c, Bbmajor_c]
Emajor_cp_r = [Emajor_c, Dbminor_c, Amajor_c, Bmajor_c]
Fmajor_cp_r = [Fmajor_c, Dminor_c, Bbmajor_c, Cmajor_c]
Gbmajor_cp_r = [Gbmajor_c, Ebminor_c, Bmajor_c, Dbmajor_c]
Gmajor_cp_r = [Gmajor_c, Eminor_c, Cmajor_c, Dmajor_c]
Abmajor_cp_r = [Abmajor_c, Fminor_c, Dbmajor_c, Ebmajor_c]
Amajor_cp_r = [Amajor_c, Gbminor_c, Dmajor_c, Emajor_c]
Bbmajor_cp_r = [Bbmajor_c, Gminor_c, Ebmajor_c, Fmajor_c]
Bmajor_cp_r = [Bmajor_c, Abminor_c, Emajor_c, Gbmajor_c]

#I_VI_IV_V minor
Aminor_cp_r = [Aminor_c, Cmajor_c, Gmajor_c, Eminor_c]
Bbminor_cp_r = [Bbminor_c, Dbmajor_c, Abmajor_c, Fminor_c]
Bminor_cp_r = [Bminor_c, Dmajor_c, Amajor_c, Gbminor_c]
Cminor_cp_r = [Cminor_c, Ebmajor_c, Bbmajor_c, Gminor_c]
Dbminor_cp_r = [Dbminor_c, Emajor_c, Bmajor_c, Abminor_c]
Dminor_cp_r = [Dminor_c, Fmajor_c, Cmajor_c, Aminor_c]
Ebminor_cp_r = [Ebminor_c, Gbmajor_c, Dbmajor_c, Bbminor_c]
Eminor_cp_r = [Eminor_c, Gmajor_c, Dmajor_c, Bminor_c]
Fminor_cp_r = [Fminor_c, Abmajor_c, Ebmajor_c, Cminor_c]
Gbminor_cp_r = [Gbminor_c, Amajor_c, Emajor_c, Dbminor_c]
Gminor_cp_r = [Gminor_c, Bbmajor_c, Fmajor_c, Dminor_c]
Abminor_cp_r = [Abminor_c, Bmajor_c, Gbmajor_c, Ebminor_c]


#r&b
Fminor_9 = chord.Chord([F, G, Ab, C5, Ab5], type='quarter')
Bb_7 = chord.Chord([F, Ab, Bb, D5], type='quarter')
Ebminor_9 = chord.Chord([Eb, Gb, Bb, Db5, F5], type='quarter')
Ab_7 = chord.Chord([Ab, C5, Eb5, Gb5], type='quarter')

#chord progression
rb_cp = [Fminor_9, Bb_7, Ebminor_9, Ab_7]
rb_minor = [Fminor_9, Ebminor_9,Eminor_c,Aminor_c]
rb_major = [Bb_7, Ab_7, Gbmajor_c,Fmajor_c]

#instruments
#pop
piano = instrument.Piano()
guitar = instrument.Guitar()

#rock
electric_guitar = instrument.ElectricGuitar()
electric_bass = instrument.ElectricBass()

#jazz
alto_sax = instrument.AltoSaxophone()
baritone_sax = instrument.BaritoneSaxophone()
trumpet = instrument.Trumpet()

#r&b
#electric bass
#piano
organ = instrument.Organ()

def build_jazz(num_syl, key, new_song):
    major = [bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s, bluesmajor_s,
            Cmajor_cp_j, Dbmajor_cp_j, Dmajor_cp_j, Ebmajor_cp_j, Emajor_cp_j, Fmajor_cp_j, Gbmajor_cp_j, Gmajor_cp_j, Abmajor_cp_j, Amajor_cp_j, Bbmajor_cp_j, Bmajor_cp_j]
    minor = [bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s, bluesminor_s,
            Cminor_cp_j, Dbminor_cp_j, Dminor_cp_j, Ebminor_cp_j, Eminor_cp_j, Fminor_cp_j, Gbminor_cp_j, Gminor_cp_j, Abminor_cp_j, Aminor_cp_j, Bbminor_cp_j, Bminor_cp_j]
    if key == True:
        #base = random.choice(major)
        base = bluesmajor_s
    if key == False:
        #base = random.choice(minor)
        base = bluesminor_s

    change = [-1,1]
    start_note = random.randrange(0, len(base)-1)
    new_song.append(base[start_note])

    for i in range(0, num_syl-1):
        delt = random.choice(change)
        start_note = start_note+delt

        if start_note < 0:
            start_note = random.choice(range(0,3))
        if start_note > len(base)-1:
            start_note = random.choice(range(3,len(base)-1))

        new_song.repeatAppend(base[start_note],1)

    return new_song

def build_pop(num_syl, key, new_song):
    major = [Cmajor_cp, Dbmajor_cp, Dmajor_cp, Ebmajor_cp, Emajor_cp, Fmajor_cp, Gbmajor_cp, Gmajor_cp , Abmajor_cp, Amajor_cp, Bbmajor_cp, Bmajor_cp]
    minor = [Cminor_cp, Dbminor_cp, Dminor_cp, Ebminor_cp, Eminor_cp, Fminor_cp, Gbminor_cp, Gminor_cp , Abminor_cp, Aminor_cp, Bbminor_cp, Bminor_cp]
    if key == True:
        base = random.choice(major)
    if key == False:
        base = random.choice(minor)

    change = [-2,-1,1,2]
    start_chord = random.randrange(0, len(base)-1)
    new_song.append(base[start_chord])

    for i in range(0,num_syl-1):
        delt = random.choice(change)
        start_chord = start_chord+delt

        if start_chord < 0 or start_chord > len(base)-1:
            start_chord = random.choice(range(0,len(base)-1))

        new_song.repeatAppend(base[start_chord],1)

    return new_song

def build_rb(num_syl, key, new_song):
    if key == True:
        base = rb_major
        base1 = rb_minor
    if key == False:
        base = rb_minor
        base1 = rb_major

    change = [-1,1]
    start_chord = random.randrange(0, len(base)-1)
    new_song.append(base[start_chord])

    for i in range(0,int(num_syl/2)):
        start_chord = random.choice(base)
        start_chord1 = random.choice(base1)
        new_song.repeatAppend(start_chord,1)
        new_song.repeatAppend(start_chord1,1)
    if num_syl % 2 != 0:
        end_chord = random.choice(base)
        new_song.repeatAppend(end_chord,1)
    return new_song

def build_rock(num_syl, key, new_song):
    major = [Cmajor_cp_r, Dbmajor_cp_r, Dbmajor_cp_r, Ebmajor_cp_r, Emajor_cp_r, Fmajor_cp_r, Gbmajor_cp_r, Gmajor_cp_r, Abmajor_cp_r, Amajor_cp_r, Bbmajor_cp_r, Bmajor_cp_r]
    minor = [Cminor_cp_r, Dbminor_cp_r, Dminor_cp_r, Ebminor_cp_r, Eminor_cp_r, Fminor_cp_r, Gbminor_cp_r, Gminor_cp_r , Abminor_cp_r, Aminor_cp_r, Bbminor_cp_r, Bminor_cp_r]
    if key == True:
        base = random.choice(major)
    if key == False:
        base = random.choice(minor)

    change = [-1,1]
    start_chord = random.randrange(0, len(base)-1)
    new_song.append(base[start_chord])

    for i in range(0,num_syl):
        delt = random.choice(change)
        start_chord = start_chord+delt

        if start_chord < 0 or start_chord > len(base)-1:
            start_chord = random.choice(range(0,len(base)-1))

        new_song.repeatAppend(base[start_chord],1)

    return new_song



def choices(num_syl,key,new_song,buttons):
    if buttons['jazz'].clicked == True:
        return build_jazz(num_syl,key,new_song)
    elif buttons['pop'].clicked  == True:
        return build_pop(num_syl,key,new_song)
    elif buttons['rb'].clicked  == True:
        return build_rb(num_syl,key,new_song)
    elif buttons['rock'].clicked  == True:
        return build_rock(num_syl,key,new_song)
    elif buttons['random'].clicked  == True:
        pick = random.choice(fw.g_list[0:3])
        if pick == 'J A Z Z': return build_jazz(num_syl,key,new_song)
        if pick == 'R & B': return build_rb(num_syl,key,new_song)
        if pick == 'P O P': return build_pop(num_syl,key,new_song)
        if pick == 'R O C K': return build_rock(num_syl,key,new_song)

def input_to_key(i):
    sent = SentimentIntensityAnalyzer()
    polarity = sent.polarity_scores(i)
    if polarity['neg'] > polarity ['pos']:
        return False
    else:
        return True

def generate_song(input, buttons):
    #i = fw.input_text
    num_syl = sc.phrase_syllables(input)
    key = input_to_key(input)
    new_song = stream.Stream()
    new_song = choices(num_syl,key,new_song,buttons)
    new_song.show('midi')
    #new_song.show()

#input_def()
