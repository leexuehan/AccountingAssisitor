import logging

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.ticket_price_manage import Ui_Ticket_Price
from utils.sql.TickeDbtUtils import TicketDbUtils


class TicketPriceDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketPriceDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Ticket_Price()
        self.ui.setupUi(self)

        # init hide component
        self.hide_sell_price_related()
        self.hide_purchase_price_related()

        # init combox
        self.compute_ways = ['元/吨', '元/车']
        self.ticket_sorts = []
        self.ticket_sorts_selected = None
        self.init_ticket_sorts_from_db()
        self.init_compute_unit()

        # init list view
        self.model = QStandardItemModel()

        # init value of var
        self.ticket_price_change_date = None
        self.change_purchase_price = False
        self.change_sell_price = False
        self.new_purchase_price = None
        self.new_sell_price = None

    def hide_sell_price_related(self):
        self.ui.ticket_sell_price_display.hide()
        self.ui.input_new_sellprice_label.hide()
        self.ui.sell_price_input.hide()
        self.ui.sell_compute_unit.hide()
        self.ui.sell_unit_label.hide()

    def hide_purchase_price_related(self):
        self.ui.ticket_purchase_price_display.hide()
        self.ui.input_new_purchase_price_label.hide()
        self.ui.purchase_price_input.hide()
        self.ui.purchase_compute_unit.hide()
        self.ui.purchase_unit_label.hide()

    def show_sell_price_related(self):
        self.ui.ticket_sell_price_display.setVisible(True)
        self.ui.ticket_sell_price_display.setText(self.ticket_sell_price)
        self.ui.input_new_sellprice_label.setVisible(True)
        self.ui.sell_price_input.setVisible(True)
        self.ui.sell_compute_unit.setVisible(True)
        self.ui.sell_unit_label.setVisible(True)

    def show_purchase_price_related(self):
        self.ui.ticket_purchase_price_display.setVisible(True)
        self.ui.ticket_purchase_price_display.setText(self.ticket_purchase_price)
        self.ui.purchase_price_input.setVisible(True)
        self.ui.purchase_compute_unit.setVisible(True)
        self.ui.input_new_purchase_price_label.setVisible(True)

    def init_ticket_sorts_from_db(self):
        self.ui.ticket_sorts.clear()
        utils = TicketDbUtils()
        try:
            ticket_list = utils.query_all_tickets_name()
        except:
            logging.warning("there is no ticket in db")
            ticket_list = []
        for ticket in ticket_list:
            self.ticket_sorts.append(ticket[0])
        'default ticket sorts is the first'
        if len(ticket_list) is not 0:
            self.ticket_sorts_selected = ticket_list[0][0]
        self.ui.ticket_sorts.addItems(self.ticket_sorts)

    def init_compute_unit(self):
        self.ui.purchase_compute_unit.clear()
        self.ui.sell_compute_unit.clear()
        self.ui.purchase_compute_unit.addItems(self.compute_ways)
        self.ui.sell_compute_unit.addItems(self.compute_ways)

    def select_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.setModal(True)
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_content.setText(date.strftime('%Y/%m/%d'))
            self.ticket_price_change_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def select_ticket_sort(self, item):
        # 获得条目
        ticket_sort = self.ticket_sorts[item]
        self.ticket_sorts_selected = ticket_sort
        self.refresh_ticket_information_from_db(ticket_sort)

    def refresh_ticket_information_from_db(self, ticket_sort):
        utils = TicketDbUtils()
        self.latest_price_info = utils.query_latest_price_info_by_name(ticket_sort)
        self.latest_date = str(self.latest_price_info[0][0])
        sell_price = str(self.latest_price_info[0][1]) + str(self.latest_price_info[0][2])
        self.ticket_sell_price = sell_price
        self.ticket_purchase_price = str(self.latest_price_info[0][3]) + str(self.latest_price_info[0][4])
        self.ui.ticket_sell_price_display.setText(self.ticket_sell_price)
        self.ui.ticket_purchase_price_display.setText(self.ticket_purchase_price)

    def select_modify_purchase_price(self, state):
        if state == Qt.Checked:
            self.show_purchase_price_related()
            self.change_purchase_price = True
        else:
            self.hide_purchase_price_related()
            self.change_purchase_price = False

    def select_modify_sell_price(self, state):
        if state == Qt.Checked:
            self.show_sell_price_related()
            self.change_sell_price = True
        else:
            self.hide_sell_price_related()
            self.change_sell_price = False

    def input_new_purchase_price(self):
        print("new_purchase_price is", self.ui.purchase_price_input.text())
        self.new_purchase_price = self.ui.purchase_price_input.text()

    def select_purchase_compute_unit(self, item):
        self.purchase_compute_way_selected = self.compute_ways[item]

    def input_new_sell_price(self):
        print("new_sell_price is", self.ui.sell_price_input.text())
        self.new_sell_price = self.ui.sell_price_input.text()

    def select_sell_compute_unit(self, item):
        self.sell_compute_way_selected = self.compute_ways[item]

    def confirm_update(self):
        new_ticket_price_info = self.valid_and_get_new_ticket_price_information()
        if new_ticket_price_info is False:
            return
        info = "更改日期：%s,更改煤种：%s,进价：%s,计价方式：%s,售价：%s,计价方式：%s" % (
            new_ticket_price_info[0], new_ticket_price_info[1], new_ticket_price_info[2], new_ticket_price_info[3],
            new_ticket_price_info[4], new_ticket_price_info[5])
        print("" + info)
        TicketDbUtils().add_ticket_record(new_ticket_price_info[0], new_ticket_price_info[1], new_ticket_price_info[2],
                                          new_ticket_price_info[3], new_ticket_price_info[4], new_ticket_price_info[5])
        self.refresh_ticket_information_from_db(self.ticket_sorts_selected)
        self.add_item_to_list_view(info)
        QMessageBox.information(self, 'Success', '更改成功!', QMessageBox.Yes)

    def valid_and_get_new_ticket_price_information(self):
        # valid params
        date = self.ticket_price_change_date
        if self.valid_date(date) is False:
            return False
        if self.ticket_sorts_selected is None:
            QMessageBox.critical(self, 'Warning', '没有选择票种', QMessageBox.Yes)
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
        selected = self.ticket_sorts_selected
        return (date, selected, new_purchase_price, new_purchase_compute_way, new_sell_price, new_sell_compute_way)

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
