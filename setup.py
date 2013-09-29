#!/usr/bin/env python

from setuptools import setup

setup(
    name='gillham',
    version='0.1',
    license='GPL',
    author='tomad',
    description='Gillham code altitude decoding',
    packages=['gillham'],
    tests_require=['nose'],
    test_suite='nose.collector'
)
