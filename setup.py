#!/usr/bin/env python3

import setuptools
import m3u8fu

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="hls",
    version=m3u8fu.version(),
    author="Adrian",
    author_email="spam@iodisco.com",
    description="HLS M3U8 Parser with SCTE-35 Support",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/hls",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.6",
)
