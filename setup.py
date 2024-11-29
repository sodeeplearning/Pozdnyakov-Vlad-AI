from os import path

from setuptools import setup
from setuptools import find_packages


__version__ = "0.0.5"

project_dir = path.abspath(path.dirname(__file__))


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

    license="MIT License",

    packages=find_packages(),
    install_requires=requirements,

    python_requires=">=3.9"
)
