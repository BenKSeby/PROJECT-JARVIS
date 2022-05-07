# import time

from mimetypes import init
import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
from web_auto1 import *
from web_automation import *
from word import *
from google_search import *
from translation import *
from internet_speed_test import *
from whatsapp import *
from camera import camera
import os
from weather import *
from digital_clock import *
from briya_birthday import *
from repeat import first1
from news import *
#from introduce_jarvis import introduction, inventionim 
import sys
# os.system("cls")
def initial_conversation():
    rl = sr.Recognizer()
    engine = p.init()
    engine.setProperty("rate", 140)
    engine.say("Hello sir, how are you today?")
    engine.runAndWait()
    with sr.Microphone() as source:
        rl.adjust_for_ambient_noise(source)
        print("how are you today?")
        audio = rl.listen(source)
        try:
            text = rl.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            print("err1 -- please say it again")
            initial_conversation()
        except sr.RequestError as e:
            print("err2")
            initial_conversation()
        except Exception as e:
            print("err3 -- please say it again")
            initial_conversation()

    engine.setProperty("rate", 140)
    engine.say("What would you like me to do?")
    engine.runAndWait()
    print("What do you want?")

    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        audio = r2.listen(source)
        try:
            instruction = r2.recognize_google(audio)
            print(instruction)
        except sr.UnknownValueError:
            print("err1 -- please say it again")
            initial_conversation()
        except sr.RequestError as e:
            print("err2")
            initial_conversation()
        except Exception as e:
            print("err3 -- please say it again")
            initial_conversation()
        r3 = sr.Recognizer()
    if "information" in instruction:
        engine.setProperty("rate", 140)
        engine.say("information about what?")
        engine.runAndWait()
        with sr.Microphone() as source1:
            audio2 = r3.listen(source1)
        try:
            information = r3.recognize_google(audio2)
            bot1 = info()
            bot1.get_info(information)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    # movie rating
    r4 = sr.Recognizer()
    if "review" in instruction:
        engine.setProperty("rate", 140)
        engine.say("What is the name of the movie?")
        engine.runAndWait()
        with sr.Microphone() as source2:
            audio3 = r4.listen(source2)
            try:
                rating = r4.recognize_google(audio3)
                bot2 = Movie()
                bot2.movie_review(rating)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # playing music
    r5 = sr.Recognizer()
    if "music" in instruction:
        engine.setProperty("rate", 140)
        engine.say("which artist should i play?")
        engine.runAndWait()
        with sr.Microphone() as source3:
            audio4 = r5.listen(source3)
            try:
                video = r5.recognize_google(audio4)
                bot3 = Music()
                bot3.play(video)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # getting meaning of a word
    r6 = sr.Recognizer()
    if "meaning" in instruction:
        engine.setProperty("rate", 140)
        engine.say("which word sir?")
        engine.runAndWait()
        with sr.Microphone() as source4:
            audio5 = r6.listen(source4)
            try:
                word = r6.recognize_google(audio5)
                bot4 = Meaning()
                bot4.word_meaning(word)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # getting information from Google
    r7 = sr.Recognizer()
    if "Google" in instruction:
        engine.setProperty("rate", 140)
        engine.say("google search on what sir?")
        engine.runAndWait()
        with sr.Microphone() as source5:
            audio6 = r7.listen(source5)
            try:
                question = r7.recognize_google(audio6)
                bot5 = Google()
                bot5.google_search(question)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # translation
    r8 = sr.Recognizer()
    if "translate" in instruction:
        engine.setProperty("rate", 140)
        engine.say("which word would you like to translate sir?")
        engine.runAndWait()
        with sr.Microphone() as source6:
            audio7 = r8.listen(source6)
            try:
                translation_word = r8.recognize_google(audio7)
                bot6 = Translation()
                bot6.translate_word(translation_word)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # internet speed check
    r9 = sr.Recognizer()
    if "internet" in instruction:
        engine.setProperty("rate", 140)
        engine.say("getting internet speed")
        engine.runAndWait()
        with sr.Microphone() as source20:
            audio20 = r9.listen(source20)
            try:
                check = r9.recognize_google(audio20)
                bot20 = internet()
                bot20.speed(check)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")
    
    
    # whatsapp chat
    r40 = sr.Recognizer()
    if "WhatsApp" in instruction:
        engine.setProperty("rate", 140)
        engine.say("ok sir, setting up whatsapp")
        engine.runAndWait()
        whatsapp_chat()
        #with sr.Microphone() as source40:
            #audio40 = r40.listen(source40)
            #try:
            
                #data = r40.recognize_google(audio40)
                
                #whatsapp_chat()
            #except sr.UnknownValueError:
            #    print("")
            #except sr.RequestError as e:
            #    print("")

    # introduction
    # r41 = sr.Recognizer()
    if "introduce" in instruction:
        engine = p.init()
        engine.setProperty("rate", 140)
        engine.say("Hello, I am your personal AI assistant JARVIS. I am a famous character in marvel studios 'Iron Man' movies where i am a assistant for tony stark.")
        print("Hello, I am your personal AI assistant JARVIS. I am a famous character in marvel studios 'Iron Man' movies where i am a assistant for tony stark.")
        engine.say("I can take your commands and do whatever you want.")
        print("I can take your commands and do whatever you want.")
        engine.say("For example, I can search content in wikipedia and in  google, I can send whatsapp messages, translate words, search meanings of words, play music on youtube, read news for you, check the internet speed and search for movie reviews.")
        print("""For example, I can search content in wikipedia and in  google, I can send whatsapp messages, translate words,
                read news for you, search meanings of words, play music on youtube, check the internet speed and search for movie reviews.""")
        engine.runAndWait()
        time.sleep(3)
        first()

    # # invention
    # r42 = sr.Recognizer()
    # if "invented" or "found" in instruction:
    #     engine = p.init()
    #     engine.setProperty("rate", 140)
    #     engine.say("I was invented by Tony Stark, but I have been recreated by BEN")
    #     print("I was invented by Tony Stark, but I have been recreated by BEN")
    #     engine.runAndWait()
    #     time.sleep(3)
    #     first()

    # taking a photo
    if "photo" in instruction:
        engine.say("setting up camera")
        engine.runAndWait()
        camera()

    # weather app
    if "weather" in instruction:
        engine.say("setting up weather app")
        engine.runAndWait()
        app()

    # clock-digital
    if "what is the time" in instruction:
        engine.say("setting up clock")
        engine.runAndWait()
        clock()
    
    # news 
    r0 = sr.Recognizer()
    if "news" in instruction:
        engine.setProperty("rate", 140)
        engine.say("loading TIMES OF INDIA")
        print("")
        engine.runAndWait()
        with sr.Microphone() as source0:
            audio0 = r0.listen(source0)
            try:
                check = r0.recognize_google(audio0)
                bot0 = News()
                bot0.headlines(check)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # # briya birthday
    # r0 = sr.Recognizer()
    # if "birthday" in instruction:
    #     engine.setProperty("rate", 140)
    #     engine.say("Happy birthday Ben's sister, Briya")
    #     print("Happy birthday Ben's sister, Briya")
    #     engine.runAndWait()
    #     with sr.Microphone() as source0:
    #         audio0 = r0.listen(source0)
    #         try:
    #             check = r0.recognize_google(audio0)
    #             bot0 = Birthday()
    #             bot0.play(check)
    #         except sr.UnknownValueError:
    #             print("")
    #         except sr.RequestError as e:
    #             print("")

    # else
    if "nothing" or "sleep" in instruction:
        engine.setProperty("rate", 140)
        engine.say("ok sir,turning on sleep mode....")
        engine.runAndWait()
        time.sleep(2)
        print("turning on sleep mode")
        time.sleep(2)
        print("TURNED ON 'SLEEP MODE'. Jarvis will come back in five minutes")
        time.sleep(300)
        first1()

    if "shutdown" in instruction:
        engine.setProperty("rate", 140)
        engine.say("shutting down")
        print("shutting down....")
        engine.runAndWait()
        quit()

    else:
        engine.setProperty("rate", 140)
        engine.say("sorry,i didn't understand")
        print("try to say it again")
        first()

from repetition import first

initial_conversation()
