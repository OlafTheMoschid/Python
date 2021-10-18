import home1

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QPlainTextEdit


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 480, 480)
        self.setWindowTitle('Words')

        self.btn = QPushButton('Compute', self)
        self.btn.move(200, 50)
        self.btn.clicked.connect(self.button)

        self.plane_text = QPlainTextEdit(self)
        self.plane_text.setReadOnly(True)
        self.plane_text.move(50, 100)
        self.plane_text.resize(380, 180)

    def button(self):
        password = home1.PasswordChecker()
        f = open('top 10000 passwd.txt', 'r')
        a = f.readlines()
        s = {}
        for i in a:
            try:
                password.lenghtChecker(i[:-1])
            except home1.PasswordLenghtError as e:
                s.update({e.__class__.__name__: s.get(
                    e.__class__.__name__, 0) + 1})

            try:
                password.lettersChecker(i[:-1])
            except home1.PasswordLetterError as e:
                s.update({e.__class__.__name__: s.get(
                    e.__class__.__name__, 0) + 1})

            try:
                password.digitsChecker(i[:-1])
            except home1.PasswordDigitError as e:
                s.update({e.__class__.__name__: s.get(
                    e.__class__.__name__, 0) + 1})

            try:
                password.threeChecker(i[:-1])
            except home1.PasswordThreeError as e:
                s.update({e.__class__.__name__: s.get(
                    e.__class__.__name__, 0) + 1})

            try:
                password.wordListChecker(i[:-1])
            except home1.PasswordWordsError as e:
                s.update({e.__class__.__name__: s.get(
                    e.__class__.__name__, 0) + 1})

        k = sorted(s.items(), key=lambda x: x[0])
        s = dict(k)

        for i in s:
            self.plane_text.appendPlainText(str(i) + "\t: " + str(s.get(i)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
