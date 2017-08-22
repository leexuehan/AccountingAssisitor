import os

import xlwt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.account_results import Ui_Account_Dialog
from utils.account.AccurateAccountingStrategy import AccurateAccountingStrategy
from utils.account.RoughAccountingStrategy import RoughAccountingStrategy
from utils.sql.RecordDetailDbUtils import RecordDetailDbUtils


class AccountDialog(QDialog):
    def __init__(self, parent=None):
        super(AccountDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Account_Dialog()
        self.ui.setupUi(self)

        # init hide components
        self.ui.people_names.hide()
        self.ui.progressBar.hide()

        # init combox
        self.model = QStandardItemModel()
        self.load_all_persons()

        # init vars
        self.make_account_by_person = False
        self.selected_name = None
        self.count_small_change = True
        self.compute_begin_date = None
        self.compute_end_date = None

    def show_person_combox(self, state):
        if state == Qt.Checked:
            self.make_account_by_person = True
            self.ui.people_names.setVisible(True)
        else:
            self.make_account_by_person = False
            self.ui.people_names.hide()

    def on_select_begin_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            format_date_str = date.strftime('%Y/%m/%d')
            print("value get from calendar window is:" + format_date_str)
            self.ui.start_date_display.setText(format_date_str)
            self.compute_begin_date = format_date_str
        calendarDialog.destroy()

    def on_select_end_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            format_date_str = date.strftime('%Y/%m/%d')
            print("value get from calendar window is:" + format_date_str)
            if format_date_str < self.compute_begin_date:
                QMessageBox.critical(self, "Critical", self.tr('截止日期不能小于起始日期，请重新选择'))
                return
            self.ui.end_date_display.setText(format_date_str)
            self.compute_end_date = format_date_str
        calendarDialog.destroy()

    def on_person_name_select_finished(self, item):
        self.selected_name = self.people_names_collection[item]

    def count_small_change(self, state):
        if state == Qt.Checked:
            self.count_small_change = False
        else:
            self.count_small_change = True

    def on_start_compute_cmd(self):
        print("begin to compute account......")
        if self.valid_params() is False:
            return
        if self.count_small_change is True:
            strategy = AccurateAccountingStrategy()
        else:
            strategy = RoughAccountingStrategy()
        self.generate_record_detail_by_car_excel()



        # context = HTML_MODEL['account_result_show']
        # account_title = '账目明细(%s~%s)' % (self.compute_begin_date, self.compute_end_date)
        # data = ''
        # for name in self.selected_persons:
        #     coal_total_sell_price = strategy.all_coals_sell_perice_by_person(name)
        #     coal_total_purchase_price = strategy.all_coals_purchase_cost_by_person(name)
        #     ticket_total_sell_price = strategy.all_ticket_sell_price_by_person(name)
        #     ticket_total_purchase_price = strategy.all_ticket_purchase_price_by_person(name)
        #     total_profit = (coal_total_sell_price + ticket_total_sell_price) - (
        #         coal_total_purchase_price + ticket_total_purchase_price)
        #     line_data = '<tr><td>' + name + '</td><td>' + str(coal_total_sell_price) + '</td><td>' + str(
        #         coal_total_purchase_price) \
        #                 + '</td><td>' + str(ticket_total_sell_price) + '</td><td>' + str(ticket_total_purchase_price) \
        #                 + '</td><td>' + str(total_profit) + '</td></tr>'
        #     data += line_data
        # context = context % (account_title, data)
        # print("context is :\n" + context)

    def load_all_persons(self):
        result = RecordDetailDbUtils().query_all_person_names()
        self.people_names_collection = []
        for name in result:
            self.people_names_collection.append(name[0])
        self.ui.people_names.addItems(self.people_names_collection)

    def valid_params(self):
        if self.make_account_by_person is True and self.selected_name is None:
            QMessageBox.critical(self, "Critical", self.tr('没有选择人名'))
            return False
        if self.compute_begin_date is None or self.compute_end_date is None:
            QMessageBox.critical(self, "Critical", self.tr('没有选择日期'))
            return False
        if self.compute_end_date < self.compute_begin_date:
            QMessageBox.critical(self, "Critical", self.tr('开始日期不能小于结束日期'))
            return False
        return True

    def generate_record_detail_by_car_excel(self):
        results = RecordDetailDbUtils().query_all_records()
        if os.path.exists('逐车明细.xls'):
            QMessageBox.critical(self, "Critical", self.tr('逐车明细文件已经被打开，请删掉后重试'))
            return
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('逐车明细', cell_overwrite_ok=True)
        sheet.write(0, 0, '序号')
        sheet.write(0, 1, '日期')
        sheet.write(0, 2, '客户名称')
        sheet.write(0, 3, '车号')
        sheet.write(0, 4, '煤种')
        sheet.write(0, 5, '单价')
        sheet.write(0, 6, '吨位')
        sheet.write(0, 7, '票种')
        sheet.write(0, 8, '煤款')
        row = 1
        for record in results:
            column = 1
            for item in record:
                sheet.write(row, column, item)
                column += 1
            row += 1
        workbook.save('逐车明细.xls')
