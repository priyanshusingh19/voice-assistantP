import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint
import smtplib
import wikipedia 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        print("Good Morning Sir!!")
        speak("good morning sir !")

    elif h>=12 and h<17 :
        print("Good Afternoon Sir!!")
        speak("good afternoon sir")   

    else:
        print("Good Evening Sir!!")
        speak("Good Evening Sir") 

    print(" i am your assistant. Please tell how can i help you")
    speak(" i am your assistant . Please tell how can i help you") 


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query =  r.recognize_google(audio,language='en-in')
        print("user said", query)

    except Exception as e:
        print(e)
        print(" say that again please....")
        return "None"

    return query



def sendemail(add,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    #in place of email address please enter your complete email address
    #in place of password please use your gmail password for sending mail through assistant
    server.login('email address','password')
    server.sendmail('email address',add,msg)
    print("email has been sent ")
    speak("email has been sent")
    server.close()


     


if __name__ == '__main__':
    wish()
    while(True):
        query= takecommand().lower()



        if 'wikipedia' in query:
            speak('seraching......')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("Acoording to wikipedia")
            print(results)
            speak(results)

        if 'tell me about' in query:
            try:
                speak('seraching......')
                query=query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=3)
                speak("Acoording to wikipedia")
                print(results)
                speak(results) 

            except:
                print("i am not getting any info about your query")
                speak("i am not getting any info about your query")       

       
        elif 'open you tube' in query:
            webbrowser.open("youtube.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'play music' in query:
            m_dir='E:\\songs'
            songs=os.listdir(m_dir)
            os.startfile(os.path.join(m_dir,songs[randint(0,(len(songs)-1))]))      


        elif 'search' in query:
            query=query.replace("search","")
            webbrowser.open(query)

        elif 'tell me about' in query:
            query=query.replace("tell me about","")
            results = wikipedia.summary(query,sentences=2)
            #speak("Acoording to wikipedia")
            print(results)
            speak(results)  

        elif 'open vs code' in query:
            path="C:\\Users\\rajat\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)


        elif 'send message' in query:
            try:
                print("please enter receiver adress\n listening........") 
                speak("please enter receiver adress")
                add=input()
                print("what is the message ?? \n listening.........")
                speak("what is the message")
                msg=takecommand()
                sendemail(add,msg)

            except Exception as e:
                print(e)
                speak("sorry i am not able to send the messagde")
                print("sorry i am not able to send the messagde")

        elif 'send email' in query:
            try:
                print("please enter receiver adress") 
                speak("please enter receiver adress")
                add=input()
                print("what is the message ??")
                speak("what is the message")
                msg=takecommand()
                sendemail(add,msg)

            

            except Exception as e:
                print(e)
                speak("sorry i am not able to send the messagde")
                print("sorry i am not able to send the messagde")        


        elif 'send text' in query:
            try:
                print("please enter receiver adress\n") 
                speak("please enter receiver adress")
                add=takecommand().lower
                print("what is the message ??")
                speak("what is the message")
                msg=takecommand().lower
                sendemail(add,msg)

            

            except Exception as e:
                print(e)
                speak("sorry i am not able to send the message")
                print("sorry i am not able to send the message")




        elif 'thank you' in query:
            print(" your welcome")
            speak("your welcome")
        




        elif 'bye' in query:
            print("Bye Sir!!!")
            speak('Bye Sir')
            exit()



