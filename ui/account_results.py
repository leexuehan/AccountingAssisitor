# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_results.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Account_Dialog(object):
    def setupUi(self, Account_Dialog):
        Account_Dialog.setObjectName("Account_Dialog")
        Account_Dialog.resize(708, 692)
        self.account = QtWidgets.QTabWidget(Account_Dialog)
        self.account.setGeometry(QtCore.QRect(60, 10, 571, 291))
        self.account.setObjectName("account")
        self.ff = QtWidgets.QWidget()
        self.ff.setObjectName("ff")
        self.label_4 = QtWidgets.QLabel(self.ff)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 81, 20))
        self.label_4.setObjectName("label_4")
        self.people_names = QtWidgets.QComboBox(self.ff)
        self.people_names.setGeometry(QtCore.QRect(110, 20, 91, 22))
        self.people_names.setObjectName("people_names")
        self.add_people = QtWidgets.QPushButton(self.ff)
        self.add_people.setGeometry(QtCore.QRect(50, 70, 131, 23))
        self.add_people.setObjectName("add_people")
        self.listView = QtWidgets.QListView(self.ff)
        self.listView.setGeometry(QtCore.QRect(300, 0, 256, 261))
        self.listView.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.ff)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 131, 21))
        self.pushButton.setObjectName("pushButton")
        self.account.addTab(self.ff, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 30, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tableView_2 = QtWidgets.QTableView(self.tab_3)
        self.tableView_2.setGeometry(QtCore.QRect(300, 10, 256, 301))
        self.tableView_2.setObjectName("tableView_2")
        self.account.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.tableView_3 = QtWidgets.QTableView(self.tab)
        self.tableView_3.setGeometry(QtCore.QRect(190, 10, 256, 192))
        self.tableView_3.setObjectName("tableView_3")
        self.account.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.account.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.account.addTab(self.tab_2, "")
        self.return_to_main_window = QtWidgets.QPushButton(Account_Dialog)
        self.return_to_main_window.setGeometry(QtCore.QRect(470, 620, 75, 23))
        self.return_to_main_window.setObjectName("return_to_main_window")
        self.output_result = QtWidgets.QTextBrowser(Account_Dialog)
        self.output_result.setGeometry(QtCore.QRect(355, 310, 281, 261))
        self.output_result.setStyleSheet("\n"
"Header 1\n"
"Header 2\n"
"row 1, cell 1\n"
"row 1, cell 2\n"
"row 2, cell 1\n"
"row 2, cell 2\n"
"")
        self.output_result.setObjectName("output_result")
        self.compute_cmd_btn = QtWidgets.QPushButton(Account_Dialog)
        self.compute_cmd_btn.setGeometry(QtCore.QRect(150, 510, 70, 30))
        self.compute_cmd_btn.setObjectName("compute_cmd_btn")
        self.end_date = QtWidgets.QPlainTextEdit(Account_Dialog)
        self.end_date.setGeometry(QtCore.QRect(150, 480, 181, 21))
        self.end_date.setObjectName("end_date")
        self.select_start_date_btn = QtWidgets.QPushButton(Account_Dialog)
        self.select_start_date_btn.setGeometry(QtCore.QRect(60, 430, 81, 23))
        self.select_start_date_btn.setObjectName("select_start_date_btn")
        self.select_end_date_btn = QtWidgets.QPushButton(Account_Dialog)
        self.select_end_date_btn.setGeometry(QtCore.QRect(60, 480, 81, 23))
        self.select_end_date_btn.setObjectName("select_end_date_btn")
        self.start_date = QtWidgets.QPlainTextEdit(Account_Dialog)
        self.start_date.setGeometry(QtCore.QRect(150, 430, 181, 21))
        self.start_date.setObjectName("start_date")
        self.count_small_change = QtWidgets.QCheckBox(Account_Dialog)
        self.count_small_change.setGeometry(QtCore.QRect(240, 510, 80, 30))
        self.count_small_change.setObjectName("count_small_change")

        self.retranslateUi(Account_Dialog)
        self.account.setCurrentIndex(0)
        self.return_to_main_window.clicked.connect(Account_Dialog.reject)
        self.people_names.currentIndexChanged['int'].connect(Account_Dialog.on_person_name_select_finished)
        self.add_people.clicked.connect(Account_Dialog.on_add_person)
        self.compute_cmd_btn.clicked.connect(Account_Dialog.on_start_compute_cmd)
        self.select_start_date_btn.clicked.connect(Account_Dialog.on_select_begin_date)
        self.select_end_date_btn.clicked.connect(Account_Dialog.on_select_end_date)
        self.listView.clicked['QModelIndex'].connect(Account_Dialog.on_person_name_from_list_view_selected)
        self.pushButton.clicked.connect(Account_Dialog.delete_person_name_from_list_view)
        self.count_small_change.stateChanged['int'].connect(Account_Dialog.count_small_change)
        QtCore.QMetaObject.connectSlotsByName(Account_Dialog)

    def retranslateUi(self, Account_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Account_Dialog.setWindowTitle(_translate("Account_Dialog", "Dialog"))
        self.label_4.setText(_translate("Account_Dialog", "选择客户名称"))
        self.add_people.setText(_translate("Account_Dialog", "添加"))
        self.pushButton.setText(_translate("Account_Dialog", "删除"))
        self.account.setTabText(self.account.indexOf(self.ff), _translate("Account_Dialog", "按人计算"))
        self.tab_3.setWhatsThis(_translate("Account_Dialog", "<html><head/><body><p>ccc</p></body></html>"))
        self.label_5.setText(_translate("Account_Dialog", "选择车牌号"))
        self.account.setTabText(self.account.indexOf(self.tab_3), _translate("Account_Dialog", "按车计算"))
        self.label_3.setText(_translate("Account_Dialog", "选择票种"))
        self.account.setTabText(self.account.indexOf(self.tab), _translate("Account_Dialog", "按票计算"))
        self.account.setTabText(self.account.indexOf(self.tab_4), _translate("Account_Dialog", "按日期计算"))
        self.return_to_main_window.setText(_translate("Account_Dialog", "返回"))
        self.output_result.setHtml(_translate("Account_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Header 1</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Header 2</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">row 1, cell 1</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">row 1, cell 2</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">row 2, cell 1</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">row 2, cell 2</p></td></tr></table></body></html>"))
        self.compute_cmd_btn.setText(_translate("Account_Dialog", "开始计算"))
        self.select_start_date_btn.setText(_translate("Account_Dialog", "选择起始日期"))
        self.select_end_date_btn.setText(_translate("Account_Dialog", "选择截止日期"))
        self.count_small_change.setText(_translate("Account_Dialog", "抹零出账"))

