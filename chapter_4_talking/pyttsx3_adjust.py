# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:28:19 2023

@author: muckr
"""

import pyttsx3

engine = pyttsx3.init()
voice_id = 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.2)
engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait()
