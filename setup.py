# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='absolutely-proprietary',
    version='1.0.0',
    description='Proprietary package detector for arch-based distros.',
    url='https://github.com/vmavromatis/absolutely-proprietary',
    author='vmavromatis',
    author_email='bill.mavromatis@protonmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[''],
    entry_points={
        'console_scripts': [
            'absolutely-proprietary=absolutely_proprietary.__init__'
        ]
    },
)
