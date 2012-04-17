# -*- coding: utf-8 -*-
from flask import abort
from pydocsplit.docsplit import Docsplit
from pydocsplit.command_runner import RunError
from tempfile import NamedTemporaryFile
from StringIO import StringIO
from engines.utils import download_from_url
import shutil
import os
from glob import glob

def extract_image(url, width, height):
    data = download_from_url(url)
    path, ext = os.path.splitext(url)
    docsplit = Docsplit()
    tmp = NamedTemporaryFile()
    pdf_name = u'%s%s' % (tmp.name, ext)

    with open(pdf_name, 'wb') as f:
        f.write(data.getvalue())

    if width:
        if height:
            size = '%dx%d' % (width, height)
        else:
            size = '%dx' % width
    else:
        size = 'x%d' % height

    try:
        docsplit.extract_images(str(pdf_name), output='/tmp', sizes=[size], formats=['png'], pages=[1])
    except RunError:
        abort(400, 'Please enter a pdf file')

    filename, ext = os.path.splitext(pdf_name)

    io = StringIO()
    png = '/tmp/%s/%s_1.png' % (size, os.path.basename(filename))
    with open(png) as f:
        io.write(f.read())

    for remove_file in list(glob('/tmp/%s/%s*' % (size, filename))) + list(glob('/tmp/%s*' % filename)):
        print remove_file
        os.remove(remove_file)
    tmp.close()

    return io.getvalue()
