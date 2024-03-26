import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='xcroco-lops',
    version='0.0.1',    
    description='Python post-processing for Croco, based on xgcm',
    author='Sylvie Le Gentil',
    packages=['xcroco-lops'],
    long_description=read('README.md'),

    install_requires=['dask',
                      'dask-jobqueue',
                      'xarray',
                      'zarr',
                      'netcdf4',
                      'jupyterlab',
                      'ipywidgets',
                      'cartopy',
                      'geopandas',
                      'nodejs',
                      'intake-xarray',
                      'xgcm',
                      'numba',
                      'jupyterhub',
                      'ffmpeg',
                      'memory_profiler',
                      'numpy'                     
                      ],

)
