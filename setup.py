from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('collective', 'folderlogo', 'docs', 'README.rst') + "\n" +
    read('collective', 'folderlogo', 'docs', 'HISTORY.rst') + "\n" +
    read('collective', 'folderlogo', 'docs', 'CONTRIBUTORS.rst') + "\n" +
    read('collective', 'folderlogo', 'docs', 'CREDITS.rst'))


setup(
    name='collective.folderlogo',
    version='1.1',
    description="Easily add and change logos in different folders for Plone.",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.folderlogo',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone>=4.2',
        'hexagonit.testing',
        'plone.app.registry',
        'plone.browserlayer',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
