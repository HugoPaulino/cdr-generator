# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='CDR Generator package',
    long_description=readme,
    author='Hugo Santos',
    author_email='me@kennethreitz.com',
    url='https://github.com/HugoPaulino/CDRGenerator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)