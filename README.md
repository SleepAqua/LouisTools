<!--
 * @version: Python 3.7.3
 * @Author: Louis
 * @Date: 2020-06-15 18:03:30
 * @LastEditors: Louis
 * @LastEditTime: 2020-06-15 18:15:17
--> 

# LouisTools -- Tools for data/operation/testing engineers

[![PyPI](https://img.shields.io/pypi/v/LouisTools.svg?style=flat-square)](https://pypi.python.org/pypi/LouisTools/)
[![PyPI](https://img.shields.io/pypi/pyversions/LouisTools.svg?style=flat-square)](https://pypi.python.org/pypi/LouisTools/)

## About Louis
Louis is a data engineer working in financial area. A Python programmer, Linux operationer, loving learning and sharing.

## About Tools
The tools are designed for the following technicians:
* data engineers (ETL, especially for financial data and time-series data)
* operation engineers (mainly Linux)
* testing engineers (unnittest, logging, HTML, email)
* data analysts (data I/O and data-washing, especially for financial data)
* application developers (regex, logging, config I/O, useful decorators)

A HTMLTestRunner in Python 3 version is contained in the package (Thanks to Wai Yip Tung for making such a good-to-use Python 2 package).

## Examples
1: You can parse a path string including date formatters:
```python
import LouisTools as LT
file_path = "/data/certain_data/%Y/%m/%Y%m%d.csv"
today_str = LT.TODAY
today_file_path = LT.parse_date_in_str(file_path, today_str)
print(today_file_path)  # /data/certain_data/2020/06/20200616.csv
```

2: You can make a (parent) directory safely:
```python
import LouisTools as LT
file_to_save = "/home/usr/new_project/data.hdf"
LT.make_parent_dir(file_to_save)  # /home/usr/new_project will be created if not exist
dir_to_make = "/home/usr/new_project"
LT.make_dir(file_to_save)  # /home/usr/new_project will be created if not exist
```

3: You can create a logger very simply and fastly:
```python
import LouisTools as LT
LOGGER = LT.single_lvl_logger("LouisTools")  # Only StreamHandler, LouisTools is the log name
LOGGER = LT.single_lvl_logger("LouisTools", "/project/log/a_log_file.log")  # FileHandler is created saving in "/project/log/a_log_file.log"
```

4: You can interact with you config files safely and quickly (both json and ini supported):
```python
import LouisTools as LT
json_path = "/home/usr/projectL/projectL.json"  # A typical json file path in Linux
config_content = LT.read_json(json_path, encoding_="utf-8")  # You can change encoding_ arg as what you want!
assert isinstance(config_content, dict)
ini_path = r"C:\Users\A_USER\projectX\projectX.ini"  # A typical ini file path in Windows
config_content = LT.read_ini(ini_path, encoding_="utf-8-sig")  # Windows' gift: a BOM added for freee!
assert isinstance(config_content, dict)
```

5: You can dump the result without overwrite possibly existing files (safe, safe, and safe! even the directory will be checked and created if not exist):
```python
import LouisTools as LT
@LT.dump_without_overwrite(sep="\t", encoding="utf-8", header=True, index=False)
def generate_df(df, df_path):
    # You can do something on df
    return df, df_path
```
