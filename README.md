# GERSHWIN

GERSHWIN is a music generator software that takes lyrical and genre input and outputs a melody in audio and visual form (sheet music). GERSHWIN works by taking the lyrical input, counting the number of syllables, and connecting each syllable to a note or chord tied specifically to the determined major or minor key. The output of notes will adhere to standard music convention (so it won't sound like random notes strung together) and a specific genre of music (jazz, pop, R&B, and rock). Artists and music enthusiasts can use this program to get inspiration for song creation.

## Website
For more information about this project, check out our [website]!(https://sd19spring.github.io/GERSHWIN/)

## Authors

All unattributed code has been written by [Annie Chu](https://github.com/anniejchu), [Madi Wyatt](https://github.com/vmwyatt), [Eriel Wiston](https://github.com/erielw), and [Joanna Mei](https://github.com/jmei634).

## Built Using

[The CMU Pronunciation Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) - Used to count lyric syllables

[music21](https://web.mit.edu/music21/) - Used to generate notes

[MuseScore](https://musescore.org/en) - Used to produce sheet music

[TiMidity++](http://timidity.sourceforge.net/) - Used to play MIDI track

[NLTK](https://www.nltk.org/) - Used for sentiment analysis of lyrics


## Getting Started

Download relevant python packages:
```
pip install -r requirements.txt
```

Download MuseScore python library:
```
sudo snap install musescore
```
or
```
install AppImage on the MuseScore website
```

Download MIDI Player Timidity:
```
sudo apt-get install timidity
```

## To Run

In order to run GERSHWIN, make sure all applicable software has been downloaded, then run the following file in the terminal using:
```
 python framework.py
```
