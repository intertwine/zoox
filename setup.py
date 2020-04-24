from setuptools import setup, find_packages
from os import path
from io import open

"""
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zoox',
    version='0.0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/intertwine/zoox',
    author='Bryan Young',
    author_email='bryan@intertwinesys.com',
    keywords='zoom csv tsv xlsx',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    #py_modules=['zoox'],
    install_requires=[
        'click',
        'xlsxwriter'
    ],
    entry_points={
        'console_scripts': [
            'zoox=zoox:cli'
        ]
    },
)
