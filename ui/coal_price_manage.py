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
        CoalPrice.resize(741, 443)
        self.selectDate = QtWidgets.QPushButton(CoalPrice)
        self.selectDate.setGeometry(QtCore.QRect(14, 50, 81, 23))
        self.selectDate.setObjectName("selectDate")
        self.coal_sorts = QtWidgets.QComboBox(CoalPrice)
        self.coal_sorts.setGeometry(QtCore.QRect(110, 90, 131, 21))
        self.coal_sorts.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.coal_sorts.setObjectName("coal_sorts")
        self.coal_sell_price_display = QtWidgets.QLabel(CoalPrice)
        self.coal_sell_price_display.setGeometry(QtCore.QRect(90, 220, 101, 20))
        self.coal_sell_price_display.setObjectName("coal_sell_price_display")
        self.coal_sort_label = QtWidgets.QLabel(CoalPrice)
        self.coal_sort_label.setGeometry(QtCore.QRect(40, 90, 59, 16))
        self.coal_sort_label.setObjectName("coal_sort_label")
        self.coal_purchase_price_display = QtWidgets.QLabel(CoalPrice)
        self.coal_purchase_price_display.setGeometry(QtCore.QRect(90, 160, 101, 20))
        self.coal_purchase_price_display.setObjectName("coal_purchase_price_display")
        self.purchase_compute_unit = QtWidgets.QComboBox(CoalPrice)
        self.purchase_compute_unit.setGeometry(QtCore.QRect(370, 160, 69, 22))
        self.purchase_compute_unit.setObjectName("purchase_compute_unit")
        self.coal_purchase_price_label = QtWidgets.QLabel(CoalPrice)
        self.coal_purchase_price_label.setGeometry(QtCore.QRect(340, 160, 31, 16))
        self.coal_purchase_price_label.setObjectName("coal_purchase_price_label")
        self.date_value_content = QtWidgets.QLineEdit(CoalPrice)
        self.date_value_content.setGeometry(QtCore.QRect(110, 50, 151, 20))
        self.date_value_content.setObjectName("date_value_content")
        self.ok = QtWidgets.QPushButton(CoalPrice)
        self.ok.setGeometry(QtCore.QRect(250, 370, 81, 23))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(CoalPrice)
        self.cancel.setGeometry(QtCore.QRect(360, 370, 81, 23))
        self.cancel.setObjectName("cancel")
        self.purchase_price_check_box = QtWidgets.QCheckBox(CoalPrice)
        self.purchase_price_check_box.setGeometry(QtCore.QRect(30, 160, 71, 16))
        self.purchase_price_check_box.setObjectName("purchase_price_check_box")
        self.sell_price_check_box = QtWidgets.QCheckBox(CoalPrice)
        self.sell_price_check_box.setGeometry(QtCore.QRect(30, 220, 71, 16))
        self.sell_price_check_box.setObjectName("sell_price_check_box")
        self.purchase_price_input = QtWidgets.QLineEdit(CoalPrice)
        self.purchase_price_input.setGeometry(QtCore.QRect(260, 160, 71, 20))
        self.purchase_price_input.setObjectName("purchase_price_input")
        self.sell_price_input = QtWidgets.QLineEdit(CoalPrice)
        self.sell_price_input.setGeometry(QtCore.QRect(260, 220, 71, 20))
        self.sell_price_input.setObjectName("sell_price_input")
        self.coal_sell_price_label = QtWidgets.QLabel(CoalPrice)
        self.coal_sell_price_label.setGeometry(QtCore.QRect(340, 220, 31, 16))
        self.coal_sell_price_label.setObjectName("coal_sell_price_label")
        self.sell_compute_unit = QtWidgets.QComboBox(CoalPrice)
        self.sell_compute_unit.setGeometry(QtCore.QRect(370, 220, 69, 22))
        self.sell_compute_unit.setObjectName("sell_compute_unit")
        self.purchase_price_change_label = QtWidgets.QLabel(CoalPrice)
        self.purchase_price_change_label.setGeometry(QtCore.QRect(200, 160, 41, 20))
        self.purchase_price_change_label.setObjectName("purchase_price_change_label")
        self.sell_price_change_label = QtWidgets.QLabel(CoalPrice)
        self.sell_price_change_label.setGeometry(QtCore.QRect(200, 220, 40, 20))
        self.sell_price_change_label.setObjectName("sell_price_change_label")
        self.change_price_success_tip = QtWidgets.QLabel(CoalPrice)
        self.change_price_success_tip.setGeometry(QtCore.QRect(120, 340, 281, 20))
        self.change_price_success_tip.setObjectName("change_price_success_tip")
        self.select_date_error_tip = QtWidgets.QLabel(CoalPrice)
        self.select_date_error_tip.setGeometry(QtCore.QRect(280, 50, 191, 20))
        self.select_date_error_tip.setObjectName("select_date_error_tip")
        self.select_date_empty_hint = QtWidgets.QLabel(CoalPrice)
        self.select_date_empty_hint.setGeometry(QtCore.QRect(280, 30, 191, 20))
        self.select_date_empty_hint.setObjectName("select_date_empty_hint")
        self.no_price_change_hint = QtWidgets.QLabel(CoalPrice)
        self.no_price_change_hint.setGeometry(QtCore.QRect(120, 320, 271, 20))
        self.no_price_change_hint.setObjectName("no_price_change_hint")
        self.modify_detail_list = QtWidgets.QListView(CoalPrice)
        self.modify_detail_list.setGeometry(QtCore.QRect(470, 40, 256, 271))
        self.modify_detail_list.setObjectName("modify_detail_list")
        self.modify_label = QtWidgets.QLabel(CoalPrice)
        self.modify_label.setGeometry(QtCore.QRect(470, 20, 191, 20))
        self.modify_label.setObjectName("modify_label")
        self.new_purchase_price_empty_hint = QtWidgets.QLabel(CoalPrice)
        self.new_purchase_price_empty_hint.setGeometry(QtCore.QRect(250, 130, 101, 20))
        self.new_purchase_price_empty_hint.setObjectName("new_purchase_price_empty_hint")
        self.new_sell_price_empty_hint = QtWidgets.QLabel(CoalPrice)
        self.new_sell_price_empty_hint.setGeometry(QtCore.QRect(250, 190, 101, 20))
        self.new_sell_price_empty_hint.setObjectName("new_sell_price_empty_hint")

        self.retranslateUi(CoalPrice)
        self.selectDate.clicked.connect(CoalPrice.open_calendar)
        self.purchase_price_check_box.stateChanged['int'].connect(CoalPrice.on_purchase_price_check_box_selected)
        self.sell_price_check_box.stateChanged['int'].connect(CoalPrice.on_sell_price_check_box_selected)
        self.cancel.clicked.connect(CoalPrice.reject)
        self.coal_sorts.currentIndexChanged['int'].connect(CoalPrice.on_coal_sort_selected)
        self.ok.clicked.connect(CoalPrice.update_price)
        self.purchase_price_input.editingFinished.connect(CoalPrice.input_purchase_price)
        self.sell_price_input.editingFinished.connect(CoalPrice.input_sell_price)
        self.purchase_compute_unit.currentIndexChanged['int'].connect(CoalPrice.on_purchase_compute_way_selected)
        self.sell_compute_unit.currentIndexChanged['int'].connect(CoalPrice.on_sell_compute_way_selected)
        QtCore.QMetaObject.connectSlotsByName(CoalPrice)

    def retranslateUi(self, CoalPrice):
        _translate = QtCore.QCoreApplication.translate
        CoalPrice.setWindowTitle(_translate("CoalPrice", "Dialog"))
        self.selectDate.setText(_translate("CoalPrice", "点击选择日期"))
        self.coal_sell_price_display.setText(_translate("CoalPrice", "这里动态显示售价"))
        self.coal_sort_label.setText(_translate("CoalPrice", "选择煤种"))
        self.coal_purchase_price_display.setText(_translate("CoalPrice", "这里动态显示进价"))
        self.coal_purchase_price_label.setText(_translate("CoalPrice", "单位"))
        self.ok.setText(_translate("CoalPrice", "确定更改"))
        self.cancel.setText(_translate("CoalPrice", "返回"))
        self.purchase_price_check_box.setText(_translate("CoalPrice", "进价"))
        self.sell_price_check_box.setText(_translate("CoalPrice", "售价"))
        self.coal_sell_price_label.setText(_translate("CoalPrice", "单位"))
        self.purchase_price_change_label.setText(_translate("CoalPrice", "变更为"))
        self.sell_price_change_label.setText(_translate("CoalPrice", "变更为"))
        self.change_price_success_tip.setText(_translate("CoalPrice", "更改煤价成功，可以继续更改，也可以点击返回退出"))
        self.select_date_error_tip.setText(_translate("CoalPrice", "只能更改2017/08/15以后的价格"))
        self.select_date_empty_hint.setText(_translate("CoalPrice", "请选择日期"))
        self.no_price_change_hint.setText(_translate("CoalPrice", "价格没有变化，请确认是否修改进价/售价"))
        self.modify_label.setText(_translate("CoalPrice", "修改项"))
        self.new_purchase_price_empty_hint.setText(_translate("CoalPrice", "请输入新的进价"))
        self.new_sell_price_empty_hint.setText(_translate("CoalPrice", "请输入新的售价"))

