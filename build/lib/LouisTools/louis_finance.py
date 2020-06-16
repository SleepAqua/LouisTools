'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:41:58
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:53:13
'''
import pandas as pd
from datetime import date, time, datetime, timedelta

from LouisTools.louis_consts import EQUITY_TRADE_DAYS_PATH, FUTURE_TRADE_DAYS_PATH
from LouisTools.louis_log import single_lvl_logger


LOGGER = single_lvl_logger("LouisTools")

def gen_min_index(date, freq):
    """ Generate a typical trading times index. 9:30-11:30 and 13:00-15:00 """
    am_times = [datetime.combine(date, time(9, 30)) + timedelta(minutes=i*freq)
                for i in range(1, 120 // freq + 1)]
    pm_times = [datetime.combine(date, time(13, 0)) + timedelta(minutes=i*freq)
                for i in range(1, 120 // freq + 1)]
    return am_times + pm_times

def get_file_days_between(date_file, start_date, end_date):
    """ 
    Return a Series containing the dates betweeen start_date and end_date in the date_file.
    @date_file: a csv file containing only dates series
    """
    trade_days = pd.Series(pd.read_csv(date_file, header=None, dtype={0:str})[0])
    return trade_days.loc[(trade_days >= start_date) & (trade_days <= end_date)]

def format_secode(x):
    """ Add market suffix SH or SZ for stock code """
    if not isinstance(x, str):
        x = str(x.zfill(9))
    if x[0] == "6" or x[0] == "9":
        return f"{x}.SH"
    elif x[0] == "0" or x[0] == "2" or x[0] == "3":
        return f"{x}.SZ"
    else:
        LOGGER.warning("This is not a SecuCode for stocks.")
        return None
