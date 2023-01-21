#!/usr/bin/env python3

import setuptools
import m3ufu

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="m3ufu",
    version=m3ufu.version(),
    author="Adrian",
    author_email="spam@iodisco.com",
    description="M3U8 Parser with SCTE-35 Support",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/m3u8fu",
    packages=setuptools.find_packages(),
    py_modules=["m3ufu"],
    scripts=['bin/m3ufu'],
    install_requires=[
        "pyaes",
        "threefive >= 2.3.71",
        "new_reader >= 0.1.3",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.6",
)
