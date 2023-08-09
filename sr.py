# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:37:48 2023

@author: muckr
"""

import speech_recognition as sr

speech = sr.Recognizer()
while True:
    print("Python is listening...")
    inp = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
        print(f'You just said: {inp}.')
    if inp == "stop listening":
        print("Goodbye!")
        break