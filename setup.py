# -* coding: utf-8 -*-
# pylint: disable=invalid-name
"""Build, test, and install surface."""

import os
import re
import itertools
from setuptools import setup


def load_requirements_file(filename):
    requirements = []
    with open(filename) as file:
        for line in file:
            if line.startswith('-r'):
                requirements.extend(load_requirements_file(
                    os.path.join(os.path.dirname(filename), line.split()[1])))
            elif line.startswith('#') or line.startswith('-'):
                pass
            else:
                requirements.append(line.rstrip('\n'))
    return sorted(requirements)


# Project directory.
pwd = os.path.dirname(__file__)

# Get project name.
project = open('.name').read().rstrip('\n')

# Get version
version = re.search(
    r"^__version__\s*=\s*'(.*)'",
    open(os.path.join(project, '__init__.py')).read(),
    re.M).group(1)

# Get short description.
description = next(itertools.islice(open('README.rst'), 1)).rstrip('\n')
description = description[len(project)+3:].capitalize() + '.'

# Get long description.
with open('README.rst', 'r') as f:
    long_desc = f.read()


# Get requirements.
extras_require = {}
for filename in os.listdir(os.path.join(pwd, 'requirements')):
    extras_require[os.path.splitext(filename)[0]] = (
        load_requirements_file(os.path.join(pwd, 'requirements', filename)))
install_requires = extras_require.pop('default')
tests_require = extras_require.pop('tests', [])
del extras_require['dev']


setup(
    name=project,
    version=version,
    description=description,
    author='Michael R. Shannon',
    author_email='mrshannon.aerospace@gmail.com',
    license='MIT',
    url='https://github.com/ccarocean/python-{:s}'.format(project),
    download_url=('https://github.com/ccarocean/python-{:s}/'
                  'archive/v{:s}.zip').format(project, version),
    long_description=long_desc,
    packages=[project],
    platforms=['any'],
    keywords=['math', 'geometry', 'plotting'],
    install_requires=install_requires,
    extras_require=extras_requires,
    test_suite='tests',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    zip_safe=True
)
