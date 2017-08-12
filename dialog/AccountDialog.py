from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from dialog.calendarDialog import CalendarDialog
from ui.account_results import Ui_Account_Dialog


class AccountDialog(QDialog):
    def __init__(self, parent=None):
        super(AccountDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Account_Dialog()
        self.ui.setupUi(self)

        # init list view
        # self.load_all_persons()

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
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.start_date.setPlainText(date.strftime('%Y/%m/%d'))
            self.compute_begin_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_select_end_date(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.end_date.setPlainText(date.strftime('%Y/%m/%d'))
            self.compute_end_date = date.strftime('%Y/%m/%d')
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
            item = QStandardItem(self.selected_name)
            self.__add_item_to_list_view(item)
            # self.person_name = self.ui.person_name.text()

    def delete_person_name_from_list_view(self):
        row_index = self.ui.listView.currentIndex().row()
        if row_index is -1:
            QMessageBox.information(self, '请选择删除项', '请选择删除项', QMessageBox.Yes)
        else:
            name = self.model.itemData(self.ui.listView.currentIndex())[0]
            self.selected_persons.remove(name)
            self.model.removeRow(self.row_index_selected)
        self.ui.listView.reset()  # 重置当前 listview 的游标
        # self.ui.listView.setUpdatesEnabled(True)

    def __add_item_to_list_view(self, item):
        row_count = self.model.rowCount()
        print("already have items num", row_count)
        self.model.appendRow(item)
        self.ui.listView.setModel(self.model)

    def on_start_compute_cmd(self):
        print("begin to compute account......")
        info = str(self.selected_persons) + ',' + str(self.compute_begin_date) + ',' \
               + str(self.compute_end_date)
        print(info)
        self.ui.output_result.setText(info)

    def load_all_persons(self):
        self.people_names_collection = ["erha", "erya", "xxxx"]
        self.ui.people_names.addItems(self.people_names_collection)
        # model = QStandardItemModel(4, 1)
        # model.setHorizontalHeaderLabels(['标题'])
        # for row in range(4):
        #     item = QStandardItem("row %s, column %s" % (row, 0))
        #     model.setItem(row, 0, item)
        # item = QStandardItem("I am new here")
        # model.setItem(4,item)
        # self.ui.listView.setModel(model)
