import sys

from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog
from PyQt5.QtGui import QPainter, QColor

import numpy as np


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.m = (np.random.randint(1, 255, self.quantity + 2))

    def initUI(self):
        self.quantity, ok = QInputDialog.getInt(
            self, "Choise the quantity of colours", "Choise the quantity of colours", min=1, max=10)
        if ok == False:
            self.quantity = 1

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        for i in range(0, self.quantity):
            qp.setBrush(QColor(self.m[i], self.m[i + 1], self.m[i + 2]))
            qp.drawRect(30, 30 * (i+1), 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
