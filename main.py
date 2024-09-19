import openpyxl

if __name__ == '__main__':
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
    
    new_workbook.save("新文件地址.xlsx")
