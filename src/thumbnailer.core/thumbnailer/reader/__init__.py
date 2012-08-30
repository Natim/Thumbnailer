# -*- coding: utf-8 -*-
"""Read and URL and get the file from cache if possible or update the file."""
import hashlib
import datetime
import settings
import requests
import os
from wsgiref.handlers import format_date_time
from tempfile import NamedTemporaryFile

INPUT_CACHE_DIR = getattr(settings, 'INPUT_CACHE_DIR', '/tmp')

def get_input_path_for_url(url):
    """Return the input cache file path"""
    hash_id = hashlib.sha256(url).hexdigest()
    return os.path.join(INPUT_CACHE_DIR, hash_id)

def get_file_for_url(url):
    """Return the good reader for the file"""
    if url.endswith('original'):
        return get_sae_file_for_url(url)
    else:
        return get_file_for_normal_url(url)

def get_sae_file_for_url(url):
    """Return the file object related to the URL"""
    headers = {}
    cache_file_path = get_input_path_for_url(url)
    if not os.path.exists(cache_file_path):       
        req = requests.get(url, headers=headers)
        fd = open(cache_file_path, 'wb')
        fd.write(req.content)
        fd.close()
        cache = False
    else:
        cache = True

    fd = open(cache_file_path, 'rb')
    return fd, cache

def get_file_for_normal_url(url):
    """Return the file object related to the URL"""
    headers = {}
    cache_file_path = get_input_path_for_url(url)
    if os.path.exists(cache_file_path):       
        hash_id_m_time = os.path.getmtime(cache_file_path)
        headers = {'If-Modified-Since': format_date_time(hash_id_m_time)}        
    
    req = requests.get(url, headers=headers)

    if req.status_code != 304:
        fd = open(cache_file_path, 'wb')
        fd.write(req.content)
        fd.close()
        cache = False
    else:
        cache = True

    fd = open(cache_file_path, 'rb')
    return fd, cache
