# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import step, world

import requests

from PIL import Image
from StringIO import StringIO

SERVER_PREFIX = 'http://localhost:5000/'

@step(u'Given /(.*)/\?url=(.*)&width=(\d+)&height=(\d+)')
def given_engine_url_url_width_width_height_height(step, engine, url, width, height):
    world.engine = engine
    world.url = url
    world.width = int(width)
    world.height = int(height)

@step(u'When I access the api url')
def when_i_access_the_api_url(step):
    url = '%s%s?url=%s&width=%d&height=%d' % (SERVER_PREFIX, world.engine, 
                                               world.url, world.width, 
                                               world.height)
    print url
    world.response = requests.get(url)
    assert world.response.status_code == 200

@step(u'Then I get my image at size (\d+)x(\d+)')
def then_i_get_my_image_at_size_width_x_height(step, width, height):
    i = Image.open(StringIO(world.response.content))
    assert i.size == (world.width, world.height)

