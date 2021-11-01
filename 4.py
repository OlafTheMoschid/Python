import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QSlider
from PyQt5.QtGui import QPainter, QColor


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.verticalSlider = QSlider(self)
        self.verticalSlider.setGeometry(550, 10, 22, 160)
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(500)
        self.verticalSlider.valueChanged[int].connect(self.slider)
        self.setGeometry(10, 10, 900, 600)
        self.n = 1

    def initUI(self):
        self.colour, ok = QInputDialog.getItem(
            self, "Choise the colour", "Choise the colour", ("Red", "Green", "Blue"), editable=False)
        if ok == False:
            self.colour = "Red"

    def slider(self, value):
        self.n = value
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_smile(qp)
        qp.end()

    def draw_smile(self, qp):
        qp.setBrush(QColor(self.colour))
        qp.drawEllipse(0, 0, self.n, self.n)
        qp.drawEllipse(int(self.n / 2 - self.n / 4),
                       int(self.n / 5), int(self.n / 5), int(self.n / 5))
        qp.drawEllipse(int(self.n / 2 + self.n / 20),
                       int(self.n / 5), int(self.n / 5), int(self.n / 5))
        qp.drawRect(int(self.n / 8), int(self.n - self.n / (2 * 1.1)),
                    int(self.n - self.n / 4), int(self.n / 5))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
