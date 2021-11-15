import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageQt


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 200
        self.r = 500
        self.pic_size = int(self.r / 10)
        self.setGeometry(100, 100, self.r, self.r)
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setGeometry(self.x, self.y, self.pic_size, self.pic_size)

        self.fname = self.resource_path('heli.png')
        with Image.open(self.fname) as self.im:
            self.im = self.im.resize((self.pic_size, self.pic_size))

        self.imQT = ImageQt.ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(self.pixmap)

    def resource_path(self, relative):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative)
        return os.path.join(relative)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.y = self.y - self.pic_size
            if self.y < 0 or self.y > self.r:
                self.y = self.r - self.pic_size
            self.label.move(self.x, self.y)

        if event.key() == Qt.Key_Down:
            self.y = self.y + self.pic_size
            if self.y + self.pic_size < 0 or self.y + self.pic_size > self.r:
                self.y = 0
            self.label.move(self.x, self.y)

        if event.key() == Qt.Key_Left:
            self.x = self.x - self.pic_size
            if self.x < 0 or self.x > self.r:
                self.x = self.r - self.pic_size
            self.label.move(self.x, self.y)

        if event.key() == Qt.Key_Right:
            self.x = self.x + self.pic_size
            if self.x + self.pic_size < 0 or self.x + self.pic_size > self.r:
                self.x = 0
            self.label.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
