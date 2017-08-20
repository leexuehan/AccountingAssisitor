# -*- coding: utf-8 -*-
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.ticket_sort_manage import Ui_Ticket_Sort_Manage
from utils.sql.TickeDbtUtils import TicketDbUtils


class TicketSortDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketSortDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Ticket_Sort_Manage()
        self.ui.setupUi(self)

        # init compute ways
        self.load_compute_ways()
        # init list view
        self.model = QStandardItemModel()
        # init vars
        self.ticket_add_date = None

    # 用此句柄来通知主界面相关内容更新
    def set_main_window_handler(self, main_window_handler):
        self.main_window_handler = main_window_handler

    def load_compute_ways(self):
        self.ui.purchase_compute_way.clear()
        self.compute_ways = ['元/吨', '元/车']
        self.ui.purchase_compute_way.addItems(self.compute_ways)
        self.ui.sell_compute_way.addItems(self.compute_ways)

    def on_purchase_price_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.purchase_price_compute_way_selected = compute_way

    def on_sell_price_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.sell_price_compute_way_selected = compute_way

    def on_ticket_add_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.select_date.setText(date.strftime('%Y/%m/%d'))
            self.ticket_add_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_ok(self):
        handler = self.main_window_handler
        ticket_info = self.valid_params(handler)
        if ticket_info is False:
            return
        add_ticket_info = '添加日期：' + ticket_info[0] + '，票种名称：' + ticket_info[1] + \
                          '，进价：' + ticket_info[2] + '，进价计费方式：' + ticket_info[3] + '，售价：' + ticket_info[4] \
                          + '，售价计费方式：' + ticket_info[5]
        utils = TicketDbUtils()
        utils.add_ticket_record(ticket_info[0], ticket_info[1], ticket_info[2],
                                ticket_info[3], ticket_info[4], ticket_info[5])
        handler.ticket_sorts.append(ticket_info[1])
        handler.refresh_ticket_sorts_combox()
        self.add_item_to_list_view(add_ticket_info)
        QMessageBox.information(self, 'add success', '添加票种成功', QMessageBox.Yes)

    def valid_params(self, main_window_handler):
        date = self.ticket_add_date
        ticket_name = self.ui.ticket_name.text()
        ticket_purchase_price = self.ui.purchase_price.text()
        purchase_compute_way = self.purchase_price_compute_way_selected
        ticket_sell_price = self.ui.sell_price.text()
        sell_compute_way = self.sell_price_compute_way_selected
        if date is None or date is '':
            QMessageBox.critical(self, 'Warning', '没有输入日期', QMessageBox.Yes)
            return False
        if ticket_name is '':
            QMessageBox.critical(self, 'Warning', '没有输入票种名称', QMessageBox.Yes)
            return False
        ticket_name_set = main_window_handler.ticket_sorts
        if ticket_name in ticket_name_set:
            QMessageBox.warning(self, 'already add', '您已经添加过该票种', QMessageBox.Yes)
            return False
        if ticket_purchase_price is '':
            QMessageBox.critical(self, 'Warning', '没有输入票种进价', QMessageBox.Yes)
            return False
        if purchase_compute_way is '':
            QMessageBox.critical(self, 'Warning', '没有选择票种进价计价方式', QMessageBox.Yes)
            return False
        if ticket_sell_price is '':
            QMessageBox.critical(self, 'Warning', '没有输入票种售价', QMessageBox.Yes)
            return False
        if sell_compute_way is '':
            QMessageBox.critical(self, 'Warning', '没有选择票种售价计价方式', QMessageBox.Yes)
            return False
        return (date, ticket_name, ticket_purchase_price, purchase_compute_way, ticket_sell_price, sell_compute_way)

    def add_item_to_list_view(self, info):
        item = QStandardItem()
        item.setText(info)
        item.setEditable(False)
        self.model.appendRow(item)
        self.ui.add_detail_list.setModel(self.model)
