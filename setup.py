#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.sources',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.sources'],
    version='0.01',
    description='Simple Python wrapper for managing Who\'s On First sources',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-sources',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-sources/releases/tag/v0.01',
    license='BSD')
