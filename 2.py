import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui2 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        f = open('lines.txt', 'r', encoding='utf8')
        s = f.readlines()
        f.close()

        if len(s) > 0:
            self.line1 = s[0::2]
            self.line2 = s[1::2]
            self.pushButton.clicked.connect(self.run)
        else:
            self.plainTextEdit.setPlainText("File is empty")
            self.plainTextEdit_2.setPlainText("File is empty")

    def run(self):
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit_2.setPlainText("")
        for i in self.line1:
            if i.find('\n'):
                i = i[:-1]
                self.plainTextEdit.appendPlainText(i)
        for i in self.line2:
            if i.find('\n'):
                i = i[:-1]
            self.plainTextEdit_2.appendPlainText(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
