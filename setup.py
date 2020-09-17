#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptoold import setup

setup(name= 'pantex',
     version= '0.0.1',
     description= 'text cleaning package for use on pandas dataframes and lists',
     author= 'Gabriel Halm',
     packages= ['pantex'],
     install_requires= ['pandas',
                       'numpy',
                       'nltk',
                       're',
                       'tqdm'])

