'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 17:58:17
@LastEditors: Louis
@LastEditTime: 2020-06-15 18:13:23
'''
from setuptools import setup, find_packages


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '2'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

setup(
        name='LouisTools',
        version=VERSION,
        description='A very useful tool-set for data/operation/testing engineers, specialized in ETL and finance.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords='tools data operation testing finance os re IO email logging datetime',
        author='Louis Tian',
        author_email='dqyyrlfy@gmail.com',
        license='MIT',
        url='https://github.com/SleepAqua/LouisTools',
        packages=find_packages(),
        zip_safe=False,
        platforms='any',
        install_requires =['pandas'],
        classifiers=[
          'Environment :: Console',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Financial and Insurance Industry',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Database',
          'Topic :: Utilities',
          'Topic :: Office/Business :: Financial',
          'Topic :: Office/Business :: Financial :: Investment',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Communications :: Email',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration'
      ]
)
