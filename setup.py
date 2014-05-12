
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vzzual'))
from version import VERSION

long_description = '''
The Vzzual API is designed to allow image and video processing algorithms to
easily run over very large quantities of data, distributed over many servers on
the Vzzual infrastructure.

This is the official python client that wraps the Vzzual REST API (http://www.vzzual.com/page_API.html).
'''

setup(
    name = 'vzzual',
    url="https://github.com/imagemine/tools/blob/master/SDK/Python/python-vzzual",
    packages = ['vzzual'],
    version = VERSION,
    description = 'Official python wrapper for vzzual api',
    author='Dinesh Yadav',
    author_email='dineshyadav.iiit@gmail.com',
    license='MIT License',
    install_requires=[
      'requests',
      'python-dateutil',
      'simplejson',
      'nose2'
    ],
    long_description=long_description
)
