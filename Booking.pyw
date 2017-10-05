import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Booking(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint |
                         Qt.WindowSystemMenuHint)

        self.initUi()

    def initUi(self):
        pass


app = QApplication(sys.argv)
window = Booking()
window.show()
sys.exit(app.exec_())
