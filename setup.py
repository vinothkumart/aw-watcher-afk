#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='aw-watcher-afk',
      version='0.1',
      description='AFK watcher for ActivityWatch',
      author='Erik Bjäreholt',
      author_email='erik@bjareho.lt',
      url='https://github.com/ActivityWatch/aw-watcher-afk',
      namespace_packages=['aw', 'aw.watchers'],
      packages=['aw.watchers.afk'],
      install_requires=['aw-client', 'pyuserinput'],
      entry_points={
            'console_scripts': ['aw-watcher-afk = aw.watchers.afk:main']
        }
     )