#Generate a QR code

import qrcode
link = input()
img = qrcode.make(link)
img.save("QRCode-generator.png")
