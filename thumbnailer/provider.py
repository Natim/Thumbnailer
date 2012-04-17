from flask import abort, Flask, request, make_response, redirect

import requests

from PIL import Image
from StringIO import StringIO
import os.path

from engines import images, documents

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

    thumb = THUMBNAILER_ENGINE[engine](url, width, height)

    # 3. Returns the image
    response = make_response(thumb)
    response.content_type = 'image/png'

    return response

if __name__ == "__main__":
    app.run()
