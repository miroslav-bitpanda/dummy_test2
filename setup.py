"""dummy-test - Dummy test package for testing purposes

This package is super small and light used for pip testing purposes

"""

from os import path
from setuptools import setup


def read(fname: str) -> str:
    """Helper to read README."""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, fname), encoding="utf-8") as f:
        return f.read()

setup(
    name="dummy-test",
    version="9.0.0",
    author='Miroslav Svoboda',
    author_email='miroslav.svoboda@bitpanda.com',
    description="PyPi package dummy test",
    url="https://github.com/miroslav-bitpanda/dummy-test",
    project_urls={"Changelog": "https://github.com/miroslav-bitpanda/dummy-test/blob/master/CHANGELOG.md"},
    keywords="pypi package dummy test",
    packages=["dummy-test"],
    package_data={'dummy-test': ["py.typed"]},
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    license='MIT',
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)