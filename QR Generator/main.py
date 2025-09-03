import qrcode
import string
from gen import codeGen

def qrGen(data):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    label= str.maketrans('','',string.punctuation)
    return img.save(f'{data.translate(label)}.png')

def main():
    data = codeGen()
    qrGen(str(data))
main()