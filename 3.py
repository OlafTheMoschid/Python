import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui3 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        try:
            self.label_5.setText("")
            f = open(self.textEdit.toPlainText(), 'r', encoding='utf8')
            s = f.read().split()
            s = list(map(int, s))
            f.close()

            ma = np.max(s)
            mi = np.min(s)
            av = np.mean(s)

            self.lineEdit.setText(str(ma))
            self.lineEdit_2.setText(str(mi))
            self.lineEdit_3.setText(str(av))

            o = open('output.txt', 'w', encoding='utf8')

            o.write('max: ' + str(ma) + '\n')
            o.write('min: ' + str(mi) + '\n')
            o.write('average: ' + str(av))

            o.close()
        except:
            self.label_5.setText("Wrong file name!")
            self.textEdit.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
