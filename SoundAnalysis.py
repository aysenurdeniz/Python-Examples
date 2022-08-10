import time
import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        r.adjust_for_ambient_noise(source)
        data = r.record(source, duration=5)
        print("Sesiniz Tanımlanıyor...")
        text = r.recognize_google(data, language='tr')
        if "deneme" in text.lower():
            print("Tamam Ayşenur")
        if "bubble" in text.lower():
            print("Efendim Ayşenur")
        if "saat" in text.lower():
            print("Saat " + str(time.localtime().tm_hour) + "'i " + str(time.localtime().tm_min) + " geçiyor.")
