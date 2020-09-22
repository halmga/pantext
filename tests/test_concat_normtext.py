#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
import pantext

dickens = [['it','be','the','best','of','time','it','be','the','worst','of','time'],
           ['it','be','the','age','of','wisdom','it','be','the','age','of','foolishness','it','be','the','epoch','of','belief'],
           ['it', 'be', 'the', 'epoch', 'of', 'incredulity']]

def test_normal_concat():
    assert pantext.concat_normtext(dickens)== [' it be the best of time it be the worst of time',' it be the age of wisdom it be the age of foolishness it be the epoch of belief',' it be the epoch of incredulity']
    
dickens_missing_first = ["",
           "it was the age of wisdom. It was the age of foolishness. it was the epoch of belief?",
           "IT WAS THE EPOCH OF INCREDULITY!?#99"]

def test_concat_first_missing():
    assert pantext.concat_normtext(dickens_missing_first) == ['', ' it be the age of wisdom it be the age of foolishness it be the epoch of belief', ' it be the epoch of incredulity']

dickens_missing = ["It was the best of times. it was the worst of times!","","IT WAS THE EPOCH OF INCREDULITY!?#99"]

def test_concat_missing():
    assert pantext.concat_normtext(dickens_missing) == [' it be the best of time it be the worst of time', '', ' it be the epoch of incredulity']

