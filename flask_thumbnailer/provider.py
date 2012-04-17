from flask import abort, Flask, request, make_response, redirect

import requests

from PIL import Image
from StringIO import StringIO
import os.path

from utils import scale, crop, upscale

app = Flask(__name__)
app.debug=True

GITHUB_HOME = 'http://github.com/Natim/Thumbnailer/'

THUMBNAILER_ENGINE = {
    'scale': scale,
    'crop': crop,
    'upscale': upscale
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
        response = requests.get(url)
        try:
            image = Image.open(StringIO(response.content))
        except IOError:
            abort(400, u'This url is not an image')
    else:
        abort(404)

    # 2. Resize the image
    version = THUMBNAILER_ENGINE[engine](image, width, height)
    if not version:
        # If the image is smaller than the thumb
        abort(400, u'Failed to resize the image with these parameters')

    # 3. Returns the image
    thumb = StringIO()
    version.save(thumb, 'PNG')
    response = make_response(thumb.getvalue())
    response.content_type = 'image/png'

    return response

if __name__ == '__main__':
    app.run()
