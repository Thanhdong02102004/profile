import speech_recognition as sr
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import datetime


now = datetime.now()
r = sr.Recognizer()
def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
while true:

        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            print("Recongnizing...")
            try:
                text = r.recognize_google(audio_data, language="vi")
            except:
                text =""
                print(text)

                if text ==  "":
                    robot_brain = " Tôi đang lắng nghe bạn "
                    speak(robot_brain)
                elif " xin chào" in  text:
                    robot_brain ="Bạn khỏe không"
                    speak(robot_brain)
                elif "Hôm nay là ngày bao nhiêu" in text:
                    robot_brain =now.strftime("hôm nay là ngày %d/%m/%Y %H:%M:%S")
                    speak(robot_brain)
                elif "mấy giờ rồi"  in text:
                    robot_brain =now.strftime("bây giờ là %H:%M:%S")
                    speak(robot_brain) 
                elif "Goodbye" in text:
                    robot_brain =  "Tạm Biệt"
                    speak(robot_brain) 
          
            
                   


