from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cyclegan',
    # Versions should comply with PEP 440
    version='0.0.1',

    description='CyCada for Neuormation experiments',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/neuromation/cycada_release',  # Optional

    author='jhoffman',

    # Future exclusions
    packages=find_packages(exclude=['pretrained_models', 'scripts', 'imgs'])
)