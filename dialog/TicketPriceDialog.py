from PyQt5.QtWidgets import QDialog

from ui.ticket_price_manage import Ui_Ticket_Price


class TicketPriceDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketPriceDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Ticket_Price()
        self.ui.setupUi(self)

        # init hide component
        self.hide_sell_price_related()
        self.hide_purchase_price_related()

        # init combox
        self.compute_ways = ['元/吨', '元/车']
        self.ticket_sorts = []
        self.ticket_sorts_selected = None
        self.init_ticket_sorts_from_db()
        self.init_compute_unit()
