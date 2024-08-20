import qrcode


def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    name = input("Enter the name for your QR Code PNG (file extension .png will be added for you): ")
    img.save(name + '.png')
    return name + '.png'


def main():
    url = input("Enter the URL to encode in the QR code: ")
    generate_qr_code(url)


if __name__ == '__main__':
    main()
