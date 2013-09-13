#!/usr/bin/env python

from setuptools import setup

setup(
    name='modes',
    version='0.1',
    license='MIT License',
    author='td',
    description='SSR Mode-S decoding tools',
    packages=['gillham'],
    tests_require=['nose'],
    test_suite='nose.collector'
)
