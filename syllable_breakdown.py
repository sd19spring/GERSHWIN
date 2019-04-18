"""
Syllable Counter

file referenced is a version of a dictionary from a CMU pronnunciation guide:
http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=software+design+is+hard&stress=-s

Madi Wyatt
"""

import string

#initialize the dictionary and open the CMU dictionary file
pronnunciation_dict = open("syllable_dict.txt", "r")
words = dict()

#breakdown CMU dictionary and make a new one that gives us just the syllable count
for word_entry in pronnunciation_dict:
    word_list = word_entry.split()
    words[word_list[0]] = "".join(word_list[1:])
    count = 0
    for i in range(0, len(words[word_list[0]])):
        if words[word_list[0]][i] in string.digits:
            count += 1
    words[word_list[0]] = count

#write a function that allows you to imput a word and the syllable count is output
def syllable_count(word):
    return words[word.upper()]

print(syllable_count("hello"))
