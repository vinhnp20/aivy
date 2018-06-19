#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import os, sys
from gtts import gTTS

import RPi.GPIO as GPIO


def Khoitao():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

# NHẬP TÊN MICROPHONE CỦA BẠN
mic_name = "USB PnP Sound Device: Audio (hw:1,0)"

# TỶ LỆ LẤY MẪU LÀ TẦN SUẤT GHI LẠI CÁC GIÁ TRỊ
sample_rate = 48000

# BỘ NHỚ ĐỆM CHUNK, LƯU TRỮ 2048 MẪU
chunk_size = 2048

# KHỞI TẠO HÀM NHẬN DỮ LIỆU ÂM THANH TỪ THƯ VIỆN
r = sr.Recognizer()

# TẠO RA DANH SÁCH CARD ÂM THANH VÀ MICROPHONE CỦA BẠN
mic_list = sr.Microphone.list_microphone_names()

# TÌM SỐ ID CỦA THIẾT BỊ MICROPHONE
# ĐỂ CHẮC CHẮN RẰNG CHÚNG TA CHỌN ĐÚNG MICROPHONE ĐỂ THU DỮ LIỆU ÂM THANH
for i, microphone_name in enumerate(mic_list):
    print(microphone_name)
    if microphone_name == mic_name:
        device_id = i
        print(device_id)


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system('mpg321 audio.mp3')


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
    # os.system('mpg321 Truyen1_gioithieu.mp3 ')
    # os.system('mpg321 Truyen2_gioithieu.mp3 ')
    # os.system('mpg321 Truyen3_gioithieu.mp3 ')
    # os.system('mpg321 luachon_gioithieu.mp3 ')


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
    GPIO.output(24, 1)


def Tatden():
    print("Tắt đèn ...")
    GPIO.output(24, 0)


def recordAudio():
    # NHẬN DẠNG DỮ LIỆU ÂM THANH
    r = sr.Recognizer()
    with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        # ĐỢI MỘT VÀI GIÂY ĐỂ NHẬN RA ĐƯỢC MICROPHONE CỦA CHÚNG TA
        # ĐẶT NGƯỠNG NĂNG LƯỢNG DỰA TRÊN MỨC ĐỘ ỒN XUNG QUANH
        r.adjust_for_ambient_noise(source)
        print("Mời bạn lựa chọn ")
        # LẮNG NGHE CHÚNG TA NÓI
        audio = r.listen(source)

        # NHẬN DẠNG GIỌNG NÓI BẰNG Google Speech Recognition
    data = ""
    try:
        # SỬ DỤNG KEY API MẶC ĐỊNH
        # ĐỂ SỬ DỤNG API KEY KHÁC THÊM CÂU LỆNH: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language="vi-VN")
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
    # if "cuộc thi trong rừng" in data:
        # Truyen1()
        # Tieptuc()
    # elif "Chú Thỏ Thông Minh" in data:
        # Truyen2()
        # Tieptuc()
    # elif "chó sói và đàn dê" in data:
        # Truyen3()
        # Tieptuc()
    # elif "Mở đèn" in data:
        # Moden()
        # os.system('mpg321 moden.mp3 ')
    # elif "Tắt Đèn" in data:
        # Tatden()
        # os.system('mpg321 tatden.mp3 ')
    if "Xin chào" in data:
        playsound('xinchao1.mp3')
    elif "Thỏ ơi" in data:
        playsound('xinchao1_2.mp3')

    elif "Bạn có thể giới thiệu về bản thân được không" in data:
        playsound('xinchao1_2.mp3')

    elif "Thỏ ơi Mình muốn nghe kể chuyện" in data:
        playsound('xinchao1_4.mp3')
    elif "Mình muốn nghe kể chuyện" in data:
        playsound('xinchao1_4.mp3')

    elif "Bạn nói tên một vài câu chuyện được không" in data:
        playsound('xinchao1_5.mp3')
    elif "bạn nói tôi một vài câu chuyện được không" in data:
        playsound('xinchao1_5.mp3')

    elif "Thôi chuyện đó mình nghe rồi" in data:
        playsound('xinchao1_6.mp3')
    elif "mình nghe chuyện đó rồi" in data:
        playsound('xinchao1_6.mp3')

    elif "Ok Vậy bạn kể chuyện cho mình nghe đi" or "nghe cũng được đó" in data:
        print('Sau đây mình sẽ kể câu chuyện Chú thỏ thông minh ')

    elif "Thỏ ơi mình buồn ngủ rồi" in data:
        playsound('xinchao1_7.mp3')
    elif "thôi mình buồn ngủ rồi" in data:
        playsound('xinchao1_7.mp3')

# KHỞI TẠO BAN ĐẦU
Khoitao()
Gioithieu()
ON_OFF = 0

while 1:
    if ON_OFF == 0:
        data = recordAudio()
        jarvis(data)
		if "Tắt Đèn" in data:
            Tatden()
            ON_OFF = 1

    elif ON_OFF == 1:
        data = recordAudio()
        if data == "Mở đèn":
            Moden()
            os.system('mpg321 moden.mp3')
            ON_OFF = 0