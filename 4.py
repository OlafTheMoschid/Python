import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 150
        self.r = 300
        self.btnsize = 30

        self.setGeometry(300, 300, self.r, self.r)
        self.btn = QPushButton(self)
        self.btn.resize(self.btnsize, self.btnsize)
        self.btn.move(self.x - self.btnsize, self.y - self.btnsize)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.x = random.randint(0, self.r - self.btnsize)
        self.y = random.randint(0, self.r - self.btnsize)
        if self.x > event.x() + self.btnsize and self.y > event.y() + self.btnsize or \
            self.x < event.x() - self.btnsize and self.y < event.y() - self.btnsize or \
                self.x < event.x() - self.btnsize and self.y > event.y() + self.btnsize or \
        self.x > event.x() + self.btnsize and self.y < event.y() - self.btnsize:
            self.btn.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
