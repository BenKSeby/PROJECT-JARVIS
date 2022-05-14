import pyautogui as py
import speech_recognition as sr
import pyttsx3 as p


def apploader():
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        audio = r2.listen(source)
        try:
            instruction = r2.recognize_google(audio)
            print(instruction)
        except sr.UnknownValueError:
            print("err1 -- please say it again")
            apploader()
        except sr.RequestError as e:
            print("err2")
            apploader()
        except Exception as e:
            print("err3 -- please say it again")
            apploader()
    try:
        py.hotkey('winleft', 's')
        py.typewrite(instruction)
        py.press('right')
        py.press('enter')
        from repeat import first1
        first1()
    except:
        from repeat import first1
        first1()
