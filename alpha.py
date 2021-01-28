import speech_recognition as sr
import subprocess
import pyttsx3
import time
import datetime
import pywhatkit
import os
import wikipediaapi
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
newVoiceRate = 138
newVolume = 0.75


def speak(text):
    engine.say(text)
    engine.runAndWait()


engine.setProperty('rate', newVoiceRate)
engine.setProperty('volume', newVolume)


def listen():  
    try:    
        with sr.Microphone() as callsource:
            
            listener.adjust_for_ambient_noise(callsource)
            call = listener.listen(callsource, timeout = 1, phrase_time_limit = 5)
            if call != '':
                callcommand = listener.recognize_google(call)
            else:
                print('No command')
            callcommand = callcommand.lower()
            print("RawCallCommand: " + callcommand)

            if 'alpha' in callcommand:
                print('Called')
                try:

                    with sr.Microphone() as commandsource:
            
                        print('Alpha is Online...')
                        playsound('activate.mp3')
                        listener.adjust_for_ambient_noise(commandsource)
                        voice = listener.listen(commandsource, timeout = 5, phrase_time_limit = 45)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                        print("RawCommand: " + command)
                        command = command.replace('hey alpha', '')
                        command = command.replace('please', '')
                        playsound('deactivate.wav')
                        
                        if 'time' in command:
                            now = datetime.datetime.now()
                            speak('It is' + str(now.hour) + ' ' + str(now.minute))
                        elif 'date' in command:
                            now = datetime.datetime.now()
                            speak('Today is' + ' ' +  str(now.day) + ' ' + str(now.month) + ' ' + str(now.year))
                        elif 'play' in command:
                            song = command.replace('play', '')
                            if 'on youtube' in song:
                                song = song.replace('on youtube', '')
                                print(song)
                                speak('playing' + song)
                                pywhatkit.playonyt(song)
                        elif 'search for' in command:
                            search = command.replace('search for', '')
                            wiki_wiki = wikipediaapi.Wikipedia('en')
                            page_py = wiki_wiki.page(search)
                            speak(page_py.summary[0:300])  
                        elif 'open' in command:
                            app = command.replace('open', '')
                            speak('opening' + app)
                            if 'calculator' in app:
                                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                            elif 'netflix' in app:
                                os.startfile(r"D:\joshua\netflix.lnk")
                            elif 'code' in app:
                                os.startfile(r"D:\Joshua\Amarok\#Downloads\#VSCode\Microsoft VS Code\Code.exe")
                            elif 'unity' in app:
                                os.startfile(r"Desktop\Unity.lnk")
                            elif 'chrome' in app:
                                os.startfile(r"Desktop\Chrome.lnk")
                        else:
                            speak('It seems like I was not coded for that yet')
                except:
                    print('command_exception')
                    playsound('error.wav')
            else:
                print('not calling')    
    except:
        pass
        
        

