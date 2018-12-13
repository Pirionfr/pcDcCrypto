from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='pyDcCrypto',
      version='1.0.0',
      description='Data convergence encypt/decrypt library',
      long_description=long_description,
      author='Dimitri Capitaine',
      package_data={'': ['LICENSE']},
      include_package_data=True,
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'pyDcCrypto = pyDcCrypto.__main__:main'
          ]
      },
      license='Apache 2.0',
      install_requires=['M2Crypto'],
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ]
)
