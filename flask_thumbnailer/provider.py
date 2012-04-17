from flask import abort, Flask, request, make_response

import requests

from PIL import Image
from StringIO import StringIO
import os.path

from utils import scale_and_crop

app = Flask(__name__)
app.debug=True

@app.route('/resize/')
def resize():
    # 1. Get the image or raise 404
    url = request.args.get('url', None)
    width = int(request.args.get('width', 800))
    height = int(request.args.get('height', 600))
    opts = [x.strip() for x in request.args.get('opts', 'crop').split(',')]
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
    version = scale_and_crop(image, width, height, opts)
    if not version:
        abort(400, u'Failed to resize the image with these parameters')

    # 3. Returns the image
    thumb = StringIO()
    version.save(thumb, 'PNG')
    response = make_response(thumb.getvalue())
    response.content_type = 'image/png'
    return response

if __name__ == '__main__':
    app.run()
