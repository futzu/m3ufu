#!/usr/bin/env python3

import setuptools
import m3u8fu

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="m3u8fu",
    version=m3u8fu.version(),
    author="Adrian, The Left Hand of God",
    author_email="spam@iodisco.com",
    description="The Most Advanced M3U8 Parser Allowed by Law. Includes Auto AES Decryption, SCTE-35 Support, Segment Reassembly et multo magis",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/m3u8fu",
    packages=setuptools.find_packages(),
    install_requires=[
        "threefive",
        "new_reader",
        "pyaes",
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
