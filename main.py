import os.path
import time

import openpyxl

from file_reader import FileReader

output_dir = 'output'


def init_env():
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)


def get_file_path(file_name):
    return os.path.join(output_dir, file_name)


# 获取时间字符串
def get_time():
    return time.strftime("%Y-%m-%d %H：%M", time.localtime())


if __name__ == '__main__':
    init_env()

    # 打开 Excel 文件
    workbook = openpyxl.load_workbook("data/销售明细.xlsx")

    # 获取当前活动工作表（默认为第一张）
    sheet = workbook.active

    # 遍历每一行并输出 A 列的值
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(row)

    new_workbook = openpyxl.Workbook()
    new_sheet = new_workbook.active
    new_sheet["A1"] = "Hello, World!"

    new_workbook.save(get_file_path("新文件地址_{}.xlsx".format(get_time())))

    reader = FileReader("/Users/snlan/py_path/report-tools/data")
    reader.read()
