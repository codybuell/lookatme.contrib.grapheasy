"""
Setup for lookatme.contrib.grapheasy
"""


from setuptools import setup, find_namespace_packages


setup(
    name="lookatme.contrib.grapheasy",
    version="0.0.1",
    description="Adds a grapheasy code block type",
    url="https://github.com/codybuell/lookatme.contrib.grapheasy",
    author="Cody Buell",
    author_email="cody@codybuell.com",
    python_requires=">=3.9",
    packages=find_namespace_packages(include=["lookatme.*"]),
)
