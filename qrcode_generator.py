import qrcode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', action='store', type=str, required=True)
arg = parser.parse_args()

def qrcode_gen(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    print('QrCode saved !')

if __name__ == "__main__":
    
    qrcode_gen(arg)