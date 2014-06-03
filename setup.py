#!/usr/bin/env python
# written by Daniel Oaks <daniel@danieloaks.net>, Chad Nelson
# licensed under the BSD 2-clause license
__author__ = 'Daniel Oaks <daniel@danieloaks.net>, Chad Nelson'

from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='http-status',
    version='0.1.0a',
    description='HTTP Status codes, names, and descriptions.',
    long_description=long_description,
    author='Daniel Oaks',
    author_email='danneh@danneh.net',
    url='https://github.com/DanielOaks/http_status',
    packages=['http_status'],
    package_dir={'http_status': 'src/http_status'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
