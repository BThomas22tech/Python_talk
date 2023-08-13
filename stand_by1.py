# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:39:15 2023

@author: muckr
"""

from mysr import voice_to_text

while True:
    print("Python is Listening...")
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "quit the script":
        print("Have a great day!")
        break
    