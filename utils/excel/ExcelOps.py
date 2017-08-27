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
        self.MAX_COAL_SORT_NUM_EVERY_BLOCK = 3
        self.BLOCK_INTERVAL = 1
        self.title_xf_style = self.init_title_xf_style()
        self.data_xf_style = self.get_data_xf_style()
        self.parent_dir = '账目'

    def init_title_xf_style(self):
        title_xf_style = xlwt.easyxf('align:wrap on,vert center, horiz center;')
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        title_xf_style.borders = borders
        return title_xf_style

    def get_data_xf_style(self):
        data_xf_style = xlwt.easyxf('align:wrap on,vert center, horiz right;')
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        data_xf_style.borders = borders
        return data_xf_style

    def generate_record_detail_by_car_excel(self, start_date, end_date):
        start_date_for_sql = start_date.strftime('%Y/%m/%d')
        end_date_for_sql = end_date.strftime('%Y/%m/%d')
        records = RecordDetailDbUtils().query_all_records(start_date_for_sql, end_date_for_sql)
        file_name = '逐车明细' + start_date.strftime('%Y.%m.%d') + '-' + end_date.strftime('%Y.%m.%d') + '.xls'
        if os.path.exists(self.parent_dir + '\\' + file_name):
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
        workbook.save(self.parent_dir + '\\' + file_name)

    def generate_coal_excel(self, start_date, end_date):
        # 先初始化标题栏
        utils = RecordDetailDbUtils()
        start_date_for_sql = start_date.strftime('%Y/%m/%d')
        end_date_for_sql = end_date.strftime('%Y/%m/%d')
        record_sorts = utils.query_all_coal_sorts(start_date_for_sql, end_date_for_sql)
        # to decide if split to blocks
        record_sort_num_in_db = len(record_sorts)
        print('record sort num from db is', record_sort_num_in_db)
        # write and init columns dict in every block
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('分煤种销量', cell_overwrite_ok=True)
        # 填入日期、吨位、总价等标题，返回所有要填入数据的列
        cols_to_be_filled_with_data = self.fill_tons_and_fund_title(record_sorts, sheet)
        # 在标题栏填充煤种标题
        fill_info = self.fill_coal_name(record_sorts, sheet)
        # 填入煤种数据
        self.fill_data(sheet, cols_to_be_filled_with_data, fill_info, end_date_for_sql,
                       start_date_for_sql)
        file_name = '分煤种销量' + start_date.strftime('%Y.%m.%d') + '-' + end_date.strftime('%Y.%m.%d') + '.xls'
        workbook.save(self.parent_dir + '\\' + file_name)

    def fill_coal_name(self, record_sorts, sheet):
        record_sort_num_in_db = len(record_sorts)
        column_dict = {}
        date_cols = [0]  # the column can be filled with date
        xf_style = self.title_xf_style
        current_index = 2
        print('record_sort_num_in_db is ::::::', record_sort_num_in_db)
        for index in range(0, record_sort_num_in_db):
            coal_name = record_sorts[index][0]
            column_dict[coal_name] = (current_index, current_index + 1)
            sheet.write_merge(0, 0, current_index, current_index + 1, coal_name, xf_style)
            # cross space when met border
            if (self.MAX_COAL_SORT_NUM_EVERY_BLOCK - 1) == 0 or (
                            index != 0 and (index + 1) % self.MAX_COAL_SORT_NUM_EVERY_BLOCK == 0):
                print('met border,current index:', current_index)
                current_index += 1 + self.BLOCK_INTERVAL + 3
                if (index + 1) < record_sort_num_in_db:
                    date_cols.append(current_index - 2)
                print('date_cols:::::::::', date_cols)
                print('met border and jump to next block,index will be', current_index)
            else:
                current_index += 2
        return column_dict, date_cols

    def fill_data(self, sheet, cols_to_be_filled_with_data, fill_info, end_date, start_date):
        data_xf_style = self.data_xf_style
        column_dict = fill_info[0]  # 填写数据
        cols_to_be_filled_with_date = fill_info[1]  # 可以填写日期的列
        # first query info from db
        utils = RecordDetailDbUtils()
        coal_record_info = utils.query_coal_info_group_by_coal_name(start_date, end_date)
        current_record_index = 0
        last_date_inserted = None
        last_insert_row_cursor = 1
        while current_record_index < len(coal_record_info):
            record = coal_record_info[current_record_index]
            date = record[0]
            # because the record are already sorted so just compare with last row
            if date != last_date_inserted:
                insert_row_position = last_insert_row_cursor + 1
            else:
                insert_row_position = last_insert_row_cursor
            # fill date
            for col in cols_to_be_filled_with_date:
                print('insert date:::::', insert_row_position, insert_row_position, col, col + 1)
                sheet.write_merge(insert_row_position, insert_row_position, col, col + 1, date, data_xf_style)
            # find all the valid columns and fill it with 0
            print('init cols data to be 0:::::', cols_to_be_filled_with_data)
            for col in cols_to_be_filled_with_data:
                sheet.write(insert_row_position, col[0], 0, data_xf_style)
                sheet.write(insert_row_position, col[1], 0, data_xf_style)
            # according to result from db fill in the row
            last_insert_row_cursor = insert_row_position
            coal_name = record[1]
            weight_value_sum = record[2]
            coal_fund_sum = record[3]
            weight_value_sum_col = column_dict[coal_name][0]
            coal_fund_sum_col = weight_value_sum_col + 1

            sheet.write(insert_row_position, weight_value_sum_col, weight_value_sum, data_xf_style)
            sheet.write(insert_row_position, coal_fund_sum_col, coal_fund_sum, data_xf_style)
            current_record_index += 1
        # 最后填入各种煤的合计值
        self.fill_in_all_total_value(sheet, cols_to_be_filled_with_date, last_insert_row_cursor + 1, column_dict,
                                     start_date, end_date)

    # 填入日期、吨位、总价等标题，返回所有要填入数据的列
    def fill_tons_and_fund_title(self, record_sorts, sheet):
        record_sort_num_in_db = len(record_sorts)
        xf_style = self.title_xf_style
        data_col_set = []
        end_column_index = 0
        # 填入整的整数块
        block_num = int(record_sort_num_in_db / self.MAX_COAL_SORT_NUM_EVERY_BLOCK)
        tail_num = record_sort_num_in_db % self.MAX_COAL_SORT_NUM_EVERY_BLOCK
        for num in range(0, block_num):
            start_column_index = 2 + (self.BLOCK_INTERVAL + self.MAX_COAL_SORT_NUM_EVERY_BLOCK * 2 + 2) * num
            end_column_index = start_column_index + self.MAX_COAL_SORT_NUM_EVERY_BLOCK * 2
            sheet.write_merge(0, 1, start_column_index - 2, start_column_index - 1, '日期', xf_style)
            for column_index in range(start_column_index, end_column_index, 2):
                sheet.write(1, column_index, '吨位', xf_style)
                sheet.write(1, column_index + 1, '总价', xf_style)
                data_col_set.append([column_index, column_index + 1])
        # 如果有零头的话，填入零头
        print('tail num is:', tail_num)
        if tail_num is not 0:
            if block_num is 0:
                start_column_index = end_column_index
            else:
                start_column_index = end_column_index + self.BLOCK_INTERVAL
            sheet.write_merge(0, 1, start_column_index, start_column_index + 1, '日期', xf_style)
            end_column_index = start_column_index + 2 + tail_num * 2
            for column_index in range(start_column_index + 2, end_column_index, 2):
                sheet.write(1, column_index, '吨位', xf_style)
                sheet.write(1, column_index + 1, '总价', xf_style)
                data_col_set.append([column_index, column_index + 1])
        return data_col_set

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

    def get_coal_name_position(self):
        pass

    def get_coal_fund_sum_position(self):
        pass

    def get_weight_value_sum_position(self):
        pass

    def fill_in_all_total_value(self, sheet, cols_to_be_filled_with_date, start_row, column_dict, start_date, end_date):
        utils = RecordDetailDbUtils()
        records = utils.query_weight_sum_and_fund_sum_by_coal(start_date, end_date)
        for col in cols_to_be_filled_with_date:
            sheet.write_merge(start_row, start_row, col, col + 1, '合计', self.title_xf_style)
        for record in records:
            coal_name = record[0]
            weight_value_sum = record[1]
            coal_fund_sum = record[2]
            print(coal_name, weight_value_sum, coal_fund_sum)
            weight_value_sum_position = column_dict[coal_name][0]
            coal_fund_sum_position = column_dict[coal_name][1]
            print('insert total num position', weight_value_sum_position, coal_fund_sum_position)
            # 各煤种总吨位、总价款
            sheet.write(start_row, coal_fund_sum_position, coal_fund_sum, self.data_xf_style)
            sheet.write(start_row, weight_value_sum_position, weight_value_sum, self.data_xf_style)
        # 所有煤种合计总吨位、总价款
        results = utils.query_all_coal_weight_sum_and_fund_sum(start_date, end_date)
        sheet.write_merge(start_row + 1, start_row + 1, 0, 1, '总销量', self.title_xf_style)
        sheet.write_merge(start_row + 1, start_row + 1, 2, self.MAX_COAL_SORT_NUM_EVERY_BLOCK * 2 + 1,
                          str(results[0][0]) + '吨', self.title_xf_style)
        sheet.write_merge(start_row + 2, start_row + 2, 0, 1, '总价款', self.title_xf_style)
        sheet.write_merge(start_row + 2, start_row + 2, 2, self.MAX_COAL_SORT_NUM_EVERY_BLOCK * 2 + 1,
                          str(results[0][1]) + '元', self.title_xf_style)


if __name__ == '__main__':
    ExcelOps().generate_coal_excel('2017/08/22', '2017/09/27')
    # ExcelOps().method_name('test.xls', 3, 3)
