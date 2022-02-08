from setuptools import find_packages, setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="packagename",  # name used to install it. The code dir 'packagename' is what you import. Can be identical.
    version="0.1.0",
    description="A template structure for minimalistic Python projects",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Henrik Hviid Hansen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    # install_requires=[""]  # put package / dependencies required to run this one
)
