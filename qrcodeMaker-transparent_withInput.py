from time import time
from turtle import done
import qrcode
from datetime import datetime

def make_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=25,
    )

    url = input("Entrez l'URL voulu : ")

    print("Création du QR code pour l'URL " + url)

    qr.add_data(url)
    qr.make(fit=True)

    #img = qr.make_image(fill_color="black", back_color="transparent")
    img = qr.make_image(fill_color="white", back_color="transparent")
    img.save('QRCode_.png')
    print('Done.')


def getRealTime():
    print('Getting real time')
    now = datetime.now()
    dt_string = now.strftime('%d%m%Y%H%M%S.png')
    return dt_string


make_qrcode()