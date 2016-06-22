"""
Build by Subham Biswas and Arnab Borah
This code separates the twitter sentence into separate words including
hashtags
"""
# Returns a list of common english terms (words)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import re

def InitializeWords():
    wordlist = 'D:\Courses\Data Science Specialization\Datasets\wordlist.txt' # A file containing common english words
    content = None
    with open(wordlist) as f:
        content = f.readlines()
    return [word.rstrip('\n') for word in content]


def ParseSentence(sentence, wordlist):
    new_sentence = "" # output    
    terms = sentence.split(' ')    
    for term in terms:
        if term[0] == '#': # this is hashtag, parse it
            new_sentence += ParseTag(term, wordlist)
        else: # Just append the word
            new_sentence += term
        new_sentence += " "

    return new_sentence 


def ParseTag(term, wordlist):
    words = []
    # Remove hashtag, split by dash
    tags = term[1:].split('-')
    for tag in tags:
        word = FindWord(tag, wordlist)    
        while word != None and len(tag) > 0:
            words += [word]            
            if len(tag) == len(word): # Special case for when eating rest of word
                break
            tag = tag[len(word):]
            word = FindWord(tag, wordlist)
    return " ".join(words)

def FindWord(token, wordlist):
    i = len(token) + 1
    while i > 1:
        i -= 1
        if token[:i] in wordlist:
            return token[:i]
    return None 

wordlist = InitializeWords()
sentence = "#DareToPerform"
sentence = sentence.lower()
'''sentence_list = []
sentence_list = sentence.split()
hashtag = []

for w in sentence_list:
    if w[0] is '#':
        hashtag += w

sentence = ''.join(hashtag)
print sentence

for w in hashtag:
    if w is not '#':
        hashtag2 += w

print hashtag
print hashtag2
'''

#sentence = sentence.replace("#"," #")

#print (sentence)
separated_words = ParseSentence(sentence, wordlist)
print separated_words

