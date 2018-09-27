#!/usr/bin/env python3
from setuptools import setup


setup(
    name='tox-conda',
    version='0.1.0',
    py_modules=['tox_conda'],
    entry_points=dict(tox=['conda = tox_conda.plugin']),
    classifiers=['Framework:: tox'],
)
