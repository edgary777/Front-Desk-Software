from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtGui import QPainter


class PicButton(QAbstractButton):
    '''Creates an image button with static, hovered, and clicked states.

    Functionality is mostly the same as QPushButton.
    '''
    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
        super().__init__(parent)
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)

    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()

    def sizeHint(self):
        return self.pixmap.size()
