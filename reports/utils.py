""" Utility code for the report apps"""
import uuid,base64
from django.core.files.base  import ContentFile


def get_report_image(data):
    """ this function takes a base64 encoded string gotten from the formdata image src, and converts it to a file like object that can be saved as a png image"""

    _,str_image = data.split(";base64")
    decoded_image = base64.b64decode(str_image)
    img_name =str(uuid.uuid4())[:10]+".png"
    data = ContentFile(decoded_image,name=img_name)
    return data
