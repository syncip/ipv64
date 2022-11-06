from setuptools import setup, find_packages


setup(
    name='ipv64',
    version='0.1',
    license='MIT',
    author="R60",
    author_email='pypi.nmvk0@getrekt.win',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/syncip/ipv64.git',
    keywords='ipv64 updater',
    install_requires=[
          'dnspython',
      ],

)