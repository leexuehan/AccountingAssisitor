# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coal_price_manage.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CoalPrice(object):
    def setupUi(self, CoalPrice):
        CoalPrice.setObjectName("CoalPrice")
        CoalPrice.resize(508, 276)
        self.selectDate = QtWidgets.QPushButton(CoalPrice)
        self.selectDate.setGeometry(QtCore.QRect(34, 50, 81, 23))
        self.selectDate.setObjectName("selectDate")
        self.coal_sorts = QtWidgets.QComboBox(CoalPrice)
        self.coal_sorts.setGeometry(QtCore.QRect(130, 90, 131, 21))
        self.coal_sorts.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.coal_sorts.setObjectName("coal_sorts")
        self.label_coal_2 = QtWidgets.QLabel(CoalPrice)
        self.label_coal_2.setGeometry(QtCore.QRect(280, 90, 51, 20))
        self.label_coal_2.setObjectName("label_coal_2")
        self.coal_sell_price_display = QtWidgets.QLabel(CoalPrice)
        self.coal_sell_price_display.setGeometry(QtCore.QRect(330, 90, 101, 20))
        self.coal_sell_price_display.setObjectName("coal_sell_price_display")
        self.coal_sort_label = QtWidgets.QLabel(CoalPrice)
        self.coal_sort_label.setGeometry(QtCore.QRect(60, 90, 59, 16))
        self.coal_sort_label.setObjectName("coal_sort_label")
        self.price_sorts = QtWidgets.QComboBox(CoalPrice)
        self.price_sorts.setGeometry(QtCore.QRect(130, 140, 131, 21))
        self.price_sorts.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.price_sorts.setObjectName("price_sorts")
        self.label_coal_3 = QtWidgets.QLabel(CoalPrice)
        self.label_coal_3.setGeometry(QtCore.QRect(60, 140, 59, 16))
        self.label_coal_3.setObjectName("label_coal_3")
        self.label_coal_4 = QtWidgets.QLabel(CoalPrice)
        self.label_coal_4.setGeometry(QtCore.QRect(280, 110, 51, 20))
        self.label_coal_4.setObjectName("label_coal_4")
        self.coal_sell_price_display_2 = QtWidgets.QLabel(CoalPrice)
        self.coal_sell_price_display_2.setGeometry(QtCore.QRect(330, 110, 101, 20))
        self.coal_sell_price_display_2.setObjectName("coal_sell_price_display_2")
        self.ticket_price_label = QtWidgets.QLabel(CoalPrice)
        self.ticket_price_label.setGeometry(QtCore.QRect(60, 180, 91, 16))
        self.ticket_price_label.setObjectName("ticket_price_label")
        self.compute_way = QtWidgets.QComboBox(CoalPrice)
        self.compute_way.setGeometry(QtCore.QRect(370, 180, 69, 22))
        self.compute_way.setObjectName("compute_way")
        self.ticket_price_label_3 = QtWidgets.QLabel(CoalPrice)
        self.ticket_price_label_3.setGeometry(QtCore.QRect(290, 180, 81, 16))
        self.ticket_price_label_3.setObjectName("ticket_price_label_3")
        self.date_value_content = QtWidgets.QLineEdit(CoalPrice)
        self.date_value_content.setGeometry(QtCore.QRect(130, 50, 151, 20))
        self.date_value_content.setObjectName("date_value_content")
        self.price_content = QtWidgets.QLineEdit(CoalPrice)
        self.price_content.setGeometry(QtCore.QRect(130, 180, 151, 20))
        self.price_content.setObjectName("price_content")
        self.ok = QtWidgets.QPushButton(CoalPrice)
        self.ok.setGeometry(QtCore.QRect(270, 230, 81, 23))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(CoalPrice)
        self.cancel.setGeometry(QtCore.QRect(380, 230, 81, 23))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(CoalPrice)
        QtCore.QMetaObject.connectSlotsByName(CoalPrice)

    def retranslateUi(self, CoalPrice):
        _translate = QtCore.QCoreApplication.translate
        CoalPrice.setWindowTitle(_translate("CoalPrice", "Dialog"))
        self.selectDate.setText(_translate("CoalPrice", "点击选择日期"))
        self.label_coal_2.setText(_translate("CoalPrice", "当前售价"))
        self.coal_sell_price_display.setText(_translate("CoalPrice", "这里动态显示售价"))
        self.coal_sort_label.setText(_translate("CoalPrice", "选择煤种"))
        self.label_coal_3.setText(_translate("CoalPrice", "进价/售价"))
        self.label_coal_4.setText(_translate("CoalPrice", "进价"))
        self.coal_sell_price_display_2.setText(_translate("CoalPrice", "这里动态显示进价"))
        self.ticket_price_label.setText(_translate("CoalPrice", "输入价格"))
        self.ticket_price_label_3.setText(_translate("CoalPrice", "选择计价方式"))
        self.ok.setText(_translate("CoalPrice", "确定"))
        self.cancel.setText(_translate("CoalPrice", "返回"))

