import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-wsgitools',
    version='0.1.1',
    description='Tools for using Django + mod_wsgi.',
    long_description=read('README.markdown'),
    author='Matthew Tretter',
    author_email='matthew@exanimo.com',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
