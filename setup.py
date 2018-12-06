#!/usr/bin/env python3
from setuptools import setup, find_packages


with open('README.rst') as ff:
    readme = ff.read()

setup(
    name='tox-conda',
    version='0.1.0',
    description='Tox plugin that provides integration with conda',
    long_description=readme,
    author="Daniel R. D'Avella",
    author_email='ddavella@stsci.edu',
    url='https://github.com/drdavella/tox-conda',
    entry_points=dict(tox=['conda = tox_conda.plugin']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: tox",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    install_requires=['tox'],
    python_requires='>=3.3',
    packages=find_packages(exclude=['tests']),
)
