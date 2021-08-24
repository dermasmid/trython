from setuptools import setup, find_packages
from trython import __version__ as version


with open('README.md', encoding='utf-8') as f:
    readme = f.read()


with open("requirements.txt", encoding="utf-8") as f:
    requirements = [r.strip() for r in f]




setup(
    name = 'trython',
    version = version,
    packages= find_packages(),
    url = 'https://github.com/dermasmid/trython',
    license = 'MIT',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author = 'Cheskel Twersky',
    author_email= 'twerskycheskel@gmail.com',
    description = 'Wrap functions that might fail some time, so it will retry to execute that function n times',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = requirements,
    python_requires='>=3.6'
    )
