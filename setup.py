# coding: utf-8
# from distutils.core import setup
from setuptools import setup, find_packages
long_desc = '''
'''

requires = [
    'Sphinx >= 1.0',
    'six'
]

setup(
    name='sphinx_rdb_domain',
    version='0.1',
    description='Sphinx domain for Relational Database',
    long_description=long_desc,
    # url='http://github.com/whosaysni/sphinx_rdb_domain',
    # download_url='http://pypi.python.org/pypi/sphinx_rdb_domain',
    license='BSD',
    author='Yasushi Masuda',
    author_email='whosaysni@gmail.com',
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
