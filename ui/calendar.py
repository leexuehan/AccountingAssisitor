# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calendar_Dialog(object):
    def setupUi(self, Calendar_Dialog):
        Calendar_Dialog.setObjectName("Calendar_Dialog")
        Calendar_Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Calendar_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(Calendar_Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(80, 20, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Calendar_Dialog)
        self.buttonBox.accepted.connect(Calendar_Dialog.accept)
        self.buttonBox.rejected.connect(Calendar_Dialog.reject)
        Calendar_Dialog.accepted.connect(Calendar_Dialog.date_clicked)
        QtCore.QMetaObject.connectSlotsByName(Calendar_Dialog)

    def retranslateUi(self, Calendar_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Calendar_Dialog.setWindowTitle(_translate("Calendar_Dialog", "Dialog"))

