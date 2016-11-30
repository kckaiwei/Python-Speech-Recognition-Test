#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_sphinx(audio)
        print text
        if str(text).lower() == "exit program":
            stop_listening()
        else:
            pass
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

r = sr.Recognizer()
#seconds of non-speaking audio to keep on both sides
r.non_speaking_duration = 0.1
#Must be equal or larger than non_speaking_duration
r.pause_threshold = 0.1
#Getting a faster reaction by considering 0.2s a phrase
r.phrase_threshold = 0.2

m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

print "Starting Recording"
stop_listening = r.listen_in_background(m, callback)
