from setuptools import setup, find_packages

setup(
    name='django_grpc',
    version='0.0.1',
    description='client/server generated files',
    author='Michael Tetteh',
    author_email='test@test.test',
    url='https://github.com/Michaeltetteh/grpc_tut',
    packages=find_packages(include=['django_grpc', 'django_grpc.*']),
    install_requires=[
      'grpcio==1.40.0'
    ],
)