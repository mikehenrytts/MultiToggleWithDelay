from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-MultiToggleWithDelay',
      version='0.1.0',
      description='CraftBeerPi4 step plugin: multi-actor toggle with per-actor delays',
      author='Mike Henry',
      author_email='mikehenrytts"yahoo.com',
      url='https://github.com/mikehenrytts/cbpi4-MultiToggleWithDelay',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-MultiToggleWithDelay': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-MultiToggleWithDelay'],
      long_description=long_description,
      long_description_content_type='text/markdown', 
     )
