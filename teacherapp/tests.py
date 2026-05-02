from django.test import TestCase
import os
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

data = 'Present QR Code'
img = qrcode.make(data)
img.save('MyQRCode1.png')
# Create your tests here.

data = decode(Image.open(r'E:\Codebook projects\smart attendance system backend\MyQRCode1.png'))
print(data[0][0])

import qrcode
from django.http import HttpResponse
from django.utils.six import BytesIO

def generate_qr_code(request, data):
    # Generate the QR code image using the qrcode library
    img = qrcode.make(data)
    
    # Create a BytesIO object to write the image to
    buffer = BytesIO()
    img.save(buffer)
    
    # Set the content type of the response to image/png
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    
    return response