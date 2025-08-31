import qrcode

def generate_qr_code(url, filename="my_qr_code.png"):
    """
    Generates a QR code from a URL and saves it as an image file.

    Args:
        url (str): The URL you want the QR code to point to.
        filename (str, optional): The name of the output image file.
                                  Must be a .png for transparency.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    # badel il star hetha ach t7eb
    img = qr.make_image(fill_color="#000000", back_color="white")
    img.save(filename)
    print(f"Successfully generated QR code and saved it as '{filename}'")

if __name__ == "__main__":
    # This URL points ONLY to the Google Drive file.
    URL_TO_ENCODE = "YOUR_URL"

    OUTPUT_FILENAME = "SB_LINKEDIN_qr_code.png"

    generate_qr_code(URL_TO_ENCODE, OUTPUT_FILENAME)