import speech_recognition as sr

# create a Recognizer instance
r = sr.Recognizer()

# use the microphone as the source of audio input
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {}".format(e))
