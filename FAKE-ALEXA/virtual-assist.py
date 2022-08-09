import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from sys import exit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # ustawienie glosu na damski

# odzywka
def talk(text):
    engine.say(text)
    engine.runAndWait()

# wysluchanie komendy 
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '') # usuwanie slowa alexa z komendy
                print(command)
    except:
        pass
    return command

# main
def run_alexa():
    command = take_command()
    print(command)
    
    # odpalanie piosenki na yt
    if 'play' in command:
        song = command.replace('play', '') # usuwanie slowa play z komendy
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    # pytanie o aktualna godzine
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
        
    # wyszukiwanie osob na wikipedii
    elif 'who is' in command:
        person = command.replace('who is', '') # usuwanie slow who is z komendy
        info = wikipedia.summary(person, 1) # wyszukiwanie na wikipedii i podanie pierwszej linii informacji
        print(info)
        talk(info)
        
    # opowiadanie zartu
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    
    # pozegnanie i wylaczenie programu
    elif 'sayonara' in command:
        print('Bay bay')
        talk('Bay bay')
        exit(0)
        
    # niezrozumiana komenda
    else:
        print('Please repeat')
        talk('Please repeat')

while True:       
    run_alexa()