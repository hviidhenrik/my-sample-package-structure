from setuptools import setup, find_packages

setup(
    name='sample-package-name',  # should not be the same name as the root folder
    version='0.1.0',
    description='Sample package template for minimalistic Python projects',
    author='Henrik Hviid Hansen',
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent", ],
    packages=find_packages(),
)
