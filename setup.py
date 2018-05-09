from setuptools import setup, find_packages

setup(
     name='people_detection',    # This is the name of your PyPI-package.
     version='0.1',    # Update the version number for new releases
     packages=find_packages(exclude=['tests*','images','etcs']),
     description='people detection python package',
     install_requires=['argparse','matplotlib','scipy','tqdm','requests','fire','dill','scipy','scikit-learn','opencv-python','h5py','Pillow','requests','psutil']
     data_files=[('facenet/align',['det1.npy','det2.npy','det3.npy'])]
)
