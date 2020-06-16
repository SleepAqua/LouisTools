from datetime import datetime
import LouisTools as LT
# from LouisTools import louis_consts


if __name__ == "__main__":
    print(LT.louis_consts.TODAY)
    print("-"*40)
    print(LT.louis_os.count_files(r"C:\Program Files (x86)"))
