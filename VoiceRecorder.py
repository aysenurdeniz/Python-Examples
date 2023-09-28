# pip install sounddevice

import sounddevice
from scipy.io.wavfile import write

# Frekans ayarları için - kalite
fs = 44100

# Ne kadar süre kayıt yapılacak?
second = int(input("Kac saniye kayit yapacaksınız: "))
print("Kaydediliyor...")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("rec_name.wav", fs, record_voice)

print("Success process...")