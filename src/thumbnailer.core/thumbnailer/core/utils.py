# -*- coding: utf-8 -*-
import requests
from StringIO import StringIO

def download_from_url(url):
    response = requests.get(url)
    return StringIO(response.content)
