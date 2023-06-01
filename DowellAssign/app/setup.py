from setuptools import setup

setup(
    name='mayor_isaac_libraries',
    version='0.1',
    description='A Python library for interacting with the dowell nps API',
    packages=['mayor_isaac_library'],
    install_requires=[
        'requests',
    ],
)