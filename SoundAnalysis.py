import time
import speech_recognition as sr
import feedparser

r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        r.adjust_for_ambient_noise(source)
        data = r.record(source, duration=5)
        print("Sesiniz Tanımlanıyor...")
        text = r.recognize_google(data, language='tr')
        if "deneme" in text.lower():
            print("Tamam Ayşenur")
        elif "bubble" in text.lower():
            print("Efendim Ayşenur")
        elif "saat" in text.lower():
            print("Saat " + str(time.localtime().tm_hour) + "'i " + str(time.localtime().tm_min) + " geçiyor.")
        elif "hava durumu" in text.lower():
            print("Hangi ildesin Ayşenur?")
        else:
            print("Ne demek istediğiniz anlamadım.")


# locCode=EUR|TR|06420|ANKARA| > KITA|ULKE|POSTAKODU|IL
def hava(il):
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|06420|{}|" & il)
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[2], parse[4], parse[5])
    return (hava)



