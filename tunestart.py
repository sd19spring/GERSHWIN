import string
import math
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
songline = input("Type in a line of lyrics to your song! Please split up your song ly rics by syll a ble, like this: ")

def linesplit(line):
    words = str(line).split()
    collector = []
    for word in words:
        word = word.strip(string.punctuation)
        #word = word.lower()
        collector.append(word)
    return collector

def syllable(word):
    if len(word) > 5:
        count = math.ceil(word/5)
        div = 5
    elif len(word) > 2:
        count = math.ceil(word/2)
        div = 2
    else:
        count = 1
        div = 2
    wordparts = []
    while count > 0:
        wordparts.append('''Segments of a string of character count div''')
    return wordparts

#print(linesplit(songline))

def sentiment(songline):
    analyzer = SentimentIntensityAnalyzer()
    sent_scores = analyzer.polarity_scores(songline)
    return sent_scores

def det_mode(scores):
    if scores['pos'] => scores['neg']:
        print('Major')
    if scores['neg'] > scores['pos']:
        print('Minor')

def main():
    lyric = songline
    sent_analysis = sentiment(songline)
    det_mode(sent_analysis)

main()
