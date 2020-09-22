#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup

setup(name='pantex',
      packages = ['pantex'],
      version= '0.0.1',
      description= 'text cleaning package for use on pandas dataframes and lists',
      url='https://github.com/halmga/pantext',
      download_url = 'https://github.com/halmga/pantext/archive/0.0.1.tar.gz',
      author='halmga',
      license='MIT',
      install_requires= ['pandas','nltk','tqdm']
      classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', # Your License Here  
        'Programming Language :: Python :: 3',    # List Python versions that you support Here  
        'Programming Language :: Python :: 3.4',
        ],
)
