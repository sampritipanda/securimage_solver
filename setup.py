import os
from setuptools import setup, find_packages

install_requires = open('requirements.txt').read().splitlines()

__version__ = '0.1.0'


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name='securimage-solver',
    description='Solving Securimage Captchas using ConvNets',
    version=__version__,
    long_description=read('README.MD'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='captcha-solving,neural-networks,cnn',
    author='Sampriti Panda',
    author_email='sampritipanda@outlook.com',
    url="https://github.com/sampritipanda/securimage_solver",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires
)