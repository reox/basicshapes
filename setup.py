from setuptools import setup


setup(
        name="basicshapes",
        author="Sebastian Bachmann",
        author_email="hello@reox.at",
        url="https://github.com/reox/basicshapes",
        licence="MIT",
        version="0.1",
        scripts=["basicshapes"],
        install_requires=["h5py>=2.7", "numpy>=1.13", "scipy>=0.19"],
)
