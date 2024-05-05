import speech_recognition as sr
import requests
import json
import tkinter as tk
from tkinter import messagebox
import requests
import win32com.client as wincom

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture the audio
    with sr.Microphone() as source:
        print("Please start speaking...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Call the function to convert speech to text
transcribed_text = speech_to_text()

def get_weather():
    if transcribed_text:
        print("You said:", transcribed_text)
url=f"https://api.weatherapi.com/v1/current.json?key=716fd75ed7794c4092b193925241004&q={transcribed_text}"
r=requests.get(url)
weatherdic=json.loads(r.text)
T=weatherdic["current"]["temp_c"]
C=weatherdic["current"]["condition"]["text"]
TF=weatherdic["current"]["feelslike_c"]
H=weatherdic["current"]["humidity"]
pert=weatherdic["current"]["precip_mm"]
print(f"Temperature in {transcribed_text} "+str(weatherdic["current"]["temp_c"]))
print(f"Condition in {transcribed_text} "+str(weatherdic["current"]["condition"]["text"]))
print(f"Wind_kph in {transcribed_text} "+str(weatherdic["current"]["wind_kph"]))
print(f"precip_mm in {transcribed_text} "+str(weatherdic["current"]["precip_mm"]))
print(f"humidity in {transcribed_text} "+str(weatherdic["current"]["humidity"]))
print(f"current cloud % in {transcribed_text} "+str(weatherdic["current"]["cloud"]))
print(f"feellike temperature in {transcribed_text} "+str(weatherdic["current"]["feelslike_c"]))
speak = wincom.Dispatch("SAPI.SpVoice")
text = f"'the current temperature in {transcribed_text} is {T} centigrade,the current condition is {C} ,the feel like temperature is {TF} Fahrenheit,the humidity in {transcribed_text} is{H} and the precipitation is{pert}'"
speak.Speak(text)


