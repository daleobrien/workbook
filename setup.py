from setuptools import setup, find_packages

__version__ = '1.0'

description = '''App that creates xls reports, or tables, from simple lists'''

setup(
    name='workbook',
    packages=('workbook', ),
    version=__version__,
    description=description,
    author='Dale O\'Brien',
    author_email='dale@do.id.au',
    url='https://github.com/daleobrien/workbook',
    install_requires=(
        'xlutils',
        'xlwt'
        ),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        )
 )
