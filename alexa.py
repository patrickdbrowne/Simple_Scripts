# pip install pyttsx3
# pip install speech_recognition
import webbrowser
import speech_recognition as sr
import pyttsx3
import os 
import subprocess as sp
global engine 
engine = pyttsx3.init('sapi5')
def speak(words):
    engine.say(words)
    engine.runAndWait()
def Greetings():
    speak("Hello Boss")
    speak("I'm Jarvis, version 1.1. How may I assist you today!")
def GiveCommands():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        print("Give Commands...")
        r.pause_threshold = 1
        audio = r.listen(s)
        words = r.recognize_google(audio)
    return words

def FollowCommands(words):
    if "open medium" in words:
        speak("sure sir")
        webbrowser.open("medium.com")
    
    elif "open google" in words:
        speak("Opening Google")
        webbrowser.open("google.com")
    elif "run notepad" in words:
            sp.Popen(["notepad.exe"])
    elif "open youtube" in words:
            webbrowser.open("youtube.com")
    elif "launch google" in words:
            sp.Popen(['chrome.exe'])
    elif "shutdown" in words:
            exit()
    Greetings()

while True:
    query = GiveCommands()
    FollowCommands(query.lower())