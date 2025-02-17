import qrcode
import base64
from io import BytesIO

from django.conf import settings


# converts PIL object from qrcode to base64
def pil_to_b64(obj):
    buffered = BytesIO()
    obj.save(buffered, format="PNG")  # Save image to buffer
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def generate_qrcode(qs):
    # <app_url>/<store_name>/table/<table_id>/
    url = f"{settings.url}/{qs.table.name}/{qs.id}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image()


def base64_qr_code(db_data):
    # generate QR code
    img = generate_qrcode(db_data)
    # convert QR code to base64
    img_in_b64 = pil_to_b64(img)
    return img_in_b64
