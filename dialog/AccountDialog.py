from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.account_results import Ui_Account_Dialog
from utils.SqlUtils import SqlUtils
from utils.account.AccurateAccountingStrategy import AccurateAccountingStrategy
from utils.account.RoughAccountingStrategy import RoughAccountingStrategy
from utils.html_model import HTML_MODEL


class AccountDialog(QDialog):
    def __init__(self, parent=None):
        super(AccountDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Account_Dialog()
        self.ui.setupUi(self)

        # init combox
        self.model = QStandardItemModel()
        self.load_all_persons()

        # init collections
        self.selected_persons = []

        # init compute account settings
        self.count_small_change = True

    def on_select_begin_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            format_date_str = date.strftime('%Y/%m/%d')
            print("value get from calendar window is:" + format_date_str)
            self.ui.start_date.setPlainText(format_date_str)
            self.compute_begin_date = format_date_str
            # if 'compute_end_date' in locals().keys() and format_date_str > self.compute_end_date:
            #     QMessageBox.critical(self, "Critical", self.tr('截止日期不能小于起始日期，请重新选择起始日期'))
            #     return
        calendarDialog.destroy()

    def on_select_end_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            format_date_str = date.strftime('%Y/%m/%d')
            print("value get from calendar window is:" + format_date_str)
            if format_date_str < self.compute_begin_date:
                QMessageBox.critical(self, "Critical", self.tr('截止日期不能小于起始日期，请重新选择'))
                return
            self.ui.end_date.setPlainText(format_date_str)
            self.compute_end_date = format_date_str
        calendarDialog.destroy()

    def on_person_name_select_finished(self, item):
        self.selected_name = self.people_names_collection[item]

    def on_person_name_from_list_view_selected(self):
        row_index = self.ui.listView.currentIndex().row()
        print(row_index, "selected!!!!!!!!!!!!!")
        self.row_index_selected = row_index

    def on_add_person(self):
        print("input name is", self.selected_name, "selected persons", self.selected_persons)
        if self.selected_name not in self.selected_persons:
            self.selected_persons.append(self.selected_name)
            item = QStandardItem("添加人名：" + self.selected_name)
            self.__add_item_to_list_view(item)

    def delete_person_name_from_list_view(self):
        row_index = self.ui.listView.currentIndex().row()
        if row_index is -1:
            QMessageBox.critical(self, "Critical", self.tr('请选择删除项'))
        else:
            name = self.model.itemData(self.ui.listView.currentIndex())[0]
            self.selected_persons.remove(name)
            self.model.removeRow(self.row_index_selected)
        self.ui.listView.reset()  # 重置当前 listview 的游标

    def __add_item_to_list_view(self, item):
        row_count = self.model.rowCount()
        print("already have items num", row_count)
        self.model.appendRow(item)
        self.ui.listView.setModel(self.model)

    def count_small_change(self, state):
        if state == Qt.Checked:
            self.count_small_change = False
        else:
            self.count_small_change = True

    'accounting cmd begin....'

    def on_start_compute_cmd(self):
        print("begin to compute account......")
        if self.count_small_change is True:
            strategy = AccurateAccountingStrategy()
        else:
            strategy = RoughAccountingStrategy()
        context = HTML_MODEL['account_result_show']
        account_title = '账目明细(%s~%s)' % (self.compute_begin_date, self.compute_end_date)
        data = ''
        for name in self.selected_persons:
            coal_total_sell_price = strategy.all_coals_sell_perice_by_person(name)
            coal_total_purchase_price = strategy.all_coals_purchase_cost_by_person(name)
            ticket_total_sell_price = strategy.all_ticket_sell_price_by_person(name)
            ticket_total_purchase_price = strategy.all_ticket_purchase_price_by_person(name)
            total_profit = (coal_total_sell_price + ticket_total_sell_price) - (
                coal_total_purchase_price + ticket_total_purchase_price)
            line_data = '<tr><td>' + name + '</td><td>' + str(coal_total_sell_price) + '</td><td>' + str(
                coal_total_purchase_price) \
                        + '</td><td>' + str(ticket_total_sell_price) + '</td><td>' + str(ticket_total_purchase_price) \
                        + '</td><td>' + str(total_profit) + '</td></tr>'
            data += line_data
        context = context % (account_title, data)
        print("context is :\n" + context)
        self.ui.output_result.setHtml(context)

    def load_all_persons(self):
        result = SqlUtils().query_all_person_names()
        self.people_names_collection = []
        for name in result:
            self.people_names_collection.append(name[0])
        self.ui.people_names.addItems(self.people_names_collection)
