from PyQt5.QtWidgets import QMessageBox, QMainWindow


class VerifyUtils(QMainWindow):
    def verify_input(self, verify_element, warning_msg):
        if verify_element is None:
            QMessageBox.critical(self, "Critical", self.tr(warning_msg))
            return False
        else:
            return True
