import qrcode
from PIL import Image

def make_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    url = input("Enter the URL: ").strip()

    f_color = input("Enter fill color (e.g., black, white, or #0F4B30): ").strip()
    b_color = input("Enter background color (e.g., white, transparent, or #FFFFFF): ").strip()

    filename = input("Enter filename (without extension): ").strip()
    filename = filename + ".png"

    print("Creating the QR code for the URL:", url)

    qr.add_data(url)
    qr.make(fit=True)

    try:
        img = qr.make_image(fill_color=f_color, back_color=b_color)
    except ValueError as e:
        print(f"Error with color values: {e}")
        return

    img.save(filename)
    print('QR code created and saved as', filename)

make_qrcode()
