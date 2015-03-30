from distutils.core import setup
import os
import context
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='context',
    version=context.__version__,
    packages=[
        'context',
        'context.data',
        'context.handlers',
    ],
    install_requires=required
)
