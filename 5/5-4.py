__author__ = 'Cq'
"""
    读写excel文件
"""
import xlrd
import xlwt


def text_excel():
    # 使用第三方库xlrd和xlwt

    # 读取excel文件
    book = xlrd.open_workbook('demo.xlsx')
    sheets = book.sheets()

    # 获取行数列数
    print(sheets[0].nrows)
    print(sheets[0].ncols)

    # 单元操作
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(0, 0)
    print(cell.value)  # 文本值
    print(cell.ctype)  # 字段类型

    # 内置字段类型码
    print(xlrd.XL_CELL_NUMBER)
    print(xlrd.XL_CELL_TEXT)

    # 获取整行整列
    print(sheet.row(0))
    print(sheet.row_values(0))
    print(sheet.col(1))
    print(sheet.col_values(1))

    # 添加单元格内容
    wboot = xlwt.Workbook()

    wsheet = wboot.add_sheet('sheet1')
    wsheet.write(0, 0, 'aaaaaaaaaa')
    wboot.save('output.xlsx')


def do_sum_excel():
    """
        excel记录为
        姓名 语文 英语 数据，我们加一个总分列，并计算每行的3门成绩之和
    :return:
    """
    rbook = xlrd.open_workbook('demo.xlsx')
    rsheet = rbook.sheet_by_index(0)

    nc = rsheet.ncols
    rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

    for row in range(1, rsheet.nrows):
        s = sum(rsheet.row_values(row, 1))
        rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, s, None)


    wbook = xlwt.Workbook()
    wsheet = wbook.add_sheet(rsheet.name)
    style = xlwt.easyxf('align: vertical center, horizontal center')

    for r in range(rsheet.nrows):
        for c in range(rsheet.ncols):
            wsheet.write(r, c, rsheet.cell_value(r, c), style)

    wbook.save("output.xlsx")


if __name__ == '__main__':
    # text_excel()
    do_sum_excel()