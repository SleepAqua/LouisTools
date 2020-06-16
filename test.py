from datetime import datetime
import LouisTools as LT


def parse_a_path(file_path):
    file_path = "/data/certain_data/%Y/%m/%Y%m%d.csv"
    return LT.louis_datetime.parse_date_in_str(file_path, LT.louis_consts.TODAY)

if __name__ == "__main__":
    print(LT.louis_consts.TODAY)
    print("-"*40)
    print(LT.louis_os.count_files(r"C:\Program Files (x86)"))
