from flask import abort, Flask, request, make_response, redirect

import requests

from PIL import Image
from StringIO import StringIO
import os.path

from thumbnailer.reader import get_file_for_url
from thumbnailer.engines.images import images
from thumbnailer.engines.documents import documents
from thumbnailer.cache import get_thumb_from_cache, have_cache_for_url

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
    # 1. Get the image or raise 404
    url = request.args.get('url', None)
    width = int(request.args.get('width', 0))
    height = int(request.args.get('height', 0))

    if width == 0 and height == 0:
        abort(400, u'You must set either width or height')

    if url:
        if url.startswith('/'):
            url = '%s%s' % (request.host_url, url[1:])
    else:
        abort(404)

    # Call the reader
    file_obj = get_file_for_url(url)

    # If needed we call the engine
    if not (have_cache_for_url(request.url) and file_obj.is_from_cache):
        THUMBNAILER_ENGINE[engine](file_obj, request.url, width, height)

    # Get the thumb
    thumb = get_thumb_from_cache(request.url)

    # 3. Returns the image
    response = make_response(thumb.read())
    response.content_type = 'image/png'

    file_obj.close()
    thumb.close()
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
