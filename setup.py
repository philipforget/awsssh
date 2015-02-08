#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'AwsSsh',
    version = '0.0.2',
    description = 'Easily manage ec2 ssh configs',
    author = 'Philip Forget',
    author_email = 'philipforget@gmail.com',
    url = 'https://github.com/philipforget/awsssh',
    packages = ['awsssh'],
    install_requires  =  ['boto>=2'],
    entry_points = {
        'console_scripts': ['awsssh = awsssh.awsssh:main']
    }
)
