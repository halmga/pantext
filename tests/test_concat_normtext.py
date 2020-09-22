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
    
dickens_missing_first = [[], ['it', 'be', 'the', 'age', 'of', 'wisdom', 'it', 'be', 'the', 'age', 'of', 'foolishness', 'it', 'be', 'the', 'epoch', 'of', 'belief'], ['it', 'be', 'the', 'epoch', 'of', 'incredulity']]

def test_concat_first_missing():
    assert pantext.concat_normtext(dickens_missing_first) == ['', ' it be the age of wisdom it be the age of foolishness it be the epoch of belief', ' it be the epoch of incredulity']

dickens_missing = [['it', 'be', 'the', 'best', 'of', 'time', 'it', 'be', 'the', 'worst', 'of', 'time'], [], ['it', 'be', 'the', 'epoch', 'of', 'incredulity']]

def test_concat_missing():
    assert pantext.concat_normtext(dickens_missing) == [' it be the best of time it be the worst of time', '', ' it be the epoch of incredulity']

