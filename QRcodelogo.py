import qrcode
from PIL import Image


Logo_Link = "csumb.jpg"
logo = Image.open(Logo_Link)
logo = logo.convert("RGBA") #converts to RGBA so we can make transparent
basewidth = 100
wpercent = basewidth / float(logo.size[0])
hsize = int(logo.size[1] * float(wpercent))
logo = logo.resize((basewidth, hsize))

QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
url = "https://www.youtube.com/watch?v=L7vXZ1BnTBI"
QRcode.add_data(url)

QRimg = QRcode.make_image(fill_color='green', back_color='white').convert('RGBA')
diff = (QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2
QRimg.paste(logo, diff, logo)
QRimg.save("mynewQRcode.png")
img = Image.open("mynewQRcode.png")
img.show()

