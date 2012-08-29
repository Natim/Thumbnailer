# -*- coding: utf-8 -*-
from flask import abort
from pydocsplit.docsplit import Docsplit
from pydocsplit.command_runner import RunError
from cStringIO import StringIO
import shutil
import os
from glob import glob
import hashlib
import settings

THUMB_CACHE_DIR = getattr(settings, 'THUMB_CACHE_DIR', '/tmp')

def extract_image(file_obj, url, width, height):
    if width:
        if height:
            size = '%dx%d' % (width, height)
        else:
            size = '%dx' % width
    else:
        size = 'x%d' % height

    pdf_name = file_obj.name
    png = '/tmp/%s/%s_1.png' % (size, os.path.basename(pdf_name))

    # Extract PDF page as images
    os.rename(pdf_name, '%s.pdf' % pdf_name)
    docsplit = Docsplit()
    try:
        docsplit.extract_images(str(pdf_name+'.pdf'), output='/tmp', sizes=[size], formats=['png'], pages=[1])
    except RunError:
        abort(400, 'Please enter a pdf file')
    os.rename('%s.pdf' % pdf_name, pdf_name)
        
    hash_id = hashlib.sha256(url).hexdigest()
    cache_file_path = os.path.join(THUMB_CACHE_DIR, hash_id)
    io = open(cache_file_path, 'wb')
    with open(png) as f:
        io.write(f.read())

    remove_list = list(glob('/tmp/%s/%s*' % (size, os.path.basename(pdf_name)))) + list(glob('/tmp/%s*' % os.path.basename(pdf_name)))
    remove_list.remove(png)

    for remove_file in remove_list:
        os.remove(remove_file)

    io.seek(0)

    return io
