import os.path
import time

import openpyxl

import config
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


# 先识别是那个银行的交易流水
def get_bank_translation(file):
    print("start recognition translation type:", file)
    # 打开 Excel 文件
    workbook = openpyxl.load_workbook(file)

    try:
        # 获取当前活动工作表（默认为第一张）
        sheet = workbook.active

        # 遍历每一行并输出 A 列的值
        for row in sheet.iter_rows(min_row=1, max_row=config.prefetch_row, values_only=True):
            for cell in row:
                clazz = config.BankTranslation.get(cell)
                if clazz is not None:
                    return clazz

    finally:
        workbook.close()


def is_subset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.issubset(set2)


def get_bank_translation_records(execl_file, tx_class):
    workbook = openpyxl.load_workbook(execl_file)


    try:
        sheet = workbook.active

        # 是不是交易开始行, 在Excel中，行号和列号是从1开始的，而不是从0
        tx_start_row_number = 0

        # 转化为交易对象
        data = []

        for row in sheet.iter_rows(min_row=1):
            row_number, column_count, values, not_empty = read_row(row)
            if is_subset(tx_class.field_list, values):
                tx_start_row_number = row_number

            if tx_start_row_number != 0 and row_number > tx_start_row_number and not_empty:
                # 只需要指定长度的列表项，多的不要
                args = values[:len(tx_class.field_list)]
                tx = tx_class(*args)
                print(tx)
                data.append(tx)

        return data
    finally:
        workbook.close()

def read_row(row):
    row_number = 0
    column_count = 0
    values = []

    for cell in row:
        row_number = cell.row
        column_count += 1
        values.append(cell.value)

    return row_number, column_count, values, values.__getitem__(0) is not None


if __name__ == '__main__':
    init_env()

    reader = FileReader("/Users/snlan/py_path/report-tools/data")
    files = reader.read()

    for file in files:
        tx_clazz = get_bank_translation(file)
        if tx_clazz is not None:
            txs = get_bank_translation_records(file, tx_clazz)
            print(txs)
