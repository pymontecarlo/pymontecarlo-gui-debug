#!/usr/bin/env python

# Standard library modules.
import os

# Third party modules.
from setuptools import setup, find_packages

# Local modules.
import versioneer

# Globals and constants variables.
BASEDIR = os.path.abspath(os.path.dirname(__file__))

PACKAGES = find_packages()

INSTALL_REQUIRES = ['numpy', 'h5py', 'matplotlib', 'PyQt5', 'qtpy', 'scipy']
SETUP_REQUIRES = ['nose']

ENTRY_POINTS = {'gui_scripts': "pymontecarlo-gui-debug = pymontecarlo_gui_debug.__main__:run"}

CMDCLASS = versioneer.get_cmdclass()

setup(name="pyMonteCarlo-GUI-debug",
      version=versioneer.get_version(),
      url='http://pymontecarlo.github.io',
      description="Python interface for Monte Carlo simulation programs",
      author="Hendrix Demers and Philippe T. Pinard",
      author_email="hendrix.demers@mail.mcgill.ca and philippe.pinard@gmail.com",
      license="GPL v3",
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Physics'],

      packages=PACKAGES,

      install_requires=INSTALL_REQUIRES,
      setup_requires=SETUP_REQUIRES,

      entry_points=ENTRY_POINTS,

      test_suite='nose.collector',

      cmdclass=CMDCLASS,
)

