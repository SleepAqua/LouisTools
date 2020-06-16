'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:41:58
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:40:27
'''
import os


def make_parent_dir(path_):
    parent_dir = os.path.dirname(path_)
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)

def make_dir(path_):
    if not os.path.isdir(path_):
        os.makedirs(path_)

def count_files(dir_):
    """ If the directory does not exist, return None. """
    if not os.path.isdir(dir_):
        return None
    return len(os.listdir(dir_))
