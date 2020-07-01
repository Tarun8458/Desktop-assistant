import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")  
    
    speak("I am Edge Sir. I am your Desktop Assistant")    
    speak("Please tell me what can i do for you")      

def  takeCommand():
    #take microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None" 
    return query          
        
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:    
        query = takeCommand().lower()
        #logic  for executing task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\phone mp3'
            songs = os.listdir(music_dir)
            #print(songs)
            value = random.randint(0,50)    
            os.startfile(os.path.join(music_dir, songs[value]))
      

        elif 'the time ' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Devil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play friends' in query:
            friends_dir = 'E:\\Web Series\\F.R.I.E.N.D.S\\Friends Season 2 COMPLETE.720p.BRrip.sujaidr (pimprg)'
            video = os.listdir(friends_dir)
            value2 =random.randint(2,25) 
            os.startfile(os.path.join(friends_dir, video[value2]))  
