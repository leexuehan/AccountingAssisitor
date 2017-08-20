# -*- coding: utf-8 -*-

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.coal_sort_manage import Ui_Coal_Sort_Manage
from utils.sql.CoalDbUitls import CoalDbUtils


class CoalSortDialog(QDialog):
    def __init__(self, parent=None):
        super(CoalSortDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Coal_Sort_Manage()
        self.ui.setupUi(self)

        # init compute ways
        self.load_compute_ways()
        # init list view
        self.model = QStandardItemModel()
        # init var values
        self.coal_add_date = None

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
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_content.setText(date.strftime('%Y/%m/%d'))
            self.coal_add_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def add_new_coal(self):
        coal_name = self.ui.coal_sort_name.text()
        coal_purchase_price = self.ui.purchase_price.text()
        coal_sell_price = self.ui.sell_price.text()
        add_info = "添加日期:" + str(self.coal_add_date) + \
                   "煤种名称:" + coal_name + "进价:" + coal_purchase_price + "进价计费方式:" + \
                   self.purchase_price_compute_way_selected + "售价:" + coal_sell_price \
                   + "售价计费方式:" + self.sell_price_compute_way_selected
        handler = self.main_window_handler
        coal_name_set = handler.coal_sorts
        if coal_name in coal_name_set:
            QMessageBox.warning(self, 'Warning', '您已经添加过该煤种', QMessageBox.Yes)
            return
        else:
            if self.valid_params(self.coal_add_date, coal_name, coal_purchase_price,
                                 self.purchase_price_compute_way_selected,
                                 coal_sell_price, self.sell_price_compute_way_selected) is False:
                return
            utils = CoalDbUtils()
            utils.add_coal_record(str(self.coal_add_date), coal_name, coal_purchase_price,
                                  self.purchase_price_compute_way_selected, coal_sell_price,
                                  self.sell_price_compute_way_selected)
            handler.coal_sorts.append(coal_name)
            handler.refresh_coal_sorts_combox()
            self.add_item_to_list_view(add_info)
            QMessageBox.information(self, 'success', '添加煤种成功', QMessageBox.Yes)

    def valid_params(self, date, coal_name, coal_purchase_price, purchase_price_compute_way_selected,
                     coal_sell_price, sell_price_compute_way_selected):
        if date is None or date is '':
            QMessageBox.critical(self, 'Warning', '没有选择日期', QMessageBox.Yes)
            return False
        if coal_name is None or coal_name is '':
            QMessageBox.critical(self, 'Warning', '没有输入煤种', QMessageBox.Yes)
            return False
        if coal_purchase_price is None or coal_purchase_price is '':
            QMessageBox.critical(self, 'Warning', '没有输入煤种进价', QMessageBox.Yes)
            return False
        if purchase_price_compute_way_selected is None or '':
            QMessageBox.critical(self, 'Warning', '没有选择进价计价方式', QMessageBox.Yes)
            return False
        if coal_sell_price is None or coal_sell_price is '':
            QMessageBox.critical(self, 'Warning', '没有输入售价', QMessageBox.Yes)
            return False
        if sell_price_compute_way_selected is None or sell_price_compute_way_selected is '':
            QMessageBox.critical(self, 'Warning', '没有选择售价计价方式', QMessageBox.Yes)
            return False
        return True

    def add_item_to_list_view(self, info):
        item = QStandardItem()
        item.setText(info)
        item.setEditable(False)
        self.model.appendRow(item)
        self.ui.modify_detail_list.setModel(self.model)
