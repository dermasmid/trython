import re

from setuptools import find_packages, setup


with open("trython/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]


with open("README.md", encoding="utf-8") as f:
    readme = f.read()


setup(
    name="trython",
    version=version,
    packages=find_packages(),
    url="https://github.com/dermasmid/trython",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Cheskel Twersky",
    author_email="twerskycheskel@gmail.com",
    description="Wrap functions that might fail some time, so it will retry to execute that function n times",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
