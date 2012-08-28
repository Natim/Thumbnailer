# -*- coding: utf-8 -*-
"""Read and URL and get the file from cache if possible or update the file."""
import hashlib
import settings

THUMB_CACHE_DIR = getattr(settings, 'THUMB_CACHE_DIR', '/tmp')

def get_thumb_from_cache(url):
    """Return the thumb file object related to the URL"""
    hash_id = hashlib.sha256(url).hexdigest()
    cache_file_path = os.path.join(THUMB_CACHE_DIR, hash_id)
    return open(cache_file_path, 'r')
