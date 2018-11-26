from setuptools import find_packages
from distutils.core import setup

setup(
    name='angr_platforms',
    version='0.1',
    description='A collection of extra platforms for angr',
    packages=find_packages(),
    install_requires=[
        'angr',
        'cle',
        'archinfo',
        'pyvex',
        'clint'
    ],
)
