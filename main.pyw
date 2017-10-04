import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PicButton import PicButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        btnBooking = PicButton(QPixmap("resources/bo-s.png"),
                               QPixmap("resources/bo-h.png"),
                               QPixmap("resources/bo-c.png"))
        btnCheckIn = PicButton(QPixmap("resources/ci-s.png"),
                               QPixmap("resources/ci-h.png"),
                               QPixmap("resources/ci-c.png"))
        btnCheckOut = PicButton(QPixmap("resources/co-s.png"),
                                QPixmap("resources/co-h.png"),
                                QPixmap("resources/co-c.png"))
        btnOptions = PicButton(QPixmap("resources/op-s.png"),
                               QPixmap("resources/op-h.png"),
                               QPixmap("resources/op-c.png"))

        btnLayout = QHBoxLayout(self)
        btnLayout.addStretch()
        btnLayout.addWidget(btnBooking)
        btnLayout.addWidget(btnCheckIn)
        btnLayout.addWidget(btnCheckOut)
        btnLayout.addWidget(btnOptions)
        btnLayout.addStretch()

        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addLayout(btnLayout)
        layout.addStretch()

        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.showMaximized()
sys.exit(app.exec_())
