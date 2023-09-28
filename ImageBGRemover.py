from rembg import remove
from PIL import Image

# Arka planı temizlenecek resimin yolu
input_path = "C:\\Users\\anurd\\Downloads\\maymun.jpg"

# Temizlenen resmin kaydedilecek yolu
output_path = "C:\\Users\\anurd\\Downloads\\maymun_bg_remover.png"

# Resmi aç, inp değişkenine at
inp = Image.open(input_path)

# İnp değişkeninin arka planını temizle output değişkenine at
output = remove(inp)

# output değişkeninin belirtilen yola kaydet
output.save(output_path)