from setuptools import setup

setup(name='django_grpc',
      version='0.0.1',
      description='client/server stubs',
      url='https://github.com/Michaeltetteh/grpc_tut',
      author='Mike',
      author_email='test@test.test',
      license='MIT',
      packages=['django_grpc'],
      install_requires=[
          'grpcio==1.40.0'
      ],
      zip_safe=False)