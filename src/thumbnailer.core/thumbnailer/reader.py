# -*- coding: utf-8 -*-
"""Read and URL and get the file from cache if possible or update the file."""
from cStringIO import StringIO
import hashlib
import datetime
import settings
import requests
from wsgiref.handlers import format_date_time

INPUT_CACHE_DIR = getattr(settings, 'INPUT_CACHE_DIR', '/tmp')

def get_file_for_url(url):
    """Return the file object related to the URL"""
    hash_id = hashlib.sha256(url).hexdigest()
    headers = {}
    cache_file_path = os.path.join(INPUT_CACHE_DIR, hash_id)
    if os.path.exists(cache_file_path):       
        hash_id_m_time = os.path.getmtime(filename)
        modified_at = datetime.datetime.fromtimestamp(t)
        headers = {'If-Modified-Since': format_date_time(modified_at)}        
    
    req = requests.get(url, headers=headers)

    if req.status_code == 304:
        return open(cache_file_path, 'r')
    else:
        return StringIO(req)
