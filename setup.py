#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name='tox-conda',
    version='0.1.0',
    entry_points=dict(tox=['conda = tox_conda.plugin']),
    classifiers=['Framework:: tox'],
    packages=find_packages(),
)
