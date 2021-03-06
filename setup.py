from distutils.core import setup
setup(
  name = 'abstract_algebra',         # How you named your package folder (MyLib)
  packages = ['abstract_algebra'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python library for manipulating groups',   # Give a short description about your library
  long_description = 'A python module for manipulating groups with common operations. You can check if a group is a subgroup, if a group is cyclic, you can compute the external direct product of groups and cosets of groups. Specialized groups such as S_n and A_n are coming soon!',
  author = 'Benjamin Jeffers',                   # Type in your name
  author_email = 'bjeffers@trinity.edu',      # Type in your E-Mail
  url = 'https://github.com/benjeffers/Algebra.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/benjeffers/Algebra/archive/0.3.tar.gz',    # I explain this later on
  keywords = ['algebra', 'groups'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'wheel'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)