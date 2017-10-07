import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def center(self):
    qtRectangle = self.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    self.move(qtRectangle.topLeft())
