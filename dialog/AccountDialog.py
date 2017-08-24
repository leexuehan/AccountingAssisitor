import os

import xlwt
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.account_results import Ui_Account_Dialog
from utils.account.AccurateAccountingStrategy import AccurateAccountingStrategy
from utils.account.RoughAccountingStrategy import RoughAccountingStrategy
from utils.excel.ExcelOps import ExcelOps
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

        # init vars MUST PUT BEFORE init combox
        self.selected_name = None
        self.count_small_change = True
        self.compute_begin_date = None
        self.compute_end_date = None

        # init combox
        self.model = QStandardItemModel()
        self.load_all_persons()

        # init account choices
        self.accounting_by_every_car_record = False
        self.accounting_by_coal = False
        self.accounting_by_car = False
        self.accounting_by_person = False
        self.accounting_by_ticket = False

    def show_person_combox(self, state):
        if state == Qt.Checked:
            self.accounting_by_every_car_record = True
        else:
            self.accounting_by_every_car_record = False

    def accounting_by_every_car_record_selected(self, state):
        if state == Qt.Checked:
            self.make_account_by_person = True
        else:
            self.make_account_by_person = False

    def accounting_by_person_selected(self, state):
        if state == Qt.Checked:
            self.accounting_by_person = True
            self.ui.people_names.setVisible(True)
        else:
            self.accounting_by_person = False
            self.ui.people_names.hide()

    def accounting_by_coal_selected(self, state):
        if state == Qt.Checked:
            self.accounting_by_coal = True
        else:
            self.accounting_by_coal = False

    def accounting_by_car_selected(self, state):
        if state == Qt.Checked:
            self.accounting_by_car = True
        else:
            self.accounting_by_car = False

    def accounting_by_ticket_selected(self, state):
        if state == Qt.Checked:
            self.accounting_by_ticket = True
        else:
            self.accounting_by_ticket = False

    def on_select_begin_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            self.compute_begin_date = date
            self.ui.start_date_display.setText(date.strftime('%Y/%m/%d'))
        calendarDialog.destroy()

    def on_select_end_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            self.compute_end_date = date
            self.ui.end_date_display.setText(date.strftime('%Y/%m/%d'))
        calendarDialog.destroy()

    def on_person_name_select_finished(self, item):
        if len(self.people_names_collection) is not 0:
            self.selected_name = self.people_names_collection[item]
            print("selected name is: " + self.selected_name)

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
        results = RecordDetailDbUtils().query_all_records()
        ExcelOps().generate_record_detail_by_car_excel(results, self.compute_begin_date, self.compute_end_date)
        self.progress_bar()
        QMessageBox.information(self, "Success", self.tr('出账已完成'))

    def progress_bar(self):
        self.ui.progressBar.setVisible(True)
        for val in range(0, 100):
            QThread.msleep(10)
            self.ui.progressBar.setValue(val)
        self.ui.progressBar.hide()

    def load_all_persons(self):
        result = RecordDetailDbUtils().query_all_person_names()
        self.people_names_collection = []
        for name in result:
            self.people_names_collection.append(name[0])
        self.ui.people_names.addItems(self.people_names_collection)

    def valid_params(self):
        if self.accounting_by_person is True and self.selected_name is None:
            QMessageBox.critical(self, "Critical", self.tr('没有选择人名'))
            return False
        if self.compute_begin_date is None or self.compute_end_date is None:
            QMessageBox.critical(self, "Critical", self.tr('没有选择日期'))
            return False
        if self.compute_end_date < self.compute_begin_date:
            QMessageBox.critical(self, "Critical", self.tr('开始日期不能大于结束日期'))
            return False
        return True

    def get_accounting_choices(self):
        pass
