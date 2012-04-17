# -*- coding: utf-8 -*-
from PIL import Image

def scale_and_crop(im, width, height, opts):
    """
    Scale and Crop.
    """
    
    x, y = [float(v) for v in im.size]

    if 'upscale' not in opts and x < width:
        # version would be bigger than original
        # no need to create this version, because "upscale" isn't defined.
        return False
    
    if width:
        xr = float(width)
    else:
        xr = float(x*height/y)
    if height:
        yr = float(height)
    else:
        yr = float(y*width/x)
    
    if 'crop' in opts:
        r = max(xr/x, yr/y)
    else:
        r = min(xr/x, yr/y)
    
    if r < 1.0 or (r > 1.0 and 'upscale' in opts):
        im = im.resize((int(x*r), int(y*r)), resample=Image.ANTIALIAS)
    
    if 'crop' in opts:
        x, y   = [float(v) for v in im.size]
        ex, ey = (x-min(x, xr))/2, (y-min(y, yr))/2
        if ex or ey:
            im = im.crop((int(ex), int(ey), int(x-ex), int(y-ey)))
    return im
    
scale_and_crop.valid_options = ('crop', 'upscale')

def scale(*args, **kwargs):
    kwargs['opts'] = []
    return scale_and_crop(*args, **kwargs)

def crop(*args, **kwargs):
    kwargs['opts'] = ['crop']
    return scale_and_crop(*args, **kwargs)

def upscale(*args, **kwargs):
    kwargs['opts'] = ['crop', 'upscale']
    return scale_and_crop(*args, **kwargs)
