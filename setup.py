#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

version = get_version('drf_gen')

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('django_drf_file_generator.egg-info')
    sys.exit()


setup(
    name='django-drf-file-generator',
    version=version,
    url="https://github.com/AlexandreProenca/django-drf-file-generator",
    license='MIT',
    description='Django DRF File Generator provides a safe way to generate automatically Django basic files like '
                'url.py, serializers.py, admin.py, views.py, to use with djangorestframework, '
                'the genereted files are based on your models.py',
    author='Alexandre Proença',
    author_email='alexandre.proenca@hotmail.com.br',  # SEE NOTE BELOW (*)
    packages=get_packages('drf_gen'),
    #package_data=get_package_data('drf_gen'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'drf_gen=drf_gen.drf_gen:main',
        ],
    },
    zip_safe=False,
    keywords='django',
    package_data={
        'drf_gen': ['*.ini'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
