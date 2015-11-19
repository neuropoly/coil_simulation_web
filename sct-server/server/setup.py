import os

from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_mailer',
    'itsdangerous',
    'waitress',
    'sqlalchemy',
    'alembic',
    'passlib',
    'pyramid_tm',
    'cryptacular',
    'zope.sqlalchemy',
    'simplejson',
    'psutil',
    'pyramid_debugtoolbar',
    'cornice',
    'jsonpickle',
    'scipy',
    'numpy',
    'nibabel',
    'matplotlib',
    'sympy',
    'dipy',
    'redis',
    'pandas',
    'pillow'

    ]

setup(name='server',
      version='0.1',
      description='server',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Willis Pinaud & Pierre-Olivier Quirion',
      author_email='',
      url='spinalcordtoolbox.org',
      keywords='Spinal cord toolbox web mri',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      cmdclass={'build_ext':build_ext},
      setup_requires=['numpy'],
      install_requires=requires,
      tests_require=requires,
      test_suite="server",
      entry_points="""\
      [paste.app_factory]
      main = server:main
      """,
      )
