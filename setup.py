# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This contrib extension, sphinxcontrib.jinjadomain provides a Sphinx
domain for describing jinja templates.

You can find the documentation from the following URL:

http://packages.python.org/sphinxcontrib-jinjadomain/
'''

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-jinjadomain',
    version='0.5.1',
    url='https://github.com/offlinehacker/sphinxcontrib.jinjadomain',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-jinjadomain',
    license='BSD',
    author='Jaka Hudoklin',
    author_email='jakahudoklin@gmail.com',
    description='Jinja domain for jinja templates',
    long_description=long_desc,
    zip_safe=False,
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
    namespace_packages=['sphinxcontrib'],
)
