#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytest
from pantext import clean_text

dickens = ["It was the best of times. it was the worst of times!",
           "it was the age of wisdom. It was the age of foolishness. it was the epoch of belief?",
           "IT WAS THE EPOCH OF INCREDULITY!?#99"]

def test_remove_numbers_characters():
    assert pantext.clean_text(dickens,replace = '[!#0-9]', replace_with='') == ['It was the best of times. it was the worst of times',
                                                                        'it was the age of wisdom. It was the age of foolishness. it was the epoch of belief?',
                                                                        'IT WAS THE EPOCH OF INCREDULITY?']

def test_remove_words():
    assert pantext.clean_text(dickens,replace = '\w+', replace_with='') == ['     .      !', '     .      .      ?', '     !?#']

def test_remove_nothing():
    assert pantext.clean_text(dickens,replace = "'", replace_with='NOTHING') == ['It was the best of times. it was the worst of times!',
                                                                         'it was the age of wisdom. It was the age of foolishness. it was the epoch of belief?',
                                                                         'IT WAS THE EPOCH OF INCREDULITY!?#99']

