#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, 2016, 2018 Adam Dybbroe

# Author(s):

#   Hrobjartur Thorsteinsson <thorsteinssonh@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


try:
    with open("./README", "r") as fd:
        long_description = fd.read()
except IOError:
    long_description = ""


from setuptools import setup
import sys


def get_version():
    if sys.version_info >= (3, 5):
        import importlib
        spec = importlib.util.spec_from_file_location('version', 'pydecorate/version.py')
        version = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(version)
    else:
        # python 2.7 doesn't have the `importlib.util` package
        # python 3.4 doesn't have the `module_from_spec` method
        import imp
        version = imp.load_source('pydecorate.version', 'pydecorate/version.py')
    return version.__version__

setup(name='pydecorate',
      version=get_version(),
      description='Decorating PIL images: logos, texts, pallettes',
      author='Hrobjartur Thorsteinsson',
      author_email='thorsteinssonh@gmail.com',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v3 " +
                   "or later (GPLv3+)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Scientific/Engineering"],
      url="http://code.google.com/p/pydecorate/",
      # download_url="..."
      long_description=long_description,
      license='GPLv3',

      packages=['pydecorate'],

      # Project should use reStructuredText, so ensure that the docutils get
      # installed or upgraded on the target machine
      install_requires=['docutils>=0.3',
                        'pillow'],
      scripts=[],
      data_files=[],
      test_suite="nose.collector",
      tests_require=[],

      zip_safe=False
      )