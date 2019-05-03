### How It Works

![](uml_diagram.jpg)

Input text is broken down into the number of syllables, which correlates with the number of notes generated, and is analyzed via sentiment analysis. If the lyrics input have a happeir sentiment, the song is played in a major key, while if the song has a more sad tone, the song is played in a minor key. 

Genre choice is linked to lists of common noes, scales, and progressions defined within a given genre. 

The outputs are extended paths from music21, a python music library, to musescore, a sheet music and midi program, to timidity, where our audio is generated. 

_put image here of concept map_


_step through code, pull where necessary_
