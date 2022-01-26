"""
Setup for lookatme.contrib.grapheasy
"""

import os

from setuptools import setup, find_namespace_packages

req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
with open(req_path, "r") as f:
    required = f.read().splitlines()

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme_path, "r") as f:
    readme = f.read()

setup(
    name="lookatme.contrib.grapheasy",
    version="0.0.1",
    description="Adds a grapheasy code block type",
    lond_description=readme,
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
    install_requires=required,
    packages=find_namespace_packages(include=["lookatme.*"]),
    install_requires=[],
)
