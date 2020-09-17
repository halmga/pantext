#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from nltk.corpus import stopwords
from nltk import download
from re import sub
from nltk.tokenize import RegexpTokenizer, sent_tokenize, word_tokenize
from tqdm import tqdm

download('stopwords')
download('wordnet')

class Quantifiers:
    """
    class for quantifying aspects of text in a panda column format
    """
    def __init__(self,text):
        self.text = text
    
        #sentence count 
    def sent_count(self):
        count = []
        for i in tqdm(self.text):
            count.append(len(sent_tokenize(i)))
        return count

    #regex counter can count any type of regular expression occurrences in text default words
    def counts(self, regex = "\w+"):
        tokenizer = RegexpTokenizer(r'{}'.format(regex))
        count = []
        for i in tqdm(self.text):
            count.append(len(tokenizer.tokenize(i)))
        return count

    #counts percentage of words in text that are stopwords
    def stopword_percent(self, stop_words = 'english'):
        """
        stop_words: see nltk.corpus.stopwords for languages, default 'english'
        choose language for stopwords being used
        """
        stops = set(stopwords.words(stop_words))
        percent = []
        for i in tqdm(self.text):
            text_l = i.lower()
            word_tokens = word_tokenize(text_l)
            stop_w = [word for word in word_tokens if word in stops]
            percent.append(round((len(stop_w)/len(word_tokens)), 2))
        return percent

