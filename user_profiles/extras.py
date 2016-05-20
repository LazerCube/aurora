import StringIO
from PIL import Image
from django.core.files.base import ContentFile

from django.core.files.uploadedfile import InMemoryUploadedFile
import StringIO

def make_thumbnail(file):
    size = 64, 64
    img = Image.open(file)
    img.thumbnail((size), Image.ANTIALIAS)
    thumbnailString = StringIO.StringIO()
    img.save(thumbnailString, 'JPEG')
    newFile = InMemoryUploadedFile(thumbnailString, None, 'temp.jpg', 'image/jpeg', thumbnailString.len, None)

    return newFile
