# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

VERSION = (0, 1, 6)

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()


setup(
    name='easy_zipcode',
    version='.'.join(map(str, VERSION)),
    description='easy_zipcode is a lightweight python app for retrieving \
        brazilian address from a zip code',
    longdescription=readme,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    keywords='zip code',
    author='Fernando Chimicoviaki',
    author_email='fernando.chimicoviaki@stored.com.br',
    url='http://github.com/stored/easy_zipcode',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
    ],
)
