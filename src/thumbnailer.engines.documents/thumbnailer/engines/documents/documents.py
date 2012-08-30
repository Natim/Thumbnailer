# -*- coding: utf-8 -*-
from flask import abort
from pydocsplit.docsplit import Docsplit
from pydocsplit.command_runner import RunError
from cStringIO import StringIO
import shutil
import os
from glob import glob
import hashlib
import re

import settings
from thumbnailer.cache import get_thumb_path_for_kwargs, have_cache_for_kwargs

THUMB_CACHE_DIR = getattr(settings, 'THUMB_CACHE_DIR', '/tmp')

def extract_image(file_obj, **kwargs):
    if kwargs['width']:
        if kwargs['height']:
            size = '%dx%d' % (kwargs['width'], kwargs['height'])
        else:
            size = '%dx' % kwargs['width']
    else:
        size = 'x%d' % kwargs['height']

    pdf_name = file_obj.name

    params = kwargs.copy()
    params['page'] = 1
    if have_cache_for_kwargs(**params):
        abort(400, 'Page not found %d' % kwargs['page'])

    # Extract PDF page as images
    os.rename(pdf_name, '%s.pdf' % pdf_name)
    docsplit = Docsplit()
    try:
        docsplit.extract_images(str(pdf_name+'.pdf'), output='/tmp', sizes=[size], formats=['png'])
    except RunError:
        abort(400, 'Please enter a pdf file')
    os.rename('%s.pdf' % pdf_name, pdf_name)


    pngs = list(glob('/tmp/%s/%s*.png' % (size, os.path.basename(pdf_name))))
    # For each page, we create the image in the cache
    for page_png in pngs:
        m = re.search('_(\d+)\.png$', page_png)
        page_number = int(m.group(1))
        params['page'] = page_number
        page_cache_file_path = get_thumb_path_for_kwargs(**params)
        cache_file = open(page_cache_file_path, 'w')
        with open(page_png, 'r') as f:
            cache_file.write(f.read())
        cache_file.close()
        # print page_cache_file_path, params['page']
    print len(pngs)
        
    remove_list = pngs
    for remove_file in remove_list:
        os.remove(remove_file)

    return len(pngs)
