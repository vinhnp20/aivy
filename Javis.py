#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from playsound import playsound
from time import ctime
import time
import os, sys
from gtts import gTTS

import RPi.GPIO as GPIO

def Khoitao():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)

# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = "USB PnP Sound Device: Audio (hw:1,0)"
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

def Gioithieu_Text():
    print('Xin chào bạn, mình là robot kể chuyện. Mình có một vài câu chuyện để kể cho bạn như sau:'
          '\n1.Cuộc thi trong rừng'
          '\n2.Chú thỏ thông minh'
          '\n3.Chó sói và đàn dê'
          '\nBạn muốn nghe chuyện nào nè !!'
          '  ')

def Gioithieu():
    Gioithieu_Text()
    os.system('mpg321 xinchao.mp3 ')
    os.system('mpg321 Truyen1_gioithieu.mp3 ')
    os.system('mpg321 Truyen2_gioithieu.mp3 ')
    os.system('mpg321 Truyen3_gioithieu.mp3 ')
    os.system('mpg321 luachon_gioithieu.mp3 ')

def Truyen1():
    print('Sau đây mình sẽ kể câu chuyện Cuộc thi trong rừng ')
    os.system('mpg321 Truyen1.mp3 ')
    print('')

def Truyen2():
    print('Sau đây mình sẽ kể câu chuyện Chú thỏ thông minh ')
    os.system('mpg321 Truyen2.mp3 ')
    print('')
def Truyen3():
    print('Sau đây mình sẽ kể câu Chó sói và đàn dê')
    os.system('mpg321 Truyen3.mp3 ')
    print('')

def Moden():
    print("Mở đèn...")
    GPIO.output(24,1)

def Tatden():
    print("Tắt đèn ...")
    GPIO.output(24,0)

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Mời bạn lựa chọn ")
        # listens for the user's input
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language="vi-VN")
        print("Bạn đã chọn : " + data)
    except sr.UnknownValueError:
        print("Xin lỗi mình nghe không rõ bạn có thể nói lại được không nè ")
        os.system('mpg321 xinloi_gioithieu.mp3 ')
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def Tieptuc():
    print('Ban có muốn nghe tiếp truyện nào nữa không hay bạn muốn mình tắt đèn để chúng ta cùng đi ngủ ??')
    os.system('mpg321 tieptuc.mp3 ')

def jarvis(data):
    if "cuộc thi trong rừng" in data:
        Truyen1()
        Tieptuc()
    elif "Chú Thỏ Thông Minh" in data:
        Truyen2()
        Tieptuc()
    elif "chó sói và đàn dê" in data:
        Truyen3()
        Tieptuc()
    elif "Mở đèn" in data:
        Moden()
        os.system('mpg321 moden.mp3 ')
        ON_OFF=0
    elif "Tắt Đèn" in data:
        Tatden()
        os.system('mpg321 tatden.mp3 ')
        ON_OFF=1
    elif "what time is it" in data:
        speak(ctime())

# initialization
Khoitao()
Gioithieu()
ON_OFF=0

while 1:
    if ON_OFF == 0:
        data = recordAudio()
        jarvis(data)
    
    elif ON_OFF == 1:
        data = r.recognize_google(audio,language="vi-VN")
        if data == "Mở đèn":
            Moden()
            os.system('mpg321 moden.mp3')
            ON_OFF=0

