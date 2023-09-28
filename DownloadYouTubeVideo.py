# pip install yt-dlp
import yt_dlp

url = input("Indirmek istediğiniz video yolunu giriniz: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video basarılı bir sekilde indirildi.")