from setuptools import setup

setup(
    name='smanim',
    version='1',
    packages=['AnimationLibrary', 'AnimationLibrary.drawable', 'AnimationLibrary.algorithms', 'AnimationLibrary.equations', 'AnimationLibrary.tree'],
    install_requires=[
      "pillow",
    ],
    url='https://github.com/szwos/smanim',
    license='',
    author='Szwos',
    author_email='szwos5@gmail.com',
    description='smanim - small library of objects for creating simple mathematic animations. Written in Python 3 for my engineer\'s thesis. '
)
