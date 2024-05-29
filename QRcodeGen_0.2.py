import subprocess
import sys

def install_and_import(package, friendly_name=None):
    try:
        __import__(package)
        # print(f"The package '{package}' is already installed.")
    except ImportError:
        friendly_name = friendly_name if friendly_name else package
        response = input(f"The package '{friendly_name}' is required but not installed. Would you like to install it? (yes/no): ").strip().lower()
        if response == 'yes':
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            try:
                __import__(package)
            except ImportError:
                print(f"Failed to install {friendly_name}. Exiting.")
                sys.exit(1)
        else:
            print(f"The package '{friendly_name}' is required to run this script. Exiting.")
            sys.exit(1)

# Check and install the required third-party packages
install_and_import('qrcode')
install_and_import('PIL', 'Pillow (a dependency of qrcode)')

# Now import the necessary modules
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

    # img = qr.make_image(fill_color="black", back_color="transparent")
    img = qr.make_image(fill_color=(15, 75, 48), back_color="transparent")
    img.save('QRCode_.png')
    print('Done.')

def getRealTime():
    print('Getting real time')
    now = datetime.now()
    dt_string = now.strftime('%d%m%Y%H%M%S.png')
    return dt_string

make_qrcode()
