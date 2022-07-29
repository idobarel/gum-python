from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Creating cool CLIs'
LONG_DESCRIPTION = 'A package that allows you to create cool CLIs using the gum tool.'

setup(
    name="gum",
    version=VERSION,
    author="GodZilo (Ido Barel)",
    author_email="<vikbarel5@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'CLI', 'cmd', 'cli', 'gum'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)