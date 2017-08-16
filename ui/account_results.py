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
        Account_Dialog.resize(913, 671)
        self.return_to_main_window = QtWidgets.QPushButton(Account_Dialog)
        self.return_to_main_window.setGeometry(QtCore.QRect(700, 570, 75, 23))
        self.return_to_main_window.setObjectName("return_to_main_window")
        self.compute_cmd_btn = QtWidgets.QPushButton(Account_Dialog)
        self.compute_cmd_btn.setGeometry(QtCore.QRect(350, 330, 70, 30))
        self.compute_cmd_btn.setObjectName("compute_cmd_btn")
        self.end_date = QtWidgets.QPlainTextEdit(Account_Dialog)
        self.end_date.setGeometry(QtCore.QRect(350, 300, 181, 21))
        self.end_date.setObjectName("end_date")
        self.select_start_date_btn = QtWidgets.QPushButton(Account_Dialog)
        self.select_start_date_btn.setGeometry(QtCore.QRect(260, 250, 81, 23))
        self.select_start_date_btn.setObjectName("select_start_date_btn")
        self.select_end_date_btn = QtWidgets.QPushButton(Account_Dialog)
        self.select_end_date_btn.setGeometry(QtCore.QRect(260, 300, 81, 23))
        self.select_end_date_btn.setObjectName("select_end_date_btn")
        self.start_date = QtWidgets.QPlainTextEdit(Account_Dialog)
        self.start_date.setGeometry(QtCore.QRect(350, 250, 181, 21))
        self.start_date.setObjectName("start_date")
        self.count_small_change = QtWidgets.QCheckBox(Account_Dialog)
        self.count_small_change.setGeometry(QtCore.QRect(440, 330, 80, 30))
        self.count_small_change.setObjectName("count_small_change")
        self.groupBox = QtWidgets.QGroupBox(Account_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 120, 821, 80))
        self.groupBox.setObjectName("groupBox")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(480, 30, 111, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 30, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(390, 30, 91, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 30, 91, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.people_names = QtWidgets.QComboBox(self.groupBox)
        self.people_names.setGeometry(QtCore.QRect(120, 30, 91, 22))
        self.people_names.setObjectName("people_names")
        self.listView_2 = QtWidgets.QListView(Account_Dialog)
        self.listView_2.setGeometry(QtCore.QRect(260, 380, 521, 141))
        self.listView_2.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.listView_2.setObjectName("listView_2")

        self.retranslateUi(Account_Dialog)
        self.return_to_main_window.clicked.connect(Account_Dialog.reject)
        self.compute_cmd_btn.clicked.connect(Account_Dialog.on_start_compute_cmd)
        self.select_start_date_btn.clicked.connect(Account_Dialog.on_select_begin_date)
        self.select_end_date_btn.clicked.connect(Account_Dialog.on_select_end_date)
        self.count_small_change.stateChanged['int'].connect(Account_Dialog.count_small_change)
        self.people_names.currentIndexChanged['int'].connect(Account_Dialog.on_person_name_select_finished)
        self.checkBox_5.stateChanged['int'].connect(Account_Dialog.show_person_combox)
        QtCore.QMetaObject.connectSlotsByName(Account_Dialog)

    def retranslateUi(self, Account_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Account_Dialog.setWindowTitle(_translate("Account_Dialog", "Dialog"))
        self.return_to_main_window.setText(_translate("Account_Dialog", "返回"))
        self.compute_cmd_btn.setText(_translate("Account_Dialog", "开始计算"))
        self.select_start_date_btn.setText(_translate("Account_Dialog", "选择起始日期"))
        self.select_end_date_btn.setText(_translate("Account_Dialog", "选择截止日期"))
        self.count_small_change.setText(_translate("Account_Dialog", "抹零出账"))
        self.groupBox.setTitle(_translate("Account_Dialog", "出账选项"))
        self.checkBox_4.setText(_translate("Account_Dialog", "按每日明细出账"))
        self.checkBox_2.setText(_translate("Account_Dialog", "按车出账"))
        self.checkBox_3.setText(_translate("Account_Dialog", "按票种出账"))
        self.checkBox_5.setText(_translate("Account_Dialog", "按客户出账"))

