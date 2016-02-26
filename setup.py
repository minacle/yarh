#!/usr/bin/env python3

from setuptools import setup, find_packages
from codecs import open
from os import path

root = path.abspath(path.dirname(__file__))

with open(path.join(root, "README.rst")) as f:
    readme = f.read()

setup(
    name="yarh",
    version="0.3.1",  # phase4
    description="Yet Another Rough HTML",
    long_description=readme,
    url="https://github.com/minacle/yarh",
    author="Mayu Laierlence",
    author_email="minacle@live.com",
    license="BSD",
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="yarh html",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yarh=yarh.__main__:main",
        ],
    },
)
