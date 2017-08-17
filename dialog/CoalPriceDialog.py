# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog

from ui.coal_price_manage import Ui_CoalPrice


class CoalPriceDialog(QDialog):
    def __init__(self, parent=None):
        super(CoalPriceDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_CoalPrice()
        self.ui.setupUi(self)

