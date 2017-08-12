from PyQt5.QtWidgets import QDialog

from ui.calendar import Ui_Calendar_Dialog


class CalendarDialog(QDialog):
    def __init__(self, parent=None):
        super(CalendarDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Calendar_Dialog()
        self.ui.setupUi(self)

    def date_clicked(self):
        self.date_time = self.ui.calendarWidget.selectedDate().toPyDate()
