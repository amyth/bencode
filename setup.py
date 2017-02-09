#!/usr/bin/python
# -*- coding: utf-8 -*-
#
########################################
##
# @author:          Amyth
# @email:           mail@amythsingh.com
# @website:         www.techstricks.com
# @created_date: 09-02-2017
# @last_modify: Thu Feb  9 17:03:34 2017
##
########################################


from distutils.core import setup
from setuptools import find_packages

setup(
    name='bencode-python3',
    version='1.0.0',
    author='Amyth Arora',
    author_email='mail@amythsingh.com',
    packages=find_packages(),
    url='https://github.com/amyth/bencode',
    license='GPL3 License',
    description='Python 3 port for the official bencode library',
    long_description='This is the python 3 port for the official bencode '\
	    '(Bitorrent) encoding and decoding library. This project supports '\
	    'both python 2 and python 3.',
    zip_safe=False,
)
