'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:41:58
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:52:12
'''
import os
import json
import configparser
import pandas as pd

from LouisTools.louis_consts import SEP_MAP


def read_json(json_file, encodings="utf8"):
    """ Read and parse a .json file to a Python dict object. """
    with open(json_file, "r", encoding=encodings) as f:
        paths = json.load(f)
    return paths

def write_json(content, json_file, mode_="a", encodings="utf8"):
    with open(json_file, mode=mode_, encoding=encodings) as f:
        json.dump(content, f)

def read_ini(config_file, encoding_="utf-8-sig"):
    """ Read and parse a .ini file to a Python dict object. """
    cf = configparser.ConfigParser()
    cf.read(config_file, encoding=encoding_)
    client_info = dict(cf._sections)
    for i in client_info:
        client_info[i] = dict(client_info[i])
    return client_info

def export_to_ini_file(config_file, section, option, value, encoding_="utf-8-sig"):
    cf = configparser.ConfigParser()
    cf.read(config_file, encoding=encoding_)
    try:
        cf.set(section, option, value)
    except configparser.NoSectionError:
        cf.add_section(section)
        cf.set(section, option, value)
    with open(config_file, "w+", encoding=encoding_) as fp:
        cf.write(fp)

def safe_read_df(df_path, encoding_):
    sep_ = SEP_MAP[df_path.split(".")[-1]]
    try:
        df = pd.read_csv(df_path, encoding=encoding_, sep=sep_)
    except:
        df = pd.read_excel(df_path, encoding=encoding_, sep=sep_)
    return df
