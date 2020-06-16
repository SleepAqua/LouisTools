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

setup(
        name='LouisTools',
        version='0.0.2',
        description='This is a tool-set for data engineering, mainly in financial area.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords='tools data data-washing finance os logging',
        author='Louis Tian',
        author_email='dqyyrlfy@gmail.com',
        url='https://github.com/SleepAqua/LouisTools',
        packages=find_packages(),
        install_requires =['pandas']
)
