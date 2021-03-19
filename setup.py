"""The setup script."""
from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author_email="paul@caston.id.au",
    author="Paul Caston",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Get the latest Open Peer Power version from various sources.",
    install_requires=[
        "aiohttp>=3.6.1,<4.0",
        "async_timeout<=3.0.1",
        "awesomeversion>=20.12.4",
    ],
    keywords=["openpeerpower", "version", "update"],
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=readme,
    name="pyoppversion",
    packages=find_packages(include=["pyoppversion"]),
    python_requires=">=3.8.0",
    url="https://github.com/pcaston/pyoppversion",
    version="main",
)
