# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:35:44 2023

@author: muckr
"""

import platform

if platform.system() == "Windows":
    import pyttsx3
    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.2)
    
    def print_say(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()