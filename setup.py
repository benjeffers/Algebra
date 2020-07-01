from setuptools import setup, find_packages
 
setup(name='algebra',
      version='0.1',
      url='https://github.com/benjeffers/Algebra.git',
      author='Benjamin Jeffers',
      author_email='bjeffers@trinity.edu',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)