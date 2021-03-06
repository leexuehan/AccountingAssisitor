# -*- coding: utf-8 -*-
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.coal_price_manage import Ui_CoalPrice
from utils.sql.CoalDbUitls import CoalDbUtils


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
        self.compute_ways = ['元/吨', '元/车']
        self.coal_sorts = []
        self.coal_sorts_selected = None
        self.init_coal_sorts_from_db()
        self.init_compute_unit()

        # init list view
        self.model = QStandardItemModel()

        # init value of var
        self.change_purchase_price = False
        self.change_sell_price = False
        self.coal_price_change_date = None
        self.new_purchase_price = None
        self.new_sell_price = None

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

    def on_coal_sort_selected(self, item):
        # 获得条目
        coalSorts = self.coal_sorts[item]
        self.coal_sorts_selected = coalSorts
        self.refresh_coal_information_from_db(coalSorts)

    def refresh_coal_information_from_db(self, coalSorts):
        utils = CoalDbUtils()
        self.latest_price_info = utils.query_coal_latest_price_info_by_name(coalSorts)
        self.latest_date = str(self.latest_price_info[0][0])
        sell_price = str(self.latest_price_info[0][1]) + str(self.latest_price_info[0][2])
        self.coal_sell_price = sell_price
        self.coal_purchase_price = str(self.latest_price_info[0][3]) + str(self.latest_price_info[0][4])
        self.ui.coal_sell_price_display.setText(self.coal_sell_price)
        self.ui.coal_purchase_price_display.setText(self.coal_purchase_price)

    def init_compute_unit(self):
        self.ui.purchase_compute_unit.clear()
        self.ui.sell_compute_unit.clear()
        self.ui.purchase_compute_unit.addItems(self.compute_ways)
        self.ui.sell_compute_unit.addItems(self.compute_ways)

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
        calendarDialog.setModal(True)
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
            self.change_purchase_price = True
        else:
            self.hide_purchase_price_related()
            self.change_purchase_price = False

    def on_sell_price_check_box_selected(self, state):
        if state == Qt.Checked:
            self.show_sell_price_related()
            self.change_sell_price = True
        else:
            self.hide_sell_price_related()
            self.change_sell_price = False

    def input_purchase_price(self):
        print("new_purchase_price is", self.ui.purchase_price_input.text())
        self.new_purchase_price = self.ui.purchase_price_input.text()

    def input_sell_price(self):
        print("new_sell_price is", self.ui.sell_price_input.text())
        self.new_sell_price = self.ui.sell_price_input.text()

    def on_purchase_compute_way_selected(self, item):
        self.purchase_compute_way_selected = self.compute_ways[item]

    def on_sell_compute_way_selected(self, item):
        self.sell_compute_way_selected = self.compute_ways[item]

    def update_price(self):
        new_coal_price_info = self.valid_and_get_new_coal_price_information()
        if new_coal_price_info is False:
            return
        info = "更改日期：%s,更改煤种：%s,进价：%s,计价方式：%s,售价：%s,计价方式：%s" % (
            new_coal_price_info[0], new_coal_price_info[1], new_coal_price_info[2], new_coal_price_info[3],
            new_coal_price_info[4], new_coal_price_info[5])
        print("" + info)
        CoalDbUtils().add_coal_record(new_coal_price_info[0], new_coal_price_info[1], new_coal_price_info[2],
                                      new_coal_price_info[3], new_coal_price_info[4], new_coal_price_info[5])
        self.refresh_coal_information_from_db(self.coal_sorts_selected)
        self.add_item_to_list_view(info)
        QMessageBox.information(self, 'Success', '更改成功!', QMessageBox.Yes)

    def add_item_to_list_view(self, info):
        item = QStandardItem()
        item.setText(info)
        item.setEditable(False)
        self.model.appendRow(item)
        self.ui.modify_detail_list.setModel(self.model)

    def valid_date(self, date):
        if date is None:
            QMessageBox.critical(self, 'Warning', '没有选择日期', QMessageBox.Yes)
            return False
        if self.latest_date >= date:
            QMessageBox.critical(self, 'Warning', '只能更改' + self.latest_date + '之后的价格', QMessageBox.Yes)
            return False

    def valid_and_get_new_coal_price_information(self):
        # valid params
        date = self.coal_price_change_date
        if self.valid_date(date) is False:
            return False
        if self.coal_sorts_selected is None:
            QMessageBox.critical(self, 'Warning', '没有选择煤种', QMessageBox.Yes)
            return False
        if self.change_sell_price is False and self.change_purchase_price is False:
            QMessageBox.critical(self, 'Warning', '没有更改进价和售价', QMessageBox.Yes)
            return False

        # if price not changed then use latest price in db
        if self.change_purchase_price is True:
            if self.new_purchase_price is None or self.new_purchase_price is '':
                QMessageBox.critical(self, 'Warning', '请输入新的进价', QMessageBox.Yes)
                return False
            new_purchase_price = self.new_purchase_price
            new_purchase_compute_way = self.purchase_compute_way_selected
        else:
            new_purchase_price = self.latest_price_info[0][3]
            new_purchase_compute_way = self.latest_price_info[0][4]

        if self.change_sell_price is True:
            if self.new_sell_price is None or self.new_sell_price is '':
                QMessageBox.critical(self, 'Warning', '请输入新的售价', QMessageBox.Yes)
                return False
            new_sell_price = self.new_sell_price
            new_sell_compute_way = self.sell_compute_way_selected
        else:
            new_sell_price = self.latest_price_info[0][1]
            new_sell_compute_way = self.latest_price_info[0][2]
        selected = self.coal_sorts_selected
        return (date, selected, new_purchase_price, new_purchase_compute_way, new_sell_price, new_sell_compute_way)
