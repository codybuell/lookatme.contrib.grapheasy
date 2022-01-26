"""
Setup for lookatme.contrib.grapheasy
"""

import pathlib

from setuptools import setup, find_namespace_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="lookatme.contrib.grapheasy",
    version="0.0.1",
    description="Adds a grapheasy code block type",
    lond_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/codybuell/lookatme.contrib.grapheasy",
    author="Cody Buell",
    author_email="cody@codybuell.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Environment :: Console",
        "Environment :: Plugins",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.9",
    packages=find_namespace_packages(include=["lookatme.*"]),
    install_requires=[],
)
