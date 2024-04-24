import googletrans as gt
import speech_recognition as sr 
import gtts as g
import playsound as ps
import os
print(gt.LANGUAGES)# for showing list of language  
inputlang=input("enter the input languaga")
outputlang=input("enter the output lang")


#convert voice to text 
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("spek now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language=inputlang)
    print(text)
#convert text to voice
translator=gt.Translator()
translation=translator.translate(text,dest=outputlang)
print(translation.text)
converted_audio=g.gTTs(translation.text,lang=outputlang)
converted_audio.save("hello.mp3")
ps.playsound("hellow.mp3")
#remove the voice file atomatacaly  after playing
os.remove("hellow.mp3")







