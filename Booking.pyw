import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Booking(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint |
                         Qt.WindowSystemMenuHint)
        self.currentD = QDate.currentDate()
        self.cal = QCalendarWidget()
        self.initUi()

    def initUi(self):
        arrival = QDateEdit()
        arrival.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        arrival.setDisplayFormat('d MMM yyyy')
        arrival.setDateRange(self.currentD,
                             self.cal.maximumDate())
        arrivalLabel = QLabel("Fecha de llegada:")
        arrivalLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        arrivalBtnCal = QToolButton()
        arrivalBtnCal.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        arrivalLayout = QHBoxLayout()
        arrivalLayout.addWidget(arrivalLabel)
        arrivalLayout.addStretch()
        arrivalLayout.addWidget(arrival)
        arrivalLayout.addWidget(arrivalBtnCal)

        #######################################################################
        #######################################################################

        departure = QDateEdit()
        departure.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        departure.setDisplayFormat('d MMM yyyy')
        departure.setDateRange(self.currentD.addDays(1),
                               self.cal.maximumDate())
        departureLabel = QLabel("Fecha de salida")
        departureLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        departureBtnCal = QToolButton()
        departureBtnCal.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        departureLayout = QHBoxLayout()
        departureLayout.addWidget(departureLabel)
        departureLayout.addStretch()
        departureLayout.addWidget(departure)
        departureLayout.addWidget(departureBtnCal)

        #######################################################################
        #######################################################################

        datesLayout = QVBoxLayout()
        datesLayout.addLayout(arrivalLayout)
        datesLayout.addLayout(departureLayout)

        #######################################################################
        #######################################################################

        calendar = QCalendarWidget()
        calendar.setHorizontalHeaderFormat(QCalendarWidget.
                                           HorizontalHeaderFormat(1))

        #######################################################################
        #######################################################################

        layout = QGridLayout()
        layout.addLayout(datesLayout, 0, 0)
        layout.addWidget(calendar, 0, 1)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = Booking()
window.show()
sys.exit(app.exec_())
