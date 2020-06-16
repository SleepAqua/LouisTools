'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 17:06:58
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:08:20
'''
import keyring


def register(subject, username, password):
    """
    Save your password inside your computer permenately.
    """
    keyring.set_password(subject, username, password)

def peek_password(subject, username):
    """
    Access your password inside your computer.
    """
    return keyring.get_password(subject, username)