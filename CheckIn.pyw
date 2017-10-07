import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Functions


class CheckIn(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint |
                         Qt.WindowSystemMenuHint)
        self.initUi()

    def initUi(self):

        #######################################################################
        #######################################################################
        # Definiciones de las paginas

        search = Search()
        p1 = PersonalData()

        #######################################################################
        #######################################################################
        # Setup de mainLayout

        self.mainLayout = QStackedLayout()
        self.mainLayout.addWidget(p1)

        #######################################################################
        #######################################################################
        # Setup de abstractLayout

        self.abstractLayout = QStackedLayout()
        self.abstractLayout.addWidget(search)

        #######################################################################
        #######################################################################
        # Setup del layout

        layout = QHBoxLayout()
        layout.addLayout(self.abstractLayout, 1)
        layout.addLayout(self.mainLayout, 3)

        self.setLayout(layout)

        #######################################################################
        #######################################################################
        # configuración de la ventana

        self.resize(900, 450)
        Functions.center(self)

    def nextPage(self):
        self.layout.setCurrentIndex(self.layout.currentIndex + 1)

    def previousPage(self):
        self.layout.setCurrentIndex(self.layout.currentIndex - 1)

    def cancel(self):
        pass


class Search(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        #######################################################################
        #######################################################################
        # Setup de los botones

        walkIn = QPushButton("Check-in Rapido")

        nameSearch = QPushButton("Buscar por Nombre")
        phoneSearch = QPushButton("Buscar por Teléfono")
        idSearch = QPushButton("Buscar por ID")

        exit = QPushButton("Cancelar")

        #######################################################################
        #######################################################################
        # setup del layout

        layout = QVBoxLayout()
        layout.addWidget(walkIn)
        layout.addSpacing(30)
        layout.addWidget(nameSearch)
        layout.addWidget(phoneSearch)
        layout.addWidget(idSearch)
        layout.addStretch()
        layout.addWidget(exit)

        self.setLayout(layout)


class PersonalData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):

        #######################################################################
        #######################################################################
        # Fields setup
        # All fields are the same in here so it made sense to create them in a
        # loop.
        # variable name base and the text for the label are defined in a dict,
        # then we loop through it and define them.

        varDict = {"name": "Nombre(S)", "surnameF": "Appellido Paterno",
                   "surnameM": "Appellido Materno", "street": "Calle",
                   "extNo": "No. Ext", "intNo": "No. Int",
                   "district": "Colonia", "county": "Municipio",
                   "state": "Estado", "country": "País", "phone": "Teléfono",
                   "email": "E-Mail"}

        for key, value in varDict.items():
            # Input field is created
            setattr(self, key, QLineEdit())
            # Label is created
            setattr(self, key + "Label", QLabel(value))
            # Label is aligned to center
            getattr(self, key + "Label").setAlignment(Qt.AlignCenter)
            # Layout is created
            setattr(self, key + "Layout", QVBoxLayout())
            # Stretch is added to layout
            getattr(self, key + "Layout").addStretch()
            # Label is added to layout
            getattr(self, key + "Layout").addWidget(getattr(self,
                                                    key + "Label"))
            # Input field is added to layout
            getattr(self, key + "Layout").addWidget(getattr(self, key))
            # Stretch is added to layout
            getattr(self, key + "Layout").addStretch()

        #######################################################################
        #######################################################################
        # Layout setup

        self.btnNext = QPushButton("Siguiente")
        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        btnLayout.addWidget(self.btnNext)

        #######################################################################
        #######################################################################
        # Layout setup

        l1 = QHBoxLayout()
        l1.addLayout(self.nameLayout)
        l1.addLayout(self.surnameFLayout)
        l1.addLayout(self.surnameMLayout)

        l2 = QHBoxLayout()
        l2.addLayout(self.streetLayout, 4)
        l2.addLayout(self.extNoLayout, 1)
        l2.addLayout(self.intNoLayout, 1)
        l2.addSpacing(20)
        l2.addLayout(self.districtLayout, 4)

        l3 = QHBoxLayout()
        l3.addLayout(self.countyLayout, 2)
        l3.addLayout(self.stateLayout, 2)
        l3.addLayout(self.countryLayout, 2)
        l3.addLayout(self.emailLayout, 5)

        layout = QVBoxLayout()
        layout.addLayout(l1)
        layout.addLayout(l2)
        layout.addLayout(l3)
        layout.addLayout(btnLayout)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = CheckIn()
window.show()
sys.exit(app.exec_())
