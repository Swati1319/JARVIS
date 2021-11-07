import pyttsx3
import datetime
import requests
import speech_recognition as sr 
import wikipedia
import smtplib
import pywhatkit as kit
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import cv2
import random
from requests import get
from email.message import EmailMessage
from myids import my_gmail,password,destination
from mynumbers import num
import sys
import pyautogui
import time


p = password
g = my_gmail
d = destination
n = num

 
 
engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def T_time():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("the current time is")
        speak(Time)



def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("Welcome back  mam!")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <=12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")

    
    speak("Jarvis at your service. How I can Help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source , timeout=1 ,phrase_time_limit=5)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"User Said : {query}")

    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "None"

    return query

def email_info():
    speak('To whom you want to send the email ')
    nam = takeCommand()
    receiver = d[nam]
    speak('What is the subject of your email')
    subject = takeCommand()
    speak('Tell me the text in your email')
    message =takeCommand()
    sendemail(receiver,subject,message)


def sendemail(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(g,p)
    email = EmailMessage()
    email['From'] = g
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C://Users//ss040//OneDrive//Pictures//Jarvis//ss.jpeg")

def cpu():
    usage = str(psutil.cpu_percent())
    print("CPU is at" + usage)
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    print("battery is at ")
    print(battery.percent)
    speak("battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())

def message():
    speak('To whom you want to whatsapp ')
    person = takeCommand()
    phn = n[person]
    speak('Tell me the text in your message')
    wmsgs =takeCommand()
    print(wmsgs)
    kit.sendwhatmsg(phn,wmsgs,19,27)

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=734651fe9a474684b31b7c443efa2a28'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

    





if __name__ == "__main__":
    wishme()

    while True:
    #if 1:
        query = takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace("wikipedia" ,"")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif "time" in query:
            T_time()

        elif "date" in query:
            date()

        elif "send email" in query:
            try:
                email_info()
                speak("The mail was sent successfully")
                speak('Do you want to send more email?')
                send_more = takeCommand()
                if 'yes' in send_more:
                    email_info()

            except Exception as e:
                print(e)
                speak("Sorry Swati . I am not able to send this mail at this point of time")

        elif "message" in query:
            message()

        elif "search in chrome" in query:
            speak("What Should I search?")
            chromepath = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "play song" in query:
            songs_dir = "D:\songs"
            songs = os.listdir(songs_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(songs_dir,rd))

        elif "remember that" in query:
            speak("What should I remember")
            data = takeCommand()
            speak("You said me to remember"+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("You said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "play on youtube" in query:
            speak('Which song you want to listen ')
            fav = takeCommand()
            kit.playonyt(fav)
            speak('Playing' + fav)

        elif "open notepad" in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img =cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(10)
                if k==7:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip =get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(f"your IP address is {ip}")

        elif "open google" in query:
            speak("What should I search on google")
            cm = takeCommand().lower()
            wb.open(f"{cm}")

        elif "close notepad" in query:
            speak('Okay mam, close notepad')
            os.system("taskkill /f /im notepad.exe")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "D:\songs"
                son = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,son[0]))

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait mam, fetching the latest news")
            news()

        elif "offline" in query:
            speak("thanks for interacting, have a good day!")
            sys.exit()

        speak("Do You Want me to do something more for you")
