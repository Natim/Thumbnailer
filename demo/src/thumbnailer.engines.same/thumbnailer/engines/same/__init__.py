# -*- coding: utf-8 -*-
from thumbnailer.core.utils import download_from_url


def extract_image(url, width, height):
    data = download_from_url(url)
    return data.read()
