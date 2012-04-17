############################
Service / API for thumbnails
############################

Draft for the documentation, specs, and tasks...
May be moved to some github repository: https://github.com/Natim/Thumbnailer

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

Brainstorm... Name of repository is temporary.

***
API
***

scale
+++++
Scale the input image to enter the box, if either width or height are empty, it will scale on only one

    > curl -o thumb_scale.png 'http://localhost:5000/scale/?url=http://localhost:8000/images/horizontal.jpg&width=200&height=150'
    < 200 OK + image/png thumb with max size 200x150

crop
++++
Crop the input image at the right size

    > curl -o thumb_crop.png 'http://localhost:5000/crop/?url=http://localhost:8000/images/horizontal.jpg&width=200&height=150'
    < 200 OK + image/png thumb with a center crop at size 200x150

upscale
+++++++

Upscale the input image if it is too little for a crop

    > curl -o thumb_upscale.png 'http://localhost:5000/upscale/?url=http://localhost:8000/images/horizontal.jpg&width=200&height=150'
    < 200 OK + image/png thumb with an upscale crop at size 200x150
