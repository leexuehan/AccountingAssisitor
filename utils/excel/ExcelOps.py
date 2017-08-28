import os

import xlwt
from PyQt5.QtWidgets import QMessageBox

from utils.sql.RecordDetailDbUtils import RecordDetailDbUtils


class ExcelOps(object):
    def __init__(self):
        self.totalColumns = 0
        self.totalRows = 0
        self.sheet = None
        self.MAX_COAL_SORT_NUM_EVERY_BLOCK = 3
        self.BLOCK_INTERVAL = 1
        self.title_xf_style = self.__init_title_xf_style()
        self.data_xf_style = self.__get_data_xf_style()
        self.parent_dir = '账目'

    def __init_title_xf_style(self):
        title_xf_style = xlwt.easyxf('align:wrap on,vert center, horiz center;')
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        title_xf_style.borders = borders
        return title_xf_style

    def __get_data_xf_style(self):
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
        if os.path.exists(self.parent_dir) is False:
            os.mkdir(self.parent_dir)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('逐车明细', cell_overwrite_ok=True)
        # 初始化标题
        start_col = 0
        sheet.write(0, start_col, '序号', self.title_xf_style)
        sheet.write_merge(0, 0, start_col + 1, start_col + 2, '日期', self.title_xf_style)
        sheet.write(0, start_col + 3, '客户名称', self.title_xf_style)
        sheet.write(0, start_col + 4, '车号', self.title_xf_style)
        sheet.write(0, start_col + 5, '煤种', self.title_xf_style)
        sheet.write(0, start_col + 6, '煤种单价', self.title_xf_style)
        sheet.write(0, start_col + 7, '煤种计价方式', self.title_xf_style)
        sheet.write(0, start_col + 8, '煤款', self.title_xf_style)
        sheet.write(0, start_col + 9, '吨位', self.title_xf_style)

        sheet.write(0, start_col + 11, '序号', self.title_xf_style)
        sheet.write_merge(0, 0, start_col + 12, start_col + 13, '日期', self.title_xf_style)
        sheet.write(0, start_col + 14, '票种', self.title_xf_style)
        sheet.write(0, start_col + 15, '票种单价', self.title_xf_style)
        sheet.write(0, start_col + 16, '票种计价方式', self.title_xf_style)
        sheet.write(0, start_col + 17, '票款', self.title_xf_style)
        sheet.write(0, start_col + 18, '应收', self.title_xf_style)
        sheet.write(0, start_col + 19, '利润', self.title_xf_style)
        # 填入数据
        row = 1
        for record in records:
            column = 1
            sheet.write(row, 0, row, self.title_xf_style)
            sheet.write(row, 11, row, self.title_xf_style)
            for item in record:
                if column == 1:
                    # 对日期一列特殊处理,同时写两块的两列
                    sheet.write_merge(row, row, column, column + 1, item, self.data_xf_style)
                    sheet.write_merge(row, row, column + 11, column + 12, item, self.data_xf_style)
                    column += 2
                    continue
                if column == 9:
                    sheet.write(row, column, item, self.data_xf_style)
                    # 进入下一块
                    column += 5
                    continue
                sheet.write(row, column, item, self.data_xf_style)
                column += 1
            row += 1
        # 最后几行 写吨位合计、煤款合计、利润合计??????时间段查询
        results = RecordDetailDbUtils().query_total_tons_coalfunds_profit()
        total_tons = results[0][0]
        total_coal_funds = results[0][1]
        total_profit = results[0][2]
        sheet.write(row, 3, '吨位合计', self.title_xf_style)
        sheet.write_merge(row, row, 4, 5, str(total_tons) + '吨', self.data_xf_style)
        sheet.write(row + 1, 3, '煤款合计', self.title_xf_style)
        sheet.write_merge(row + 1, row + 1, 4, 5, str(total_coal_funds) + '元', self.data_xf_style)
        sheet.write(row + 2, 3, '利润合计', self.title_xf_style)
        sheet.write_merge(row + 2, row + 2, 4, 5, str(total_profit) + '元', self.data_xf_style)
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

    def generate_ticket_excel(self, compute_begin_date, compute_end_date):
        start_date_for_sql = compute_begin_date.strftime('%Y/%m/%d')
        # start_date_for_sql = '2017/08/22'
        end_date_for_sql = compute_end_date.strftime('%Y/%m/%d')
        # end_date_for_sql = '2017/09/27'
        file_name = '票统计' + compute_begin_date.strftime('%Y.%m.%d') + '-' + compute_end_date.strftime(
            '%Y.%m.%d') + '.xls'
        file_name = 'ticket.xls'
        if os.path.exists(self.parent_dir + '\\' + file_name):
            QMessageBox.critical(self, "Critical", self.tr('票统计账目已经存在，如想重新生成，请删除该文件后重试'))
            return
        if os.path.exists(self.parent_dir) is False:
            os.mkdir(self.parent_dir)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('票统计', cell_overwrite_ok=True)
        utils = RecordDetailDbUtils()
        # 先写标题栏(日期、票种)
        records = utils.query_ticket_sorts(start_date_for_sql, end_date_for_sql)
        sheet.write_merge(0, 0, 0, 1, '日期', self.title_xf_style)
        start_cols = 2
        columns_dict = {}
        for record in records:
            ticket_name = record[0]
            columns_dict[ticket_name] = start_cols
            sheet.write(0, start_cols, ticket_name, self.title_xf_style)
            start_cols += 1
        ticket_sort_num = len(records)
        # 再填写数据
        records = utils.query_ticket_and_every_count(start_date_for_sql, end_date_for_sql)
        last_data_insert_row = 0
        last_date_inserted = None
        for record in records:
            date = record[0]
            ticket_name = record[1]
            ticket_num = record[2]
            if date != last_date_inserted:
                last_data_insert_row += 1
            sheet.write_merge(last_data_insert_row, last_data_insert_row, 0, 1, date, self.title_xf_style)
            # 先默认填写为 0
            for index in range(2, ticket_sort_num + 2):
                sheet.write(last_data_insert_row, index, 0, self.data_xf_style)
            sheet.write(last_data_insert_row, columns_dict[ticket_name], ticket_num, self.data_xf_style)
        # 填写各票种合计
        records = utils.query_ticket_total_count(start_date_for_sql, end_date_for_sql)
        sheet.write_merge(last_data_insert_row + 1, last_data_insert_row + 1, 0, 1, '合计', self.title_xf_style)
        all_ticket_sum = 0
        for record in records:
            ticket_name = record[0]
            every_ticket_sum_count = record[1]
            all_ticket_sum += every_ticket_sum_count
            sheet.write(last_data_insert_row + 1, columns_dict[ticket_name], every_ticket_sum_count, self.data_xf_style)
        # 填写总票种合计
        sheet.write_merge(last_data_insert_row + 2, last_data_insert_row + 2, 0, 1, '总票数合计',
                          self.title_xf_style)
        sheet.write_merge(last_data_insert_row + 2, last_data_insert_row + 2, 2, 1 + ticket_sort_num, all_ticket_sum,
                          self.title_xf_style)
        workbook.save(self.parent_dir + '\\' + file_name)

    def generate_person_excel(self, compute_begin_date, compute_end_date, person_name):
        start_date_for_sql = compute_begin_date.strftime('%Y/%m/%d')
        # start_date_for_sql = '2017/08/22'
        end_date_for_sql = compute_end_date.strftime('%Y/%m/%d')
        # end_date_for_sql = '2017/09/27'
        file_name = person_name + compute_begin_date.strftime('%Y.%m.%d') + '-' + compute_end_date.strftime(
            '%Y.%m.%d') + '.xls'
        # file_name = 'personal_account.xls'
        if os.path.exists(self.parent_dir + '\\' + file_name):
            QMessageBox.critical(self, "Critical", self.tr('个人应收账目已经存在，如想重新生成，请删除该文件后重试'))
            return
        if os.path.exists(self.parent_dir) is False:
            os.mkdir(self.parent_dir)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(person_name + '个人应收', cell_overwrite_ok=True)
        utils = RecordDetailDbUtils()
        # 先写标题栏(日期、煤款合计、车数)
        records = utils.query_personal_account(start_date_for_sql, end_date_for_sql, person_name)
        sheet.write_merge(0, 0, 0, 1, '日期', self.title_xf_style)
        sheet.write(0, 2, '煤款合计', self.title_xf_style)
        sheet.write(0, 3, '车数', self.title_xf_style)
        # 填入数据
        last_data_insert_row = 0
        last_date_inserted = None
        total_funds = 0
        total_car_count = 0
        for record in records:
            date = record[0]
            total_funds_every_day = record[1]
            car_count_every_day = record[2]
            if date != last_date_inserted:
                last_data_insert_row += 1
            insert_row_position = last_data_insert_row
            sheet.write_merge(insert_row_position, insert_row_position, 0, 1, date, self.title_xf_style)
            sheet.write(insert_row_position, 2, total_funds_every_day, self.data_xf_style)
            sheet.write(insert_row_position, 3, car_count_every_day, self.data_xf_style)
            total_funds += total_funds_every_day
            total_car_count += car_count_every_day
        # 填入合计金额
        sheet.write_merge(last_data_insert_row + 1, last_data_insert_row + 1, 0, 1, '总计', self.title_xf_style)
        sheet.write(last_data_insert_row + 1, 2, total_funds, self.data_xf_style)
        sheet.write(last_data_insert_row + 1, 3, total_car_count, self.data_xf_style)
        workbook.save(self.parent_dir + '\\' + file_name)


if __name__ == '__main__':
    ExcelOps().generate_person_excel('2017/08/22', '2017/09/27', 'aaa')
    # ExcelOps().method_name('test.xls', 3, 3)
