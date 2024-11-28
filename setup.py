from os import path, environ

from setuptools import setup
from setuptools.config.expand import find_packages


__version__ = environ.get('version')

project_dir = path.abspath(path.dirname(__file__))

exec(sorted([el if el.startswith('__version__') else 'Z' for el in open('./pozdnyakov/__init__.py', 'r').read().split('\n')], reverse=True)[0])


with open(path.join(project_dir, 'README.md'), encoding='utf-8') as f:
    description_md = f.read()

with open("requirements.txt", "r") as reqs_file:
    requirements = reqs_file.read().split("\n")


setup(
    name="pozdnyakov",
    version=__version__,
    author="Vitally Petreev",
    author_email="vitaliy.petreev@gmail.com",

    description="Library to talk with Pozdnyakov (наш слоняра)",
    long_description=description_md,
    long_description_content_type="text/markdown",

    url="https://github.com/sodeeplearning/Pozdnyakov-Vlad-AI",

    license="MIT License, see LICENSE file",

    packages=find_packages(),
    install_requires=requirements,

    python_requires=">=3.9"
)
