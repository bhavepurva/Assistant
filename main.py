import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia as wiki
import webbrowser
import os
import smtplib

#initializing
engine = pyttsx3.init()

#setting properties voices is list, 0 for male 1 for female
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

wiki.set_lang("en")

#defining speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#microphone input
def commands():
    recognize=sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        recognize.adjust_for_ambient_noise(src, duration=1)

        audio=recognize.listen(src)
        audio_input=""

    try:
        print("Recognizing...")
        audio_input=recognize.recognize_google(audio,language="en-in")
        print(f"Your command: {audio_input}\n")
    except Exception as e:
        speak("Say that again please...")
        print(str(e))

    return audio_input

#pulls wikipedia articles
def wikipedia_articles(audio_input):
    speak("searching wikipedia")
    audio_input = audio_input.replace("wikipedia", "")
    result = wiki.summary(audio_input, sentences=5)
    speak(result)
    print(result)

#send email
def sendEmail():
    speak()

if __name__=="__main__":
    speak("Welcome")
    date=datetime.datetime.now().date()

    speak("Today is "+str(date))

    while True:
        audio_input=commands().lower()
        if "hello" in audio_input:
            speak("hii bitch")
        elif "date" in audio_input:
            speak(str(date))
        elif "time" in audio_input:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif "name" in audio_input:
            speak("My name is assistant.")

        elif "wikipedia" in audio_input:
            wikipedia_articles(audio_input)
        elif "youtube" in audio_input:
            speak("Launching youtube")
            audio_input=audio_input.replace("open youtube and play","")
            audio_input=audio_input.replace(" ","")
            webbrowser.open("http://www.youtube.com/"+audio_input)
            speak("enjoy")
        elif "google" in audio_input:
            speak("Launching google")
            webbrowser.open("https://www.google.com/"+audio_input.replace(" ",""))
        elif "play music" in audio_input:
            speak("starting music player")
            music_path="F:\songs\sick beats" #get path of music dir
            songs=os.listdir(music_path) #list of all songs in that dir
            os.startfile(os.path.join(music_path,songs[0])) #play first song
        elif "open notepad" in audio_input:
            path=r"C:\Users\Aarya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad"
            os.startfile(path)
        # elif "send email" in audio_input:
        #     try:

        else:
            pass





