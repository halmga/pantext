#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
import pantext

dickens = ["It was the best of times. it was the worst of times!",
           "it was the age of wisdom. It was the age of foolishness. it was the epoch of belief?",
           "IT WAS THE EPOCH OF INCREDULITY!?#99"]

Q = pantext.Quantifier(dickens)

def test_normal_sentcount():
    assert Q.sent_count() == [2, 3, 2]
    
def test_word_count():
    assert Q.counts() == [12, 18, 7]

def test_english_stopcount():
    assert Q.stopword_percent(stop_words="english") == [0.57, 0.57, 0.4]
    
dickens_missing = ["It was the best of times. it was the worst of times!","","IT WAS THE EPOCH OF INCREDULITY!?#99"]

Q_missing = pantext.Quantifier(dickens_missing)

def test_zero_percent():
    assert Q_missing.stopword_percent(stop_words="english") == [0.57, 0.0, 0.4]

