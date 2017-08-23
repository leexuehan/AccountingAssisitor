import datetime
import os

import xlrd
import xlwt
from PyQt5.QtWidgets import QMessageBox
from xlutils.copy import copy

from utils.sql.RecordDetailDbUtils import RecordDetailDbUtils


class ExcelOps(object):
    def __init__(self):
        self.totalColumns = 0
        self.totalRows = 0
        self.sheet = None

    def generate_record_detail_by_car_excel(self, records, start_date, end_date):
        path = '账目'
        file_name = '逐车明细' + start_date.strftime('%Y.%m.%d') + '-' + end_date.strftime('%Y.%m.%d') + '.xls'
        if os.path.exists(path + '\\' + file_name):
            QMessageBox.critical(self, "Critical", self.tr('逐车明细账目已经存在，如想重新生成，请删除该文件后重试'))
            return
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('逐车明细', cell_overwrite_ok=True)
        sheet.write(0, 0, '序号')
        sheet.write(0, 1, '日期')
        sheet.write(0, 2, '客户名称')
        sheet.write(0, 3, '车号')
        sheet.write(0, 4, '煤种')
        sheet.write(0, 5, '煤种单价')
        sheet.write(0, 6, '煤种计价方式')
        sheet.write(0, 7, '煤款')
        sheet.write(0, 8, '吨位')
        sheet.write(0, 9, '票种')
        sheet.write(0, 10, '票种单价')
        sheet.write(0, 11, '票种计价方式')
        sheet.write(0, 12, '票款')
        sheet.write(0, 13, '应收')
        sheet.write(0, 14, '利润')
        row = 1
        for record in records:
            column = 1
            sheet.write(row, 0, row)
            for item in record:
                sheet.write(row, column, item)
                column += 1
            row += 1
        # 最后几行 写吨位合计、煤款合计、利润合计
        results = RecordDetailDbUtils().query_total_tons_coalfunds_profit()
        total_tons = results[0][0]
        total_coal_funds = results[0][1]
        total_profit = results[0][2]
        sheet.write(row, 0, '吨位合计')
        sheet.write(row, 1, total_tons)
        sheet.write(row + 1, 0, '煤款合计')
        sheet.write(row + 1, 1, total_coal_funds)
        sheet.write(row + 2, 0, '利润合计')
        sheet.write(row + 2, 1, total_profit)
        workbook.save(path + '\\' + file_name)

    def generate_param_table(self):
        if os.path.exists('参数表.xls'):
            workbook = xlrd.open_workbook('参数表.xls')
            table = workbook.sheets()[0]
            self.totalColumns = table.ncols
            self.totalRows = table.nrows
        else:
            workbook = xlwt.Workbook()
            self.sheet = workbook.add_sheet('参数表', cell_overwrite_ok=True)
            self.init_param_table(self.sheet)
            workbook.save('参数表.xls')
        print("init param table successfully")

    # 初始化参数表
    def init_param_table(self, sheet):
        # 初始化参数表中的煤种类
        column = 1
        with open('煤种列表.txt', 'r') as file:
            for line in file:
                sheet.write(0, column, line)
                column += 1
            self.totalColumns = column

    # 在表格里更新煤种的价格
    def update_param_table(self, item_selected, price_input, begin_date, end_date):
        if begin_date > end_date:
            return False
        kind_index = self.find_index_of_kind(item_selected)
        book = xlrd.open_workbook('参数表.xls')
        new_book = copy(book)
        sheet_to_write = new_book.get_sheet(0)
        dates = self.date_range(begin_date, end_date)
        print("dates length is : " + str(dates.__len__()))
        for date in dates:
            # 一行一行插入数据
            sheet_to_read = xlrd.open_workbook('参数表.xls').sheets()[0]
            position = self.find_position_to_insert(date)
            # 从最后一行开始移动
            print("insert position is : " + str(position))
            # 防止将第一行的煤种拷贝下来
            if position != 1:
                row_cursor = self.totalRows
                while row_cursor >= position:
                    for col_cursor in range(0, self.totalColumns):
                        cell_value = sheet_to_read.cell_value(row_cursor - 1, col_cursor)
                        print("value to copy is : " + str(cell_value))
                        sheet_to_write.write(row_cursor, col_cursor, cell_value)
                    row_cursor -= 1
            # 在该行写入数据
            sheet_to_write.write(position, 0, date)
            sheet_to_write.write(position, kind_index, price_input)
            new_book.save('参数表.xls')
            # 此时表的总行数已经增加 1 个单位
            self.totalRows += 1
        new_book.save('参数表.xls')
        return True

    @staticmethod
    def date_range(beginDate, endDate):
        dates = []
        dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
        date = beginDate[:]
        while date <= endDate:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime("%Y-%m-%d")
        return dates

    def find_index_of_date(self, date):
        sheet = xlrd.open_workbook('参数表.xls').sheets()[0]
        for row in range(self.totalRows):
            cell_value = sheet.cell_value(row, 0)
            if cell_value == str(date):
                return row

    def find_index_of_kind(self, item_selected):
        sheet = xlrd.open_workbook('参数表.xls').sheets()[0]
        for column in range(1, self.totalColumns):
            cell_value = sheet.cell_value(0, column)
            if cell_value == str(item_selected + '\n'):
                return column

    def find_position_to_insert(self, insert_date):
        sheet = xlrd.open_workbook('参数表.xls').sheets()[0]
        position = 1
        for row in range(1, self.totalRows):
            cell_value = sheet.cell_value(row, 0)
            if str(insert_date) <= cell_value:
                position = row
                break
                # 如果比较完都没有比插入值大的,那么就以最后一行作为插入位置
            if row == self.totalRows - 1:
                position = self.totalRows
        return position

    def move_data_already_exists(self, position, cols):
        book = xlrd.open_workbook('参数表.xls')
        new_book = copy(book)
        sheet_for_write = new_book.get_sheet(0)
        sheet_for_read = xlrd.open_workbook('参数表.xls').sheets()[0]
        # 从最后一行开始移动
        row_cursor = self.totalRows
        while row_cursor >= position:
            for col_cursor in range(0, self.totalColumns):
                cell_value = sheet_for_read.cell_value(row_cursor - 1, col_cursor)
                sheet_for_write.write(row_cursor, col_cursor, cell_value)
            row_cursor -= 1
        new_book.save('参数表.xls')
