import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui1 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        f = open('lines.txt', 'r', encoding='utf8')
        self.s = f.readlines()
        f.close()

        if len(self.s) > 0:
            self.pushButton.clicked.connect(self.run)
        else:
            self.plainTextEdit.setPlainText("File is empty")

    def run(self):
        line = (self.s[np.random.randint(len(self.s))])
        self.plainTextEdit.setPlainText(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
