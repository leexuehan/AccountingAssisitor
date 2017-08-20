# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket_sort_manage.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ticket_Sort_Manage(object):
    def setupUi(self, Ticket_Sort_Manage):
        Ticket_Sort_Manage.setObjectName("Ticket_Sort_Manage")
        Ticket_Sort_Manage.setWindowModality(QtCore.Qt.WindowModal)
        Ticket_Sort_Manage.resize(774, 386)
        self.ticket_name_label = QtWidgets.QLabel(Ticket_Sort_Manage)
        self.ticket_name_label.setGeometry(QtCore.QRect(80, 110, 91, 16))
        self.ticket_name_label.setObjectName("ticket_name_label")
        self.ticket_price_label = QtWidgets.QLabel(Ticket_Sort_Manage)
        self.ticket_price_label.setGeometry(QtCore.QRect(80, 150, 91, 16))
        self.ticket_price_label.setObjectName("ticket_price_label")
        self.confirm = QtWidgets.QPushButton(Ticket_Sort_Manage)
        self.confirm.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Ticket_Sort_Manage)
        self.cancel.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.cancel.setObjectName("cancel")
        self.ticket_price_label_2 = QtWidgets.QLabel(Ticket_Sort_Manage)
        self.ticket_price_label_2.setGeometry(QtCore.QRect(80, 190, 91, 16))
        self.ticket_price_label_2.setObjectName("ticket_price_label_2")
        self.ticket_price_label_3 = QtWidgets.QLabel(Ticket_Sort_Manage)
        self.ticket_price_label_3.setGeometry(QtCore.QRect(300, 150, 81, 16))
        self.ticket_price_label_3.setObjectName("ticket_price_label_3")
        self.purchase_compute_way = QtWidgets.QComboBox(Ticket_Sort_Manage)
        self.purchase_compute_way.setGeometry(QtCore.QRect(380, 150, 69, 22))
        self.purchase_compute_way.setObjectName("purchase_compute_way")
        self.ticket_price_label_4 = QtWidgets.QLabel(Ticket_Sort_Manage)
        self.ticket_price_label_4.setGeometry(QtCore.QRect(300, 190, 81, 16))
        self.ticket_price_label_4.setObjectName("ticket_price_label_4")
        self.sell_compute_way = QtWidgets.QComboBox(Ticket_Sort_Manage)
        self.sell_compute_way.setGeometry(QtCore.QRect(380, 190, 69, 22))
        self.sell_compute_way.setObjectName("sell_compute_way")
        self.select_date_btn = QtWidgets.QPushButton(Ticket_Sort_Manage)
        self.select_date_btn.setGeometry(QtCore.QRect(74, 70, 81, 23))
        self.select_date_btn.setObjectName("select_date_btn")
        self.add_detail_list = QtWidgets.QListView(Ticket_Sort_Manage)
        self.add_detail_list.setGeometry(QtCore.QRect(470, 50, 256, 271))
        self.add_detail_list.setObjectName("add_detail_list")
        self.purchase_price = QtWidgets.QLineEdit(Ticket_Sort_Manage)
        self.purchase_price.setGeometry(QtCore.QRect(170, 150, 111, 20))
        self.purchase_price.setObjectName("purchase_price")
        self.sell_price = QtWidgets.QLineEdit(Ticket_Sort_Manage)
        self.sell_price.setGeometry(QtCore.QRect(170, 190, 111, 20))
        self.sell_price.setObjectName("sell_price")
        self.ticket_name = QtWidgets.QLineEdit(Ticket_Sort_Manage)
        self.ticket_name.setGeometry(QtCore.QRect(170, 110, 111, 20))
        self.ticket_name.setObjectName("ticket_name")
        self.select_date = QtWidgets.QLineEdit(Ticket_Sort_Manage)
        self.select_date.setGeometry(QtCore.QRect(170, 70, 111, 20))
        self.select_date.setObjectName("select_date")
        self.modify_label = QtWidgets.QLabel(Ticket_Sort_Manage)
        self.modify_label.setGeometry(QtCore.QRect(470, 20, 191, 20))
        self.modify_label.setObjectName("modify_label")

        self.retranslateUi(Ticket_Sort_Manage)
        self.cancel.clicked.connect(Ticket_Sort_Manage.reject)
        self.confirm.clicked.connect(Ticket_Sort_Manage.on_ok)
        self.purchase_compute_way.currentIndexChanged['int'].connect(Ticket_Sort_Manage.on_purchase_price_compute_way_selected)
        self.sell_compute_way.currentIndexChanged['int'].connect(Ticket_Sort_Manage.on_sell_price_compute_way_selected)
        self.select_date_btn.clicked.connect(Ticket_Sort_Manage.on_ticket_add_date_selected)
        QtCore.QMetaObject.connectSlotsByName(Ticket_Sort_Manage)

    def retranslateUi(self, Ticket_Sort_Manage):
        _translate = QtCore.QCoreApplication.translate
        Ticket_Sort_Manage.setWindowTitle(_translate("Ticket_Sort_Manage", "票种添加"))
        self.ticket_name_label.setText(_translate("Ticket_Sort_Manage", "输入票种名称"))
        self.ticket_price_label.setText(_translate("Ticket_Sort_Manage", "输入票种进价"))
        self.confirm.setText(_translate("Ticket_Sort_Manage", "确定"))
        self.cancel.setText(_translate("Ticket_Sort_Manage", "取消"))
        self.ticket_price_label_2.setText(_translate("Ticket_Sort_Manage", "输入票种售价"))
        self.ticket_price_label_3.setText(_translate("Ticket_Sort_Manage", "选择计价方式"))
        self.ticket_price_label_4.setText(_translate("Ticket_Sort_Manage", "选择计价方式"))
        self.select_date_btn.setText(_translate("Ticket_Sort_Manage", "选择添加日期"))
        self.modify_label.setText(_translate("Ticket_Sort_Manage", "最近添加项"))

