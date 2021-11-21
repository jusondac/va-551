# Python program speech recognizer by rejka

import speech_recognition as sr
import pyttsx3

# initialize the recognizer

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            if 'exit' in MyText:
                exit()

    except sr.RequestError as e:
        print("could not request result; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
