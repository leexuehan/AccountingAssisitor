# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coal.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Coal_Dialog(object):
    def setupUi(self, Coal_Dialog):
        Coal_Dialog.setObjectName("Coal_Dialog")
        Coal_Dialog.resize(583, 290)
        self.ticket_price_label_3 = QtWidgets.QLabel(Coal_Dialog)
        self.ticket_price_label_3.setGeometry(QtCore.QRect(260, 130, 81, 16))
        self.ticket_price_label_3.setObjectName("ticket_price_label_3")
        self.coal_sell_price_content = QtWidgets.QTextEdit(Coal_Dialog)
        self.coal_sell_price_content.setGeometry(QtCore.QRect(170, 170, 71, 21))
        self.coal_sell_price_content.setObjectName("coal_sell_price_content")
        self.coal_name_label = QtWidgets.QLabel(Coal_Dialog)
        self.coal_name_label.setGeometry(QtCore.QRect(80, 90, 91, 16))
        self.coal_name_label.setObjectName("coal_name_label")
        self.coal_name_content = QtWidgets.QTextEdit(Coal_Dialog)
        self.coal_name_content.setGeometry(QtCore.QRect(170, 90, 161, 21))
        self.coal_name_content.setObjectName("coal_name_content")
        self.sell_compute_way = QtWidgets.QComboBox(Coal_Dialog)
        self.sell_compute_way.setGeometry(QtCore.QRect(380, 170, 69, 22))
        self.sell_compute_way.setObjectName("sell_compute_way")
        self.purchase_compute_way = QtWidgets.QComboBox(Coal_Dialog)
        self.purchase_compute_way.setGeometry(QtCore.QRect(380, 130, 69, 22))
        self.purchase_compute_way.setObjectName("purchase_compute_way")
        self.ticket_price_label_4 = QtWidgets.QLabel(Coal_Dialog)
        self.ticket_price_label_4.setGeometry(QtCore.QRect(260, 170, 81, 16))
        self.ticket_price_label_4.setObjectName("ticket_price_label_4")
        self.select_date_btn = QtWidgets.QPushButton(Coal_Dialog)
        self.select_date_btn.setGeometry(QtCore.QRect(74, 50, 81, 23))
        self.select_date_btn.setObjectName("select_date_btn")
        self.coal_purchase_price_content = QtWidgets.QTextEdit(Coal_Dialog)
        self.coal_purchase_price_content.setGeometry(QtCore.QRect(170, 130, 71, 21))
        self.coal_purchase_price_content.setObjectName("coal_purchase_price_content")
        self.ticket_price_label = QtWidgets.QLabel(Coal_Dialog)
        self.ticket_price_label.setGeometry(QtCore.QRect(80, 130, 91, 16))
        self.ticket_price_label.setObjectName("ticket_price_label")
        self.ticket_price_label_2 = QtWidgets.QLabel(Coal_Dialog)
        self.ticket_price_label_2.setGeometry(QtCore.QRect(80, 170, 91, 16))
        self.ticket_price_label_2.setObjectName("ticket_price_label_2")
        self.date_value_display = QtWidgets.QPlainTextEdit(Coal_Dialog)
        self.date_value_display.setGeometry(QtCore.QRect(170, 50, 161, 21))
        self.date_value_display.setObjectName("date_value_display")
        self.confirm = QtWidgets.QPushButton(Coal_Dialog)
        self.confirm.setGeometry(QtCore.QRect(260, 250, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Coal_Dialog)
        self.cancel.setGeometry(QtCore.QRect(380, 250, 75, 23))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Coal_Dialog)
        self.purchase_compute_way.currentIndexChanged['int'].connect(Coal_Dialog.on_purchase_compute_way_selected)
        self.sell_compute_way.currentIndexChanged['int'].connect(Coal_Dialog.on_sell_compute_way_selected)
        self.select_date_btn.clicked.connect(Coal_Dialog.on_add_new_coal_date_selected)
        self.confirm.clicked.connect(Coal_Dialog.add_new_coal)
        self.cancel.clicked.connect(Coal_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Coal_Dialog)

    def retranslateUi(self, Coal_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Coal_Dialog.setWindowTitle(_translate("Coal_Dialog", "Dialog"))
        self.ticket_price_label_3.setText(_translate("Coal_Dialog", "选择计价方式"))
        self.coal_name_label.setText(_translate("Coal_Dialog", "输入煤种名称"))
        self.ticket_price_label_4.setText(_translate("Coal_Dialog", "选择计价方式"))
        self.select_date_btn.setText(_translate("Coal_Dialog", "选择添加日期"))
        self.ticket_price_label.setText(_translate("Coal_Dialog", "输入煤种进价"))
        self.ticket_price_label_2.setText(_translate("Coal_Dialog", "输入煤种售价"))
        self.confirm.setText(_translate("Coal_Dialog", "确定"))
        self.cancel.setText(_translate("Coal_Dialog", "取消"))

