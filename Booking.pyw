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
        arrivalLabel.setWordWrap(True)
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
        departureLabel.setWordWrap(True)
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

        guests = QSpinBox()
        guests.setRange(1, 10)
        # guests.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        guestsLabel = QLabel("Número de huespedes:")
        guestsLabel.setWordWrap(True)

        guestsLayout = QHBoxLayout()
        guestsLayout.addStretch()
        guestsLayout.addWidget(guestsLabel)
        guestsLayout.addWidget(guests)
        guestsLayout.addSpacing(20)

        #######################################################################
        #######################################################################

        name = QLineEdit()
        nameLabel = QLabel("Nombre:")
        nameLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        nameSearchBtn = QToolButton()
        nameSearchBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        nameLayout = QHBoxLayout()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(name)
        nameLayout.addWidget(nameSearchBtn)

        #######################################################################
        #######################################################################

        hLayout1 = QHBoxLayout()
        hLayout1.addLayout(guestsLayout,  1)
        hLayout1.addLayout(nameLayout, 5)

        #######################################################################
        #######################################################################

        phone = QLineEdit()
        phoneLabel = QLabel("Telefono:")
        phoneLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        phoneSearchBtn = QToolButton()
        phoneSearchBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        phoneLayout = QHBoxLayout()
        phoneLayout.addWidget(phoneLabel)
        phoneLayout.addWidget(phone)
        phoneLayout.addWidget(phoneSearchBtn)

        #######################################################################
        #######################################################################

        car = QCheckBox()
        carLabel = QLabel("Estacionamiento:")

        carLayout = QHBoxLayout()
        carLayout.addWidget(carLabel)
        carLayout.addWidget(car)

        #######################################################################
        #######################################################################

        hLayout2 = QHBoxLayout()
        hLayout2.addLayout(phoneLayout, 5)
        hLayout2.addSpacing(20)
        hLayout2.addLayout(carLayout), 1

        #######################################################################
        #######################################################################

        btnBx = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        #######################################################################
        #######################################################################

        layout = QGridLayout()
        layout.addLayout(datesLayout, 0, 0)
        layout.addWidget(calendar, 0, 1)
        layout.addLayout(hLayout1, 1, 0, 1, 2)
        layout.addLayout(hLayout2, 2, 0, 1, 2)
        layout.addWidget(btnBx, 3, 1)


        self.setLayout(layout)


app = QApplication(sys.argv)
window = Booking()
window.show()
sys.exit(app.exec_())
