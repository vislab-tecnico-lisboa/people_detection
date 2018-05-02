from setuptools import setup, find_packages

setup(
     name='people_detection',    # This is the name of your PyPI-package.
     version='0.1',    # Update the version number for new releases
     packages=find_packages(exclude=['tests*','images','etcs']),
     description='people detection python package',
     long_description=open('README.md').read(),
     install_requires=['argparse','matplotlib','scipy','tqdm','requests','fire','ast','dill']
)
