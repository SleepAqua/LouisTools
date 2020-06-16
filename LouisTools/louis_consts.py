'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:27:40
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:56:56
'''
import os
import sys
from enum import Enum
from datetime import datetime


TODAY = datetime.now().strftime("%Y%m%d")

SEP_MAP = {"xls": "\t", "XLS": "\t", "CSV": ",", "csv": ",", "xlsx": "\t", "XLSX": "\t"}

EQUITY_TRADE_DAYS_PATH = "$EQUITY_TRADE_DAYS"
FUTURE_TRADE_DAYS_PATH = "$FUTURE_TRADE_DAYS"

MARKET_MAP = {"SZSE": "SZ", "SSE": "SH", "SZE": "SZ"}
