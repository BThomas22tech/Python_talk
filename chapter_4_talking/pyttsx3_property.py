# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:23:41 2023

@author: muckr
"""

import pyttsx3

engine = pyttsx3.init()
voices =engine.getProperty('voices')
for voice in voices:
    print(voice)
    
rate = engine.getProperty('rate')
print('the default speed of the speech is',rate)
vol = engine.getProperty('volume')
print('the default volume of the speech is',vol)

