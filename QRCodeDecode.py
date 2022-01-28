#Decode a QR code using PIL and Pyzbar

from PIL import Image
from pyzbar import pyzbar

imgpath = input()

img = Image.open(imgpath)
qr_output = pyzbar.decode(img)
print(qr_output)
