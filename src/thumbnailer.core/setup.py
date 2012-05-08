# coding=utf-8
"""Python packaging."""
import os
from setuptools import setup, find_packages


def guess_package_name(setup_filename=None):
    """Guess package name from convention: lowercase directory name is package
    name."""
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    package_name = os.path.basename(parent_directory)
    package_name = package_name.lower()
    return package_name


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(name=guess_package_name(),
      version=read_relative_file('version.txt'),  # Follow zest.releaser
                                                  # convention.
      description='A service that take an url and returns a thumbnail',
      long_description=open("README.rst").read(),
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
      namespace_packages=['thumbnailer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'Flask == 0.8',
                        'requests == 0.11.1',
                        ],
      entry_points="""""",
      )
