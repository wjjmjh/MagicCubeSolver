from setuptools import setup, find_packages

setup(
    name="magic-cube-solver",
    version="0.0",
    description="A magic solver to solve magic cube",
    author="Stephen Ka-Wah Ma",
    author_email="980907mjh@gmail.com",
    packages=find_packages(where="core"),
    package_dir={"": "core"},
    install_requires=[
    ],
    extras_require={"dev": []},
)
