import urllib.request, io, PyPDF2
import pandas as pd


url = "C:\\Users\\anurd\\Downloads\\en_Sahih_Muslim.pdf"
remoteFile = urllib.request.urlopen(url)
pdfReader = PyPDF2.PdfFileReader(io.BytesIO(remoteFile.read()))

from PyPDF2 import PdfReader
# path="C:\\Users\\anurd\\Downloads\\new_similarity_report.pdf"
pdfObj=open(url,"rb")
pdfRead= PdfReader(pdfObj)
page = list()


for i in range(len(pdfRead.pages)):
    with open('en_Sahih_Muslim.txt', 'a+') as file:
        page.append(pdfRead.pages[i].extract_text())
        file.write(page[i])

for i in range(len(pdfRead.pages)):
    with open('en_Sahih_Muslim.txt', 'a+') as file:
        page.append(pdfRead.pages[i].extract_text())
        file.write(page[i])