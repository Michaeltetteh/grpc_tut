from setuptools import setup, find_packages

setup(
    name='django_grpc',
    version='0.0.1',
    packages=find_packages(include=['django_grpc', 'django_grpc.*']),
    install_requires=[
      'grpcio==1.40.0'
    ],
)