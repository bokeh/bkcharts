''' Setup script for bkcharts.

'''
from shutil import copy

from setuptools import find_packages, setup

# we want to have the license at the top level of the GitHub repo, but setup
# can't include it from there, so copy it to the package directory first thing
copy("LICENSE.txt", "bkcharts/")

# state our runtime deps here, also used by meta.yaml (so KEEP the spaces)
REQUIRES = [
    'six >=1.5.2',
    'numpy >=1.7.1',
    # pandas should be added after Bokeh 1.0
]

setup(

    # basic package metadata
    name='bkcharts',
    version="0.2",
    description='High level chart types built on top of Bokeh',
    license='New BSD',
    author='Continuum Analytics',
    author_email='info@continuum.io',
    url='http://github.com/bokeh/bkcharts',
    classifiers=open("classifiers.txt").read().strip().split('\n'),

    # details needed by setup
    install_requires=REQUIRES,
    packages=find_packages(exclude=["scripts*", "tests*"]),
    package_data={'bokeh': ['LICENSE.txt']},
    zip_safe=False

)
