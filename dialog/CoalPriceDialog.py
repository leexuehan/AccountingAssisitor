# -*- coding: utf-8 -*-
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from dialog.CalendarDialog import CalendarDialog
from ui.coal_price_manage import Ui_CoalPrice
from utils.sql.SqlUtils import SqlUtils


class CoalPriceDialog(QDialog):
    def __init__(self, parent=None):
        super(CoalPriceDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_CoalPrice()
        self.ui.setupUi(self)

        # init hide component
        self.hide_sell_price_related()
        self.hide_purchase_price_related()

        # init combox
        self.coal_sorts = []
        self.coal_sorts_selected = None
        self.init_coal_sorts_from_db()
        self.init_compute_unit()


        # init value of var

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

    def on_coal_sort_selected(self, item):
        # 获得条目
        coalSorts = self.coal_sorts[item]
        self.coal_sorts_selected = coalSorts
        utils = SqlUtils()
        query_sell_price_result = utils.query_coal_sell_price_by_name(coalSorts)
        query_purchase_price_result = utils.query_coal_purchase_price_by_name(coalSorts)
        sell_price = str(query_sell_price_result[0][0]) + str(query_sell_price_result[0][1])
        purchase_price = str(query_purchase_price_result[0][0]) + str(query_purchase_price_result[0][1])
        self.coal_sell_price = sell_price
        self.coal_purchase_price = purchase_price
        self.ui.coal_sell_price_display.setText(self.coal_sell_price)
        self.ui.coal_purchase_price_display.setText(self.coal_purchase_price)

    def init_compute_unit(self):
        compute_ways = ['元/吨', '元/车']
        self.ui.purchase_compute_unit.clear()
        self.ui.sell_compute_unit.clear()
        self.ui.purchase_compute_unit.addItems(compute_ways)
        self.ui.sell_compute_unit.addItems(compute_ways)

    def hide_purchase_price_related(self):
        self.ui.coal_purchase_price_display.hide()
        self.ui.purchase_price_input.hide()
        self.ui.purchase_compute_unit.hide()
        self.ui.purchase_price_change_label.hide()
        self.ui.coal_purchase_price_label.hide()

    def hide_sell_price_related(self):
        self.ui.coal_sell_price_display.hide()
        self.ui.sell_price_input.hide()
        self.ui.sell_compute_unit.hide()
        self.ui.coal_sell_price_label.hide()
        self.ui.sell_price_change_label.hide()

    def show_sell_price_related(self):
        self.ui.coal_sell_price_display.setVisible(True)
        self.ui.coal_sell_price_display.setText(self.coal_sell_price)
        self.ui.sell_price_input.setVisible(True)
        self.ui.sell_compute_unit.setVisible(True)
        self.ui.coal_sell_price_label.setVisible(True)
        self.ui.sell_price_change_label.setVisible(True)

    def show_purchase_price_related(self):
        self.ui.coal_purchase_price_display.setVisible(True)
        self.ui.coal_purchase_price_display.setText(self.coal_purchase_price)
        self.ui.purchase_price_input.setVisible(True)
        self.ui.purchase_compute_unit.setVisible(True)
        self.ui.purchase_price_change_label.setVisible(True)
        self.ui.coal_purchase_price_label.setVisible(True)

    def open_calendar(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_content.setText(date.strftime('%Y/%m/%d'))
            self.coal_price_change_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_purchase_price_check_box_selected(self, state):
        if state == Qt.Checked:
            self.show_purchase_price_related()
        else:
            self.hide_purchase_price_related()

    def on_sell_price_check_box_selected(self, state):
        if state == Qt.Checked:
            self.show_sell_price_related()
        else:
            self.hide_sell_price_related()
