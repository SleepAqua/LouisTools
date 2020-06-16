'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:27:40
@LastEditors: Louis
@LastEditTime: 2020-06-15 18:02:38
'''
import os
from datetime import datetime
from email.mime.text import MIMEText
import smtplib

from LouisTools.louis_consts import TODAY
from LouisTools.louis_datetime import parse_date_in_str
from LouisTools.louis_keyrings import peek_password


TO = 'dqyyrlfy@gmail.com'
FROM = 'dqyyrlfy@gmail.com'
SMTP_SERVER= 'smtp.exmail.gmail.com'
USR = 'Louis'
PWD = peek_password("Louis", "Louis")
LOG_PATH = "$HOME/log/%Y%m%d.log"

def simple_email(from_=FROM, to_=TO, server=SMTP_SERVER, user=USR, password=PWD, file_path=LOG_PATH):
    """ Send a email with one attach (for log sending) """
    log_file = parse_date_in_str(file_path, TODAY)
    if not os.path.isfile(log_file):
        msg = MIMEText(f"No log file of {TODAY}")
        msg["Subject"] = f"NO LOG {TODAY}"
    else:
        with open(log_file, "r", encoding="utf8") as fp:
            msg = MIMEText(fp.read())
        msg["Subject"] = f"Log {TODAY}"
    msg["From"] = from_
    msg["To"] = to_

    server = smtplib.SMTP(server)
    server.login(user, password)
    server.sendmail(from_, [to_], msg.as_string())
    server.quit()

if __name__ == '__main__':
    simple_email()