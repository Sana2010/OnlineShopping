import googletrans
import speech_recognition
import gtts
import playsound

recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language="fr")
    print(text)
translator=googletrans.Translator()
translation=translator.translate(text,dest="fr")
print(translation.text)
converted_voice=gtts.gTTS(translation.text,"fr")
converted_voice.save("hello.mp3")
playsound.playsound("hello.mp3")