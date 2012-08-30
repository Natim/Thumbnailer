from flask import abort, Flask, request, make_response, redirect

import requests

from PIL import Image
from StringIO import StringIO
import os.path

from thumbnailer.reader import get_file_for_url
from thumbnailer.engines.images import images
from thumbnailer.engines.documents import documents
from thumbnailer.cache import get_thumb_from_cache, have_cache_for_kwargs, get_thumb_path_for_kwargs

app = Flask(__name__)
app.debug=True

GITHUB_HOME = 'http://github.com/Natim/Thumbnailer/'

THUMBNAILER_ENGINE = {
    'scale': images.scale,
    'crop': images.crop,
    'upscale': images.upscale,
    'document': documents.extract_image,
}

@app.route('/')
def home():
    return redirect(GITHUB_HOME)

@app.route('/<engine>/')
def resize(engine):
    num_pages = None
    # 1. Get the image or raise 404    
    params = {'url': request.args.get('url', None),
              'width': int(request.args.get('width', 0)),
              'height': int(request.args.get('height', 0))}

    if params['width'] == 0 and params['height'] == 0:
        abort(400, u'You must set either width or height')

    if params['url']:
        if params['url'].startswith('/'):
            params['url'] = '%s%s' % (request.host_url, url[1:])
    else:
        abort(404)

    try:
        params['page'] = int(request.args.get('page', 1))
    except:
        params['page'] = 1

    # Call the reader
    file_obj, is_from_cache = get_file_for_url(params['url'])

    if engine == 'document':
        num_pages = documents.count_pages(file_obj.read())
        if params['page'] > num_pages or params['page'] < 1:
            abort(400, 'page not found')

    # If needed we call the engine
    if not (have_cache_for_kwargs(**params) and is_from_cache):
        print "CACHE STATUS", is_from_cache, have_cache_for_kwargs(**params), get_thumb_path_for_kwargs(**params)
        num_pages = THUMBNAILER_ENGINE[engine](file_obj, **params) or None

    # Get the thumb
    thumb = get_thumb_from_cache(**params)

    # 3. Returns the image
    response = make_response(thumb.read())
    response.content_type = 'image/png'

    if num_pages is not None:        
        response.headers.add('x-thumbnailer-num_pages', str(num_pages))
    else:
        response.headers.add('x-thumbnailer-num_pages', 1)

    file_obj.close()
    thumb.close()
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
