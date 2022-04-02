import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='django-basicauth',
    version='0.5.4',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/NIXKnight/django-basicauth/',
    license='MIT',
    description="Basic auth utilities for Django.",
    long_description=README + '\n\n' + CHANGES,
    packages=['basicauth'],
    install_requires=['Django>=2.0', 'passlib==1.7.4'],
    include_package_data=True,
    test_suite="tests",
    zip_safe=False,
)
