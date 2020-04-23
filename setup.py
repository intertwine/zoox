from setuptools import setup

setup(
    name='zoox',
    version='0.1',
    py_modules=['zoox'],
    install_requires=[
        'click',
        'xlsxwriter'
    ],
    entry_points='''
        [console_scripts]
        zoox=zoox:cli
    ''',
)