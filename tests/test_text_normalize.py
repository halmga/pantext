#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytest
import pantext

dickens = ["It was the best of times. it was the worst of times!",
           "it was the age of wisdom. It was the age of foolishness. it was the epoch of belief?",
           "IT WAS THE EPOCH OF INCREDULITY!?#99"]


def test_clean_list_lemmas():
    assert pantext.text_normalize(dickens, method = 'lemmas') == [['it','be','the','best','of','time','it','be','the','worst','of','time'],
                                       ['it','be','the','age','of','wisdom','it','be','the','age','of','foolishness','it','be','the','epoch','of','belief'],
                                       ['it', 'be', 'the', 'epoch', 'of', 'incredulity']]
def test_clean_list_stems():
    assert text_normalize(dickens, method = 'stems') == [['it','wa','the','best','of','time','it','wa','the','worst','of','time'],
                                                         ['it','wa','the','age','of','wisdom','it','wa','the','age','of','foolish','it','wa','the','epoch','of','belief'],
                                                         ['it', 'wa', 'the', 'epoch', 'of', 'incredul']]
def test_nested_list():
    nested = [['too many lists']]
    with pytest.raises(TypeError):
        text_normalize(nested)
    


    


# In[ ]:




