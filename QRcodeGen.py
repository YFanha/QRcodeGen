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

    f_color = input("Enter fill color (e.g., black, white, or #0F4B30): ").strip()
    b_color = input("Enter back color (e.g., white, transparent, or #FFFFFF): ").strip()

    filename = input("Enter filename : ").strip()
    filename = filename + ".png"

    print("Création du QR code pour l'URL " + url)

    qr.add_data(url)
    qr.make(fit=True)

    #img = qr.make_image(fill_color="black", back_color="transparent")
    img = qr.make_image(fill_color=f_color, back_color=b_color)

    img.save(filename)
    print('Done.')


def getRealTime():
    print('Getting real time')
    now = datetime.now()
    dt_string = now.strftime('%d%m%Y%H%M%S.png')
    return dt_string


make_qrcode()