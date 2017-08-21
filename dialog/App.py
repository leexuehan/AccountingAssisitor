# -*- coding: utf-8 -*-
import logging

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from dialog.AccountDialog import AccountDialog
from dialog.CalendarDialog import CalendarDialog
from dialog.CoalSortDialog import CoalSortDialog
from dialog.CoalPriceDialog import CoalPriceDialog
from dialog.TicketPriceDialog import TicketPriceDialog
from dialog.TicketSortDialog import TicketSortDialog
from ui.main_window import Ui_MainWindow
from utils.log.LogUtils import LogUtils
from utils.sql.CoalDbUitls import CoalDbUtils
from utils.sql.RecordDetailDbUtils import RecordDetailDbUtils
from utils.sql.SqlUtils import SqlUtils
from utils.sql.TickeDbtUtils import TicketDbUtils

__author__ = 'leexuehan@github.com'

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # init ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set hide components
        self.ui.date_hint.hide()
        self.ui.car_id_hint.hide()
        self.ui.person_name_hint.hide()
        self.ui.coal_sell_price_display.hide()
        self.ui.no_coal_name_selected_hint.hide()
        self.ui.no_ticket_name_selected_hint.hide()
        self.ui.weight_hint.hide()

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

        # init list view
        self.model = QStandardItemModel()

    def check_parmas_valid(self):
        if self.select_date is None:
            self.ui.date_hint.setVisible(True)
            self.ui.date_hint.setStyleSheet('color:red;')
            return False
        else:
            self.ui.date_hint.hide()
        if self.person_name is None or self.person_name is '':
            self.ui.person_name_hint.setVisible(True)
            self.ui.person_name_hint.setStyleSheet('color:red;')
            return False
        else:
            self.ui.person_name_hint.hide()
        if self.car_id is None:
            self.ui.car_id_hint.setVisible(True)
            self.ui.car_id_hint.setStyleSheet('color:red;')
            return False
        else:
            self.ui.car_id_hint.hide()
        if self.weight_value is None or self.weight_value is '':
            self.ui.weight_hint.setVisible(True)
            self.ui.weight_hint.setStyleSheet('color:red;')
            return False
        else:
            self.ui.weight_hint.hide()

        if self.coal_sorts_selected is None:
            self.ui.no_coal_name_selected_hint.setVisible(True)
            self.ui.no_coal_name_selected_hint.setStyleSheet('color:red;')
            return False
        else:
            self.ui.no_coal_name_selected_hint.hide()
        if self.ticket_selected is None:
            self.ui.no_ticket_name_selected_hint.setVisible(True)
            self.ui.no_ticket_name_selected_hint.setStyleSheet('color:red;')
            return False
        else:
            self.ui.no_ticket_name_selected_hint.hide()
        return True

    def refresh_coal_sorts_combox(self):
        self.ui.coal_sorts.clear()
        self.ui.coal_sorts.addItems(self.coal_sorts)

    def init_coal_sorts_from_db(self):
        self.ui.coal_sorts.clear()
        utils = CoalDbUtils()
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
        utils = TicketDbUtils()
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
        query_result = CoalDbUtils().query_coal_latest_price_info_by_name(coalSorts)
        price_info = str(query_result[0][1]) + str(query_result[0][2])
        self.ui.coal_sell_price_display.setVisible(True)
        self.ui.coal_sell_price_display.setText(price_info)

    def on_ticket_selected(self, item):
        ticket_name = self.ticket_sorts[item]
        self.ticket_selected = ticket_name
        query_result = TicketDbUtils().query_latest_price_info_by_name(ticket_name)
        price_info = str(query_result[0][1]) + str(query_result[0][2])
        self.ui.ticket_sell_price_display.setVisible(True)
        self.ui.ticket_sell_price_display.setText(price_info)

    # 添加记录“逐车明细”
    def on_record_add(self):
        logging.info("ready to add record to db")
        # 校验输入是否完整
        if self.check_parmas_valid() is False:
            return
        # 数据库存一份，excel 存一份
        RecordDetailDbUtils().add_record_by_car_detail(self.select_date, self.person_name, self.car_id,
                                                       self.coal_sorts_selected,
                                                       self.weight_value, self.ticket_selected)
        add_info = '添加日期：' + str(self.select_date) + '，客户名称：' + self.person_name + \
                   '，车牌号：' + self.car_id + '，煤种：' + self.coal_sorts_selected \
                   + '，吨位：' + str(self.weight_value) + '，票种：' + self.ticket_selected
        self.add_item_to_list_view(add_info)
        QMessageBox.information(self, 'Success', '添加成功!', QMessageBox.Yes)

    def add_item_to_list_view(self, add_info):
        item = QStandardItem()
        item.setText(add_info)
        item.setEditable(False)
        self.model.appendRow(item)
        self.ui.listView.setModel(self.model)

    def on_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
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
        accountDialog.setModal(True)
        accountDialog.show()
        accountDialog.exec_()

    def invokeHelp(self):
        QMessageBox.information(self, 'invoke help', '帮助内容', QMessageBox.Yes)

    def on_add_new_ticket(self):
        ticketDialog = TicketSortDialog()
        ticketDialog.set_main_window_handler(self)
        ticketDialog.setModal(True)
        ticketDialog.show()
        ticketDialog.exec_()

    def on_add_new_coal(self):
        coalDialog = CoalSortDialog()
        coalDialog.set_main_window_handler(self)
        coalDialog.setModal(True)
        coalDialog.show()
        coalDialog.exec_()

    def open_coal_price_manage_dialog(self):
        coalPriceDialog = CoalPriceDialog()
        coalPriceDialog.setModal(True)
        coalPriceDialog.show()
        coalPriceDialog.exec_()

    def open_ticket_price_manage_dialog(self):
        ticketPriceDialog = TicketPriceDialog()
        ticketPriceDialog.setModal(True)
        ticketPriceDialog.show()
        ticketPriceDialog.exec_()


if __name__ == '__main__':
    LogUtils.init_logger()
    SqlUtils().init_tables()
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
