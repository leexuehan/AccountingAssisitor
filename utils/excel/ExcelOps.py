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
        # 最后几列 写吨位合计、煤款合计、利润合计
        results = RecordDetailDbUtils().query_total_tons_coalfunds_profit()
        total_tons = results[0][0]
        total_coal_funds = results[0][1]
        total_profit = results[0][2]
        sheet.write(0, 15, '吨位合计')
        sheet.write(1, 15, total_tons)
        sheet.write(0, 16, '煤款合计')
        sheet.write(1, 16, total_coal_funds)
        sheet.write(0, 17, '利润合计')
        sheet.write(1, 17, total_profit)
        workbook.save(path + '\\' + file_name)

    def generate_coal_excel(self, start_date, end_date):
        coal_column_dict = {}
        date_position_dict = {}
        xf_style = xlwt.easyxf('align:wrap on,vert center, horiz center;')
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('分煤种销量', cell_overwrite_ok=True)
        sheet.write_merge(0, 1, 0, 1, '日期', xf_style)

        results = RecordDetailDbUtils().query_coal_info_group_by_coal_name(start_date, end_date)
        record_count = 0
        row_index = 2
        next_col = 2
        while record_count < len(results):
            record = results[record_count]
            date = record[0]
            coal_name = record[1]
            coal_fund_sum = record[2]
            weight_value_sum = record[3]
            if coal_name not in coal_column_dict:
                sheet.write_merge(0, 0, next_col, next_col + 1, coal_name, xf_style)
                # add title
                sheet.write(1, next_col, '吨位', xf_style)
                sheet.write(1, next_col + 1, '总价', xf_style)
                # add position info into coal_column_dict
                coal_column_dict[coal_name] = [next_col, next_col + 1]

            if date not in date_position_dict:
                # add date
                date_position_dict[date] = row_index
                sheet.write_merge(row_index, row_index, 0, 1, date, xf_style)
                row_index += 1

            # write data
            weight_position = coal_column_dict[coal_name][0]
            coal_fund_position = coal_column_dict[coal_name][1]
            row_position = date_position_dict[date]
            sheet.write(row_position, weight_position, weight_value_sum, xf_style)
            sheet.write(row_position, coal_fund_position, coal_fund_sum, xf_style)
            next_col += 2
            record_count += 1

        file_name = 'test.xls'
        workbook.save(file_name)
        print(coal_column_dict)
        print(date_position_dict)
        # sheet_to_read = xlrd.open_workbook('test.xls').sheets()[0]
        # book = xlrd.open_workbook('test.xls')
        # new_book = copy(book)
        # sheet_to_write = new_book.get_sheet(0)
        # # init all the empty cells into 0
        # for row in range(2, row_index):
        #     for col in range(2, next_col):
        #         if sheet_to_read.cell_value(row, col) is '':
        #             print("!!!!!!!!!!")
        #             sheet_to_write.write(row, col, 0)
        #             new_book.save('test.xls')

    def method_name(self, file_name, next_col, row_index):
        sheet_to_read = xlrd.open_workbook('test.xls').sheets()[0]
        book = xlrd.open_workbook('test.xls')
        new_book = copy(book)
        sheet_to_write = new_book.get_sheet(0)
        # init all the empty cells into 0
        if sheet_to_read.cell_value(3, 3) is '':
            print("!!!!!!!!!!")
            sheet_to_write.write(3, 3, 0)
            new_book.save('test.xls')

            # file_name = '分煤种销量' + start_date.strftime('%Y.%m.%d') + '-' + end_date.strftime('%Y.%m.%d') + '.xls'
            # if os.path.exists(path + '\\' + file_name):
            #     QMessageBox.critical(self, "Critical", self.tr('分煤种销量账目已经存在，如想重新生成，请删除该文件后重试'))
            #     return
            # style = xlwt.XFStyle()

            # 从逐车明细里面按照日期排序，找出最早的日期，之后遍历记录，动态添加列
            # 横坐标按照（吨位，总价）形式出现，纵坐标以日期形式出现,考虑合并单元格

            # sheet.write(0, 0, '序号')
            # sheet.write(0, 1, '日期')
            # sheet.write(0, 2, '吨位')
            # sheet.write(0, 3, '总价')

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


if __name__ == '__main__':
    ExcelOps().generate_coal_excel('2017/08/22', '2017/08/24')
    # ExcelOps().method_name('test.xls', 3, 3)
