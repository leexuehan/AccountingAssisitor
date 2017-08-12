# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ticket_Dialog(object):
    def setupUi(self, Ticket_Dialog):
        Ticket_Dialog.setObjectName("Ticket_Dialog")
        Ticket_Dialog.resize(612, 300)
        self.ticket_name_label = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_name_label.setGeometry(QtCore.QRect(80, 110, 91, 16))
        self.ticket_name_label.setObjectName("ticket_name_label")
        self.ticket_name_content = QtWidgets.QTextEdit(Ticket_Dialog)
        self.ticket_name_content.setGeometry(QtCore.QRect(170, 110, 161, 21))
        self.ticket_name_content.setObjectName("ticket_name_content")
        self.ticket_price_label = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_price_label.setGeometry(QtCore.QRect(80, 150, 91, 16))
        self.ticket_price_label.setObjectName("ticket_price_label")
        self.ticket_purchase_price_content = QtWidgets.QTextEdit(Ticket_Dialog)
        self.ticket_purchase_price_content.setGeometry(QtCore.QRect(170, 150, 71, 21))
        self.ticket_purchase_price_content.setObjectName("ticket_purchase_price_content")
        self.confirm = QtWidgets.QPushButton(Ticket_Dialog)
        self.confirm.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Ticket_Dialog)
        self.cancel.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.cancel.setObjectName("cancel")
        self.ticket_price_label_2 = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_price_label_2.setGeometry(QtCore.QRect(80, 190, 91, 16))
        self.ticket_price_label_2.setObjectName("ticket_price_label_2")
        self.ticket_sell_price_content = QtWidgets.QTextEdit(Ticket_Dialog)
        self.ticket_sell_price_content.setGeometry(QtCore.QRect(170, 190, 71, 21))
        self.ticket_sell_price_content.setObjectName("ticket_sell_price_content")
        self.ticket_price_label_3 = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_price_label_3.setGeometry(QtCore.QRect(260, 150, 81, 16))
        self.ticket_price_label_3.setObjectName("ticket_price_label_3")
        self.purchase_compute_way = QtWidgets.QComboBox(Ticket_Dialog)
        self.purchase_compute_way.setGeometry(QtCore.QRect(380, 150, 69, 22))
        self.purchase_compute_way.setObjectName("purchase_compute_way")
        self.ticket_price_label_4 = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_price_label_4.setGeometry(QtCore.QRect(260, 190, 81, 16))
        self.ticket_price_label_4.setObjectName("ticket_price_label_4")
        self.sell_compute_way = QtWidgets.QComboBox(Ticket_Dialog)
        self.sell_compute_way.setGeometry(QtCore.QRect(380, 190, 69, 22))
        self.sell_compute_way.setObjectName("sell_compute_way")
        self.date_value_display = QtWidgets.QPlainTextEdit(Ticket_Dialog)
        self.date_value_display.setGeometry(QtCore.QRect(170, 70, 161, 21))
        self.date_value_display.setObjectName("date_value_display")
        self.select_date_btn = QtWidgets.QPushButton(Ticket_Dialog)
        self.select_date_btn.setGeometry(QtCore.QRect(80, 70, 75, 23))
        self.select_date_btn.setObjectName("select_date_btn")

        self.retranslateUi(Ticket_Dialog)
        self.cancel.clicked.connect(Ticket_Dialog.reject)
        self.confirm.clicked.connect(Ticket_Dialog.on_ok)
        self.purchase_compute_way.currentIndexChanged['int'].connect(Ticket_Dialog.on_purchase_price_compute_way_selected)
        self.sell_compute_way.currentIndexChanged['int'].connect(Ticket_Dialog.on_sell_price_compute_way_selected)
        self.select_date_btn.clicked.connect(Ticket_Dialog.on_ticket_add_date_selected)
        QtCore.QMetaObject.connectSlotsByName(Ticket_Dialog)

    def retranslateUi(self, Ticket_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Ticket_Dialog.setWindowTitle(_translate("Ticket_Dialog", "Dialog"))
        self.ticket_name_label.setText(_translate("Ticket_Dialog", "输入票种名称"))
        self.ticket_price_label.setText(_translate("Ticket_Dialog", "输入票种进价"))
        self.confirm.setText(_translate("Ticket_Dialog", "确定"))
        self.cancel.setText(_translate("Ticket_Dialog", "取消"))
        self.ticket_price_label_2.setText(_translate("Ticket_Dialog", "输入票种售价"))
        self.ticket_price_label_3.setText(_translate("Ticket_Dialog", "选择计价方式"))
        self.ticket_price_label_4.setText(_translate("Ticket_Dialog", "选择计价方式"))
        self.select_date_btn.setText(_translate("Ticket_Dialog", "选择添加日期"))

