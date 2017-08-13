# -*- coding: utf-8 -*-
import logging

from dialog.AccountDialog import AccountDialog
from dialog.CoalDialog import CoalDialog
from dialog.TicketDialog import TicketDialog
from dialog.CalendarDialog import CalendarDialog
from ui.main_window import Ui_MainWindow
from utils.LogUtils import LogUtils
from utils.SqlUtils import SqlUtils
from utils.VerifyUtils import VerifyUtils

__author__ = 'leexuehan@github.com'

import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # init ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # init input params
        self.select_date = None
        self.person_name = None
        self.car_id = None
        self.coal_sorts_selected = None
        self.weight_value = None
        self.ticket_selected = None

        # init comboBox
        self.coal_sorts = []
        self.init_coal_sorts_from_db()
        self.ticket_sorts = []
        self.init_ticket_sorts_from_db()

    def check_parmas_valid(self):
        utils = VerifyUtils()
        if utils.verify_input(self.select_date, "输入日期没有选择!") is False:
            return False
        if utils.verify_input(self.person_name, "没有输入人名") is False:
            return False
        if utils.verify_input(self.car_id, "没有输入车牌号") is False:
            return False
        if utils.verify_input(self.coal_sorts_selected, "没有选择煤种") is False:
            return False
        if utils.verify_input(self.weight_value, "没有输入吨位") is False:
            return False
        if utils.verify_input(self.ticket_selected, "没有选择票种") is False:
            return False
        else:
            return True

    def refresh_coal_sorts_combox(self):
        self.ui.coal_sorts.clear()
        self.ui.coal_sorts.addItems(self.coal_sorts)

    def init_coal_sorts_from_db(self):
        self.ui.coal_sorts.clear()
        utils = SqlUtils()
        try:
            coal_list = utils.query_all_coal_names()
        except:
            logging.warning("there is no coal in db")
            coal_list = []
        for coal in coal_list:
            self.coal_sorts.append(coal[0])
        'default coal sorts is the first'
        if len(coal_list) is not 0:
            self.coal_sorts_selected = coal_list[0][0]
        self.ui.coal_sorts.addItems(self.coal_sorts)

    def refresh_ticket_sorts_combox(self):
        self.ui.ticket_sorts.clear()
        self.ui.ticket_sorts.addItems(self.ticket_sorts)

    def init_ticket_sorts_from_db(self):
        self.ui.ticket_sorts.clear()
        utils = SqlUtils()
        try:
            ticket_list = utils.query_all_tickets_name()
        except:
            logging.warning("there is no ticket sort in db")
            ticket_list = []
        for ticket in ticket_list:
            self.ticket_sorts.append(ticket[0])
        self.ui.ticket_sorts.addItems(self.ticket_sorts)

    def onCoalSortSelected(self, item):
        # 获得条目
        coalSorts = self.coal_sorts[item]
        self.coal_sorts_selected = coalSorts
        query_result = SqlUtils().query_coal_sell_price_by_name(coalSorts)
        price_info = str(query_result[0][0]) + str(query_result[0][1])
        self.ui.coal_sort_sell_price.setText(price_info)

    def on_ticket_selected(self, item):
        ticket_name = self.ticket_sorts[item]
        self.ticket_selected = ticket_name

    # 添加记录“逐车明细”
    def on_record_add(self):
        logging.info("ready to add record to db")
        # 校验输入是否完整
        if self.check_parmas_valid() is False:
            return
        # 数据库存一份，excel 存一份
        SqlUtils().add_record_by_car_detail(self.select_date, self.person_name, self.car_id,
                                            self.coal_sorts_selected,
                                            self.weight_value, self.ticket_selected)
        QMessageBox.information(self, 'Success', '添加成功!', QMessageBox.Yes)

    def on_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_content.setText(date.strftime('%Y/%m/%d'))
            self.select_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_name_input(self):
        print("input name is", self.ui.usernmae_content.text())
        self.person_name = self.ui.usernmae_content.text()

    def on_input_car_id(self):
        print("input car id is", self.ui.car_id_content.text())
        self.car_id = self.ui.car_id_content.text()

    def on_weight_value_input(self):
        print("input weight value is", self.ui.weight_value.text())
        self.weight_value = self.ui.weight_value.text()

    def exit(self):
        sys.exit(0)

    # menu actions below
    def on_compute_account(self):
        accountDialog = AccountDialog()
        accountDialog.show()
        accountDialog.exec_()

    def invokeHelp(self):
        QMessageBox.information(self, 'invoke help', '帮助内容', QMessageBox.Yes)

    def on_add_new_ticket(self):
        ticketDialog = TicketDialog()
        ticketDialog.set_main_window_handler(self)
        ticketDialog.show()
        ticketDialog.exec_()

    def on_add_new_coal(self):
        coalDialog = CoalDialog()
        coalDialog.set_main_window_handler(self)
        coalDialog.show()
        coalDialog.exec_()


if __name__ == '__main__':
    LogUtils.init_logger()
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())