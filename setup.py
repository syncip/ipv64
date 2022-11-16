from setuptools import setup
setup(
  name = 'ipv64',         # How you named your package folder (MyLib)
  version = '0.2',      # Start with a small number and increase it with every change you make
  description = 'Updater for ipv64.net',   # Give a short description about your library
  author = 'R60',                   # Type in your name
  author_email = 'pypi.nmvk0@getrekt.win',      # Type in your E-Mail
  py_modules=["ipv64"],
  package_dir={'': 'src'},
  keywords = ['ipv64', 'dyndns', 'updater'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'dnspython',
          'requests',
          'argparse',
      ],
)