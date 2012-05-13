# coding=utf-8
"""Python packaging."""
import os
from setuptools import setup, find_packages


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(name='thumbnailer',
      version=read_relative_file('version.txt'),  # Follow zest.releaser
                                                  # convention.
      description='A service that take an url and returns a thumbnail',
      long_description=read_relative_file("README.rst"),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU Lesser General Public License v3 ' \
        '(LGPLv3)',
        ],
      keywords='thumbnails',
      author='Rémy Hubscher',
      url='https://github.com/Natim/Thumbnailer',
      license='LGPLv3',
      packages=find_packages('.', exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'Flask == 0.8',
                        'Jinja2 == 2.6',
                        'Werkzeug == 0.8.3',
                        'certifi == 0.0.8',
                        'chardet == 1.0.1',
                        'requests == 0.11.1',
                        'wsgiref == 0.1.2',
                        'PIL == 1.1.7',
                        'pydocsplit == 0.2.0',
                        ],
      entry_points="""""",)
