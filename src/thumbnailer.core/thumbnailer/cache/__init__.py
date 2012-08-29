# -*- coding: utf-8 -*-
"""Read and URL and get the file from cache if possible or update the file."""
import hashlib
import settings
import os
import pickle

THUMB_CACHE_DIR = getattr(settings, 'THUMB_CACHE_DIR', '/tmp')

def get_thumb_path_for_kwargs(**kwargs):
    """Return the cache file path for url"""
    dumps = pickle.dumps(kwargs)
    hash_id = hashlib.sha256(pickle.dumps(kwargs)).hexdigest()
    return os.path.join(THUMB_CACHE_DIR, hash_id)

def get_thumb_from_cache(**kwargs):
    """Return the thumb file object related to the URL"""
    return open(get_thumb_path_for_kwargs(**kwargs), 'r')

def have_cache_for_kwargs(**kwargs):
    """Return if the cache exists for this url"""
    return os.path.exists(get_thumb_path_for_kwargs(**kwargs))
