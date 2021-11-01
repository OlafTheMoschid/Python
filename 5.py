import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from ui5 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showPlot)

    def showPlot(self):
        func = eval('lambda x:' + self.plainTextEdit.toPlainText())

        a = int(self.plainTextEdit_2.toPlainText())
        b = int(self.plainTextEdit_3.toPlainText())

        i = list(range(a, b + 1))
        j = [func(x) for x in i]

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.graphWidget.plot(i, j)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
