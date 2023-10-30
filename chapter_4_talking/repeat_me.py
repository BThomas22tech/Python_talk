# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:05:25 2023

@author: muckr
"""
from mysr import voice_to_text
import platform

if platform.system() =="Windows":
    import pyttsx3
    engine = pyttsx3.init()
else:
    import os
    
while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print(f"You just said {inp}; goodbye!")
        if platform.system() == "Windows":
            engine.say(f"You just said {inp}; goodbye!")
            engine.runAndWait()
            break
    else:
        print(f'You just said {inp}')
        if platform.system() == "Windows":
            engine.say(f'You just said {inp}')
            engine.runAndWait()
            