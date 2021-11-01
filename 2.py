import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui2 import Ui_MainWindow
from PIL import Image, ImageQt


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.verticalSlider.valueChanged[int].connect(self.slider)

    def initUI(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Choise the picture', '', 'Picture (*.png);;Picture (*.jpg);;All files (*)')
        with Image.open(fname[0]) as self.im:
            self.im = self.im.resize((500, 500)).convert('RGBA')

        self.imQT = ImageQt.ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(self.pixmap)

    def slider(self, value):
        self.im.putalpha(int(value / 99 * 255))

        self.imQT = ImageQt.ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.imQT)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
