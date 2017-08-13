from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.CalendarDialog import CalendarDialog
from ui.account_results import Ui_Account_Dialog
from utils.SqlUtils import SqlUtils


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

    'accounting cmd begin....'
    def on_start_compute_cmd(self):
        print("begin to compute account......")
        info = str(self.selected_persons) + ',' + str(self.compute_begin_date) + ',' \
               + str(self.compute_end_date)
        print(info)

        self.ui.output_result.setText(info)

    def load_all_persons(self):
        result = SqlUtils().query_all_person_names()
        self.people_names_collection = []
        for name in result:
            self.people_names_collection.append(name[0])
        self.ui.people_names.addItems(self.people_names_collection)
