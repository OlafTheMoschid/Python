import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.kspace = False
        self.kLmouse = False
        self.kRmouse = False
        self.x = 0
        self.y = 0
        self.r = 30
        self.colour = "Black"
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.kspace = True
            self.repaint()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.kLmouse = True
            self.repaint()
        elif (event.button() == Qt.RightButton):
            self.kRmouse = True
            self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(self.colour))
        if self.kLmouse == True:
            qp.drawEllipse(int(self.x - self.r / 2),
                           int(self.y - self.r / 2), self.r, self.r)
        if self.kRmouse == True:
            qp.drawRect(int(self.x - self.r / 2),
                        int(self.y - self.r / 2), self.r, self.r)
        if self.kspace == True:
            pol = QPolygon([QPoint(self.x, int(self.y - self.r / 2)), QPoint(int(self.x + self.r / 2),
                           int(self.y + self.r / 2)), QPoint(int(self.x - self.r / 2), int(self.y + self.r / 2))])
            qp.drawPolygon(pol)

        self.kspace = False
        self.kLmouse = False
        self.kRmouse = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
