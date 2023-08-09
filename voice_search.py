# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:39:15 2023

@author: muckr
"""

import webbrowser
import speech_recognition as sr

speech = sr.Recognizer()

def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input

while True:
    print("Python is Listening...")
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print("Goodbye!")
        break
    elif "browser" in inp:
        inp = inp.replace('browser ',"")
        webbrowser.open("http://google.com/search?q="+inp)
        continue