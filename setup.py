# -*- coding: utf-8 -*-
import sys
from os import path
from distutils.core import setup

if sys.version_info < (3, 7):
    sys.exit('CollLib requires Python 3.7 or higher')

ROOT_DIR = path.abspath(path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

setup(
    name='CollLib',
    version='0.0.1',
    install_requires=[
    ],
    description='',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    platforms='any',
    author='a2dict',
    author_email='a2dict@163.com',
    packages=['CollLib'],
    license='BSD-New',
)
