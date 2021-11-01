import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui1 import Ui_MainWindow
from PIL import Image, ImageQt

import numpy as np


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.btn_red.clicked.connect(self.toRed)
        self.btn_green.clicked.connect(self.toGreen)
        self.btn_blue.clicked.connect(self.toBlue)
        self.btn_right.clicked.connect(self.rotateToRight)
        self.btn_left.clicked.connect(self.rotateToLeft)
        self.count = 0

    def initUI(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Choise the picture', '', 'Picture (*.png);;Picture (*.jpg);;All files (*)')
        with Image.open(fname[0]) as self.im:
            self.im = self.im.resize((500, 500))

        self.imCopy = self.im

        self.imQT = ImageQt.ImageQt(self.im)
        pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(pixmap)

    def toRed(self):
        imNP = np.array(self.imCopy)
        imNP[:, :, 1] = 0
        imNP[:, :, 2] = 0

        self.im = Image.fromarray(imNP)
        self.imQT = ImageQt.ImageQt(self.im.rotate(90 * self.count))
        pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(pixmap)

    def toGreen(self):
        imNP = np.array(self.imCopy)
        imNP[:, :, 0] = 0
        imNP[:, :, 2] = 0

        self.im = Image.fromarray(imNP)
        self.imQT = ImageQt.ImageQt(self.im.rotate(90 * self.count))
        pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(pixmap)

    def toBlue(self):
        imNP = np.array(self.imCopy)
        imNP[:, :, 0] = 0
        imNP[:, :, 1] = 0

        self.im = Image.fromarray(imNP)
        self.imQT = ImageQt.ImageQt(self.im.rotate(90 * self.count))
        pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(pixmap)

    def rotateToLeft(self):
        self.count = 0 if self.count <= -4 or self.count >= 4 else self.count
        self.count += 1
        self.imQT = ImageQt.ImageQt(self.im.rotate(90 * self.count))
        self.pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(self.pixmap)

    def rotateToRight(self):
        self.count = 0 if self.count <= -4 or self.count >= 4 else self.count
        self.count -= 1
        self.imQT = ImageQt.ImageQt(self.im.rotate(90 * self.count))
        self.pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
