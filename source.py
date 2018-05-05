#Source code Vietnamese

from gtts import gTTS
from playsound import playsound
import threading

tts = gTTS('Hi, Can i help you?, Could you provide me exactly what you want', lang='en')
tts.save('hello.mp3')

"""
def action1():
    playsound('hello.mp3')
def action2():
    print('Success')

threading.Thread(
    target=action1
).start()

threading.Thread(
    target=action2
).start()
"""