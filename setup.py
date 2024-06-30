from setuptools import setup

setup(
   name='package',
   version='1.0',
   description='A simple dummy project',
   author = 'abc',
   packages = ['package'],
   scripts = ['scripts/add_script'],
   test=['test_string.py'],
 
)

