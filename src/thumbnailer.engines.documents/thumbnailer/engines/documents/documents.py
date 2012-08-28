# -*- coding: utf-8 -*-
from flask import abort
from pydocsplit.docsplit import Docsplit
from pydocsplit.command_runner import RunError
from cStringIO import StringIO
import shutil
import os
from glob import glob

def extract_image(file_obj, url, width, height):
    if width:
        if height:
            size = '%dx%d' % (width, height)
        else:
            size = '%dx' % width
    else:
        size = 'x%d' % height

    pdf_name = file_obj.name

    try:
        docsplit.extract_images(str(pdf_name), output='/tmp', sizes=[size], formats=['png'], pages=[1])
    except RunError:
        abort(400, 'Please enter a pdf file')

    io = StringIO()
    png = '/tmp/%s/%s_1.png' % (size, os.path.basename(pdf_name))
    with open(png) as f:
        io.write(f.read())

    for remove_file in list(glob('/tmp/%s/%s*' % (size, pdf_name))) + list(glob('/tmp/%s*' % pdf_name)):
        print remove_file
        os.remove(remove_file)
    tmp.close()

    return io.getvalue()
