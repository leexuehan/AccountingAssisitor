# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coal_sort_manage.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Coal_Sort_Manage(object):
    def setupUi(self, Coal_Sort_Manage):
        Coal_Sort_Manage.setObjectName("Coal_Sort_Manage")
        Coal_Sort_Manage.resize(743, 453)
        self.ticket_price_label_3 = QtWidgets.QLabel(Coal_Sort_Manage)
        self.ticket_price_label_3.setGeometry(QtCore.QRect(240, 100, 81, 16))
        self.ticket_price_label_3.setObjectName("ticket_price_label_3")
        self.coal_name_label = QtWidgets.QLabel(Coal_Sort_Manage)
        self.coal_name_label.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.coal_name_label.setObjectName("coal_name_label")
        self.sell_compute_way = QtWidgets.QComboBox(Coal_Sort_Manage)
        self.sell_compute_way.setGeometry(QtCore.QRect(320, 140, 69, 22))
        self.sell_compute_way.setObjectName("sell_compute_way")
        self.purchase_compute_way = QtWidgets.QComboBox(Coal_Sort_Manage)
        self.purchase_compute_way.setGeometry(QtCore.QRect(320, 100, 69, 22))
        self.purchase_compute_way.setObjectName("purchase_compute_way")
        self.ticket_price_label_4 = QtWidgets.QLabel(Coal_Sort_Manage)
        self.ticket_price_label_4.setGeometry(QtCore.QRect(240, 140, 81, 16))
        self.ticket_price_label_4.setObjectName("ticket_price_label_4")
        self.select_date_btn = QtWidgets.QPushButton(Coal_Sort_Manage)
        self.select_date_btn.setGeometry(QtCore.QRect(14, 20, 81, 23))
        self.select_date_btn.setObjectName("select_date_btn")
        self.ticket_price_label = QtWidgets.QLabel(Coal_Sort_Manage)
        self.ticket_price_label.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.ticket_price_label.setObjectName("ticket_price_label")
        self.ticket_price_label_2 = QtWidgets.QLabel(Coal_Sort_Manage)
        self.ticket_price_label_2.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.ticket_price_label_2.setObjectName("ticket_price_label_2")
        self.confirm = QtWidgets.QPushButton(Coal_Sort_Manage)
        self.confirm.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Coal_Sort_Manage)
        self.cancel.setGeometry(QtCore.QRect(230, 230, 75, 23))
        self.cancel.setObjectName("cancel")
        self.date_value_content = QtWidgets.QLineEdit(Coal_Sort_Manage)
        self.date_value_content.setGeometry(QtCore.QRect(110, 20, 151, 20))
        self.date_value_content.setObjectName("date_value_content")
        self.coal_sort_name = QtWidgets.QLineEdit(Coal_Sort_Manage)
        self.coal_sort_name.setGeometry(QtCore.QRect(110, 60, 151, 20))
        self.coal_sort_name.setObjectName("coal_sort_name")
        self.purchase_price = QtWidgets.QLineEdit(Coal_Sort_Manage)
        self.purchase_price.setGeometry(QtCore.QRect(110, 100, 81, 20))
        self.purchase_price.setObjectName("purchase_price")
        self.sell_price = QtWidgets.QLineEdit(Coal_Sort_Manage)
        self.sell_price.setGeometry(QtCore.QRect(110, 140, 81, 20))
        self.sell_price.setObjectName("sell_price")
        self.modify_detail_list = QtWidgets.QListView(Coal_Sort_Manage)
        self.modify_detail_list.setGeometry(QtCore.QRect(460, 60, 256, 271))
        self.modify_detail_list.setObjectName("modify_detail_list")
        self.modify_label = QtWidgets.QLabel(Coal_Sort_Manage)
        self.modify_label.setGeometry(QtCore.QRect(460, 30, 191, 20))
        self.modify_label.setObjectName("modify_label")

        self.retranslateUi(Coal_Sort_Manage)
        self.purchase_compute_way.currentIndexChanged['int'].connect(Coal_Sort_Manage.on_purchase_compute_way_selected)
        self.sell_compute_way.currentIndexChanged['int'].connect(Coal_Sort_Manage.on_sell_compute_way_selected)
        self.select_date_btn.clicked.connect(Coal_Sort_Manage.on_add_new_coal_date_selected)
        self.confirm.clicked.connect(Coal_Sort_Manage.add_new_coal)
        self.cancel.clicked.connect(Coal_Sort_Manage.reject)
        QtCore.QMetaObject.connectSlotsByName(Coal_Sort_Manage)

    def retranslateUi(self, Coal_Sort_Manage):
        _translate = QtCore.QCoreApplication.translate
        Coal_Sort_Manage.setWindowTitle(_translate("Coal_Sort_Manage", "煤种添加"))
        self.ticket_price_label_3.setText(_translate("Coal_Sort_Manage", "选择计价方式"))
        self.coal_name_label.setText(_translate("Coal_Sort_Manage", "输入煤种名称"))
        self.ticket_price_label_4.setText(_translate("Coal_Sort_Manage", "选择计价方式"))
        self.select_date_btn.setText(_translate("Coal_Sort_Manage", "选择添加日期"))
        self.ticket_price_label.setText(_translate("Coal_Sort_Manage", "输入煤种进价"))
        self.ticket_price_label_2.setText(_translate("Coal_Sort_Manage", "输入煤种售价"))
        self.confirm.setText(_translate("Coal_Sort_Manage", "确定添加"))
        self.cancel.setText(_translate("Coal_Sort_Manage", "取消"))
        self.modify_label.setText(_translate("Coal_Sort_Manage", "最近添加项"))

