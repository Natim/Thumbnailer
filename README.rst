############################
Service / API for thumbnails
############################

Draft for the documentation, specs, and tasks... May be moved to some github repository: https://github.com/Natim/Thumbnailer

Table of contents:

* Vision (share concept and goals)
* Alternatives (don't reinvent the wheel)
* Find a name (brainstorm)
* Specs & examples (lettuce!)

******
Vision
******

Abstract
========

An ecosystem around thumbnails:

1. a ready to use service around thumbnails.
2. recipes to generate, host, serve and reference thumbnails.

Creating thumbnails/previews of any documents (images, PDF, html... or any URL) is a killer feature.

Features
========

* Open source.
* Hosted or install-it-at-home.
* Provide an API where, given an URL and some parameters, you get a thumbnail (images) or some preview (documents?).
* Provide plugins and/or API so that it is easy to use the thumbnail generation service in your favorite framework (i.e. some template tag for Django)
* Provide recipes to build a stable and efficient architecture to serve thumbnails (i.e. charm for juju, varnish config, ...)
* Ability to choose/plugin engines: resize, crop, zoom...
* Form to get thumbnail URL: given an engine and parameters (at least an URL)

************
Alternatives
************

List of services or apps that provide similar functionality.

Services
========

http://www.webresourcesdepot.com/10-free-website-thumbnail-generation-services/

Python packages
===============

http://pypi.python.org/pypi?%3Aaction=search&term=thumbnail&submit=search
http://pypi.python.org/pypi?%3Aaction=search&term=preview&submit=search

****
Name
****

Brainstorm... Name of repository is temporary. Thumbnailer

***
API
***

http://foo.com/api/1.0/

<img src="/thumb-api/v1/resize/140x50/upload/toto.jpg" alt=""/>

/thumb-api/v1/natim/resize/upload/toto.jpg?preset=medium

# - preset (definit dans le settings)
 - width, height
# - filtres
# - options


/thumb-api/v1/natim/resize?url=/upload/toto.jpg&width=140&height=50


{% thumbnail resize img.url width=140 height=50 %}

THUMBNAILER_ENGINE = {
    'resize': 'thumbnailer.engine.resize',
    'resize': 'thumbnailer.engine.resize',
    'black-white': 'project.myapp.filter.bw',
}

http://api/natim/v1/resize/monavatar.jpg?opt=crop&width=100&height=100


************
Architecture
************

 - thumbnailer (app django)
    - __init__.py
    - urls.py
    - filters.py
    - views.py
    - engine.py

