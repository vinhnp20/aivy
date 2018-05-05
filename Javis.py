#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from playsound import playsound
from time import ctime
import time
from gtts import gTTS

# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = "USB Audio Device: - (hw:1,0)"
# Sample rate is how often values are recorded
sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    print(microphone_name)
    if microphone_name == mic_name:
        device_id = i
        print(device_id)

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    playsound('audio.mp3')


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        # listens for the user's input
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I'm feel good today")
    elif "really" in data:
        speak("Sure, My Boss")
    elif "what is my name" in data:
        speak("You are Vinh")

    elif "what time is it" in data:
        speak(ctime())


# initialization
time.sleep(2)
playsound("audio.mp3")
while 1:
    data = recordAudio()
    jarvis(data)