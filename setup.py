#!/usr/bin/env python
# coding: utf8

from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='qu',
    version='1.2.5',
    keywords=['qiniu', 'upload', 'blog'],
    description='Quickly generating unique url of a picture for markdown files.',
    long_description=readme,
    author='cls1991',
    author_email='tzk19910406@hotmail.com',
    url='https://github.com/cls1991/qu',
    py_modules=['qu'],
    install_requires=[
        'qiniu>=7.2.0',
        'click>=6.7',
        'pytest>=3.3.1'
    ],
    package_data={
        'config': ['.config.cfg']
    },
    license='Apache License 2.0',
    zip_safe=False,
    platforms='any',
    entry_points={
        'console_scripts': ['qu = qu:cli']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent'
    ]
)
