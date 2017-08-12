# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.calendarDialog import CalendarDialog
from ui.ticket import Ui_Ticket_Dialog
from utils.SqlUtils import SqlUtils


class TicketDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Ticket_Dialog()
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

    def on_purchase_price_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.purchase_price_compute_way_selected = compute_way

    def on_sell_price_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.sell_price_compute_way_selected = compute_way

    def on_ticket_add_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_display.setPlainText(date.strftime('%Y/%m/%d'))
            self.ticket_add_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_ok(self):
        ticket_name = self.ui.ticket_name_content.toPlainText()
        ticket_purchase_price = self.ui.ticket_purchase_price_content.toPlainText()
        ticket_sell_price = self.ui.ticket_sell_price_content.toPlainText()
        print("add new ticket info (添加日期，票名，进价，进价计费方式，售价，售价计费方式):",
              (self.ticket_add_date, ticket_name, ticket_purchase_price, self.purchase_price_compute_way_selected
               , ticket_sell_price, self.sell_price_compute_way_selected))
        handler = self.main_window_handler
        ticket_name_set = handler.ticket_sorts
        # todo 检验输入是否缺少
        if ticket_name in ticket_name_set:
            QMessageBox.information(self, 'already add', '您已经添加过该票种', QMessageBox.Yes)
        else:
            utils = SqlUtils()
            utils.add_ticket_record(self.ticket_add_date, ticket_name, ticket_purchase_price,
                                    self.purchase_price_compute_way_selected, ticket_sell_price,
                                    self.sell_price_compute_way_selected)
            handler.ticket_sorts.append(ticket_name)
            handler.refresh_ticket_sorts_combox()
            QMessageBox.information(self, 'add success', '添加票种成功', QMessageBox.Yes)
        self.accept()
