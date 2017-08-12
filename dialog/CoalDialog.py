# -*- coding: utf-8 -*-

import logging

from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.calendarDialog import CalendarDialog
from ui.coal import Ui_Coal_Dialog
from utils.SqlUtils import SqlUtils


class CoalDialog(QDialog):
    def __init__(self, parent=None):
        super(CoalDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Coal_Dialog()
        self.ui.setupUi(self)

        # init compute ways
        self.load_compute_ways()

    # 用此句柄来通知主界面相关内容更新
    def set_main_window_handler(self, main_window_handler):
        self.main_window_handler = main_window_handler

    def load_compute_ways(self):
        self.ui.purchase_compute_way.clear()
        self.compute_ways = ['元/吨', '元/车']
        self.ui.purchase_compute_way.addItems(self.compute_ways)
        self.ui.sell_compute_way.addItems(self.compute_ways)

    def on_purchase_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.purchase_price_compute_way_selected = compute_way

    def on_sell_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.sell_price_compute_way_selected = compute_way

    def on_add_new_coal_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_display.setPlainText(date.strftime('%Y/%m/%d'))
            self.coal_add_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def add_new_coal(self):
        coal_name = self.ui.coal_name_content.toPlainText()
        coal_purchase_price = self.ui.coal_purchase_price_content.toPlainText()
        coal_sell_price = self.ui.coal_sell_price_content.toPlainText()
        logging.info("添加日期:" + str(self.coal_add_date))
        logging.info("煤种名称:" + coal_name)
        logging.info("进价:" + coal_purchase_price)
        logging.info("进价计费方式:" + self.purchase_price_compute_way_selected)
        logging.info("售价:" + coal_sell_price)
        logging.info("售价计费方式:" + self.sell_price_compute_way_selected)
        handler = self.main_window_handler
        coal_name_set = handler.coal_sorts
        if coal_name in coal_name_set:
            QMessageBox.information(self, 'already add', '您已经添加过该煤种', QMessageBox.Yes)
        else:
            utils = SqlUtils()
            utils.add_coal_record(str(self.coal_add_date), coal_name, coal_purchase_price,
                                  self.purchase_price_compute_way_selected, coal_sell_price,
                                  self.sell_price_compute_way_selected)
            handler.coal_sorts.append(coal_name)
            handler.refresh_coal_sorts_combox()
            QMessageBox.information(self, 'add success', '添加煤种成功', QMessageBox.Yes)
        self.accept()
