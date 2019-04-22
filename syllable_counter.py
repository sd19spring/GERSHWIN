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

def word_syllables(word):
    """
    this function allows you to input a word and the syllable count is the output
    """
    return words.get(word.upper(), 0)

def phrase_syllables(phrase):
    """
    this function allows you to imput phrases
    """
    phrase_words = phrase.split()
    count = 0
    for phrase_word in phrase_words:
        i = 0
        while i < len(phrase_word):
            if string.digits.find(phrase_word[i]) > -1 or string.punctuation.find(phrase_word[i]) > -1:
                phrase_word = phrase_word[0:i] + phrase_word[i + 1:]

            i += 1

        count += word_syllables(phrase_word)

    return count


print(word_syllables("software"))
print(phrase_syllables("software design is difficult"))
