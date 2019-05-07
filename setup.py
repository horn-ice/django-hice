import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-hice',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django-based web frontend for the Horn-ICE Verification Toolkit',
    long_description=README,
    url='https://github.com/horn-ice/django-hice',
    author='Daniel Neider',
    author_email='neider@mpi-sws.org',
    install_requires=['django>=2.2.0', 'django-rq>=1.3'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
