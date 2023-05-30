import pyttsx3
import speech_recognition as sr

cusName =pyttsx3.init()
cusName.say('hello. my name is Mirza. what is your name?')
cusName.runAndWait()
name = sr.Recognizer()

with sr.Microphone()as source :
    sayName = name.listen(source)
    try:
        fullName = name.recognize_google(sayName)
    except:
        text_speech = pyttsx3.init()
        answer = 'sorry, the audio was not recognized'
        text_speech.say(answer)
        text_speech.runAndWait()

saySth = sr.Recognizer()
with sr.Microphone() as source:
    audio = pyttsx3.init()
    audio.say(f"Hello to my friend {fullName}. i am happy to talk with you")
    audio.say('say something and i can write it!')
    audio.runAndWait()
    audio = saySth.listen(source)
    try:
        text = saySth.recognize_google(audio)
        print(f'you said:{text}')
        if text == "what can you do":
            text_speech = pyttsx3.init()
            answer = "i can write everything you say"
            text_speech.say(answer)
            text_speech.runAndWait()

        if text == "what is your name" or text == "what's your name":
            text_speech = pyttsx3.init()
            answer = "my name is Mirza"
            text_speech.say(answer)
            text_speech.runAndWait()
    except:
        text_speech = pyttsx3.init()
        answer = 'sorry, the audio was not recognized'
        text_speech.say(answer)
        text_speech.runAndWait()
