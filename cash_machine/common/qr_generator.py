import qrcode
from io import BytesIO


def generate_qr(data: str):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        return img_bytes.getvalue()
    except Exception as e:
        raise Exception(f"Failed to generate QR code: {str(e)}")
