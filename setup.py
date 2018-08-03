from setuptools import setup, find_packages

setup(name='pymtg',
      version='0.2',
      description='Python research utils that some of us use at the MTG and eventually everyone will use :)',
      url='https://github.com/MTG/pymtg',
      author='Music Technology Group',
      author_email='mtg-info@upf.edu',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages())
