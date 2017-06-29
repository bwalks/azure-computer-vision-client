#!/usr/bin/env python

from distutils.core import setup

setup(name='Azure Computer Vision Client',
      version='1.0',
      description='Lightweight client for the Azure Computer Vision API',
      author='Brendan Walker',
      url='https://github.com/bwalks/azure-computer-vision-client',
      packages=['azure_computer_vision_client'],
      requires = ['requests'])