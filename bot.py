# import pyttsx3
import speech_recognition as sr
import subprocess
# import requests
# import json
# from weather import Speak
from timeParser import get_time, Speak
from quoteParser import Quotes
from gismeteoParser import get_weather
from chatGPT_brain import AI_get_response


def start_sr():
    while True:
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as mic:
                print("...🎙️...\n")
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                # recognizer.energy_threshold(mic,)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio, language='en-US')
                text = text.lower()
                
                if "stop" in text or "bye jarvis" in text or "exit" in text:
                    break
                response(text)
        except sr.UnknownValueError:
            print("Didn't catch that..")
            Speak("Didn't catch that..")
            recognizer = sr.Recognizer()
            continue


def response(text):
    if "open the youtube" in text or "open youtube" in text or " okay open the youtube" in text or "jarvis open the youtube" in text or "jarvis opens youtube" in text:
        Speak('Yeap!')
        # subprocess.Popen(['C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\AutoHotkey Dash.lnk', 'C:\\Users\\Ernar\\Documents\\JarvisBot\\opp.exe'], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run('opp.exe')
    elif "jarvis check the marks" in text or "check the marks" in text or "check marks" in text:
        Speak('Yeap!')
        subprocess.run('markchecker.exe')
    elif "tell me the weather" in text or "weather in" in text or "weather" in text:
        # city_name = str(text.split()[-1])
        # print(city_name)
        # get_weather(city_name, TOKEN)
        get_weather()
    elif "tell me the time" in text or "time" in text:
        get_time()
    else:
        print(f"User: {text} \n")
        respn = AI_get_response(text)
        print(f"Jarvis: {respn}")
        Speak(respn)
        print("\n")
    # elif "tell me a joke" in text or "tell a joke" in text or 'tell joke me' in text or 'me joke tell' in text or 'joke tell me' in text or 'joke me' in text:
    #     Quotes('humor')
    # elif 'list of current films' in text or 'current films' in text:

start_sr()


