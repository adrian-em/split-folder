#!/usr/bin/env python

import os
import sys

import splitfolder

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'splitfolder'
]

requires = ['docopt']

setup(
    name='splitfolder',
    version=splitfolder.__version__,
    description='Split a big folder into multiple smaller ones.',
    long_description=open('README.md').read(),
    author='Adrian Espinosa',
    author_email='aespinosamoreno@gmail.com',
    url='http://aesptux.com',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)