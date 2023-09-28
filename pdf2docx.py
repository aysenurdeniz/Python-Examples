# pip install pdf2docx


# Dönüştürülecek pdf dosyası
from pdf2docx import Converter

pdf_file = "C:\\Users\\anurd\\Downloads\\Danisman.Tercih.pdf"

# Kaydedilecek docx dosyası
docx_file = "C:\\Users\\anurd\\Downloads\\Response-to-Reviewers.docx"

# pdf_file için cv Converter nesnesi oluştur
cv = Converter(pdf_file)

# oluşturulan cv nesnesini docx_file dosyasına çevir
cv.convert(docx_file)

# dosyayı kapat
cv.close()
