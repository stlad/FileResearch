import datetime
from PIL import Image
from PIL.ExifTags import TAGS

import ffmpeg

from PyPDF2 import PdfFileReader

import docx

def get_image_meta(imagename):
    image = Image.open(imagename)
    exifdata = image.getexif()
    res = {}
    for tag_id in exifdata:
        # получить имя тега вместо идентификатора
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # декодировать байты
        if isinstance(data, bytes):
            data = data.decode()
        res[tag] = data
    return res

def get_vid_meta(videoname):
    return ffmpeg.probe(videoname)


def get_pdf_meta(pdfname):
    with open(pdfname, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
    return info

def ger_docx_meta(docname): # вооще из дока можнов вытащить все что у годно. тут только минимум
    doc = docx.Document(docname)
    props = doc.core_properties
    info ={
        'Author':props.author,
        'Last modified by': props.last_modified_by,
        'Creation Date':f'{props.created.day}.{props.created.month}.{props.created.year}',
        'Last Mod Date':f'{props.modified.day}.{props.modified.month}.{props.modified.year}',
        'Last Print Date':f' {props.last_printed}',
        'Saves Count':props.revision
    }
    return info