import os
import platform
import pathlib
import speech_recognition as sr

speech = sr.Recognizer()
directory = pathlib.Path.cwd()

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

def open_file(filename):
    if platform.system() == "Windows":
        os.system(f"explorer {directory}\\files\\{filename}")
while True:
    print("Python is Listening...")
    inp = voice_to_text().lower()
    print(f'You just said {inp}.')
    if inp == "quit the script":
        print("Have a great day!")
        break
    elif "open pdf" in inp:
        inp = inp.replace('open pdf ','')
        myfile = f'{inp}.pdf'
        open_file(myfile) 
        continue


