#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from playsound import playsound
from time import ctime
import time
from gtts import gTTS

import RPi.GPIO as GPIO

def Khoitao():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = "HDA Intel PCH: ALC269VC Analog (hw:0,0)"
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
    playsound('xinchao.mp3')
    playsound('Truyen1_gioithieu.mp3')
    playsound('Truyen2_gioithieu.mp3')
    playsound('Truyen3_gioithieu.mp3')
    playsound('luachon_gioithieu.mp3')

def Chuyen1():
    print('Sau đây mình sẽ kể câu chuyện Cuộc thi trong rừng ')
    playsound('Truyen1.mp3')
    print('')

def Chuyen2():
    print('Sau đây mình sẽ kể câu chuyện Chú thỏ thông minh ')
    playsound('Truyen2.mp3')
    print('')
def Chuyen3():
    print('Sau đây mình sẽ kể câu Chó sói và đàn dê')
    playsound('Truyen3.mp3')
    print('')

def Moden():
    print("Mở đèn...")
    GPIO.output(25,1)

def Tatden():
    print("Tắt đèn ...")
    GPIO.output(25,0)

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
        playsound('xinloi.mp3')
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "cuộc thi trong rừng" in data:
        Chuyen1()
    elif "Chú Thỏ Thông Minh" in data:
        Chuyen2()
    elif "chó sói và đàn dê" in data:
        Chuyen3()
    elif "Mở đèn" in data:
        Moden()
        playsound('moden.mp3')
    elif "Tắt Đèn" in data:
        Tatden()
        playsound('tatden.mp3')
    elif "what time is it" in data:
        speak(ctime())
def Tieptuc():
    print('Ban có muốn nghe tiếp truyện nào nữa không hay bạn muốn mình tắt đèn để chúng ta cùng đi ngủ ??')
    playsound('tieptuc.mp3')

# initialization
time.sleep(2)
Gioithieu()

while 1:
    data = recordAudio()
    jarvis(data)
    Tieptuc()