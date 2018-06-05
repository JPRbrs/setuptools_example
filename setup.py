from setuptools import setup

setup(name='helloworld',
      version='0.1',
      description='Python packaging test',
      author='Javi',
      author_email='javi@example.com',
      license='MIT',
      packages=['helloworld'],
      scripts=['bin/hello'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
