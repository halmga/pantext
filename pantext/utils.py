#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from re import sub
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import RegexpTokenizer, sent_tokenize, word_tokenize
from nltk import download
from tqdm import tqdm
download("punkt")

def text_normalize(text, method = 'lemmas'):
    """
    text: list or column of multiple texts as string
    method: {'lemmas','stems'}, default 'lemmas'
    """
    if method == 'lemmas':
        normalizer = WordNetLemmatizer()
    if method == 'stems':
        normalizer = PorterStemmer()
    temp = []
    for i in tqdm(range(len(text))):
        words = word_tokenize(text[i])
        words=[word.lower() for word in words if word.isalpha()]
        if method == 'lemmas':
            temp.append([normalizer.lemmatize(w, pos='v') for w in words])
        if method == 'stems':
            temp.append([normalizer.stem(w) for w in words])
    return temp


def clean_text(text,replace = None, replace_with = '', lower_case = False):
    """
    text: list or column of multiple texts as string
    replace: words or characters to be replaced
    replace_with: replacement words or characters
    lower_case: return text in lower case
    """
    clean_temp = []
    for t in tqdm(text):
        temp = []
        if lower_case == True:
            t = t.lower()  
        else:
            t = t
        t = sub(replace,replace_with,str(t))
        temp.append(t)
        clean_temp.append(temp)
    return [i for sublist in clean_temp for i in sublist]

def concat_normtext(text):
    """
    concatenate list of normalized text into one string
    
    text: list or column of multiple texts as string
    """
    temp_text = []
    for t in text:
        string = ""
        for i in t:
            temp = []
            string = string + " " + i
        temp.append(string)
        temp_text.append(temp)
    return [i for sublist in temp_text for i in sublist]

