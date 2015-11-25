from setuptools import find_packages
from setuptools import setup

setup(name='app',
      version="0.1",
      description='Angular frontend',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      )
