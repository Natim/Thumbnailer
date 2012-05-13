################
Thumbnailer demo
################

This folder contains demonstration stuff for thumbnailer:

* a custom `"Same" engine`_ which plugs in thumbnailer.engines namespace.


*************
"Same" engine
*************

This is a proof of concept engine for thumbnailer. It downloads an image and
returns it as is, i.e. without processing.

Installation
============

Since thumbnailer cannot handle configuration files by now, a hack is required:

* Go to ``demo/src/thumbnailer.engines.same/`` folder and run
  ``python setup.py develop``
* Edit ``thumbnailer/core/provider.py``:

  * Add ``from thumbnailer.engines import same`` below imports.
  * Add ``'same': same.extract_image,`` at the end of THUMBNAILER_ENGINE dict.

Usage
=====

* Run thumbnailer server.
* Use "same" engine and provide an image as url parameter. As an example, if
  you run thumbnailer on localhost, something like
  http://localhost:5000/same/?url=http://localhost:8000/images/vertical.jpg&width=10&height=10
  should work.
