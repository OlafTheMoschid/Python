import registre

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QPlainTextEdit


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 480, 480)
        self.setWindowTitle('Register')

        self.first_label = QLabel('Login', self)
        self.first_label.move(50, 50)

        self.first_line = QLineEdit(self)
        self.first_line.move(50, 65)
        self.first_line.resize(200, 20)

        self.second_label = QLabel('Password', self)
        self.second_label.move(50, 90)

        self.second_line = QLineEdit(self)
        self.second_line.move(50, 105)
        self.second_line.resize(200, 20)

        self.third_label = QLabel('Number', self)
        self.third_label.move(50, 130)

        self.third_line = QLineEdit(self)
        self.third_line.move(50, 145)
        self.third_line.resize(200, 20)

        self.btn = QPushButton('Register', self)
        self.btn.move(100, 200)
        self.btn.clicked.connect(self.button)

        self.plane_text = QPlainTextEdit(self)
        self.plane_text.setReadOnly(True)
        self.plane_text.move(50, 250)
        self.plane_text.resize(380, 80)

    def button(self):
        self.plane_text.setPlainText("")
        pw = self.second_line.text()
        password = registre.PasswordChecker()

        ph = self.third_line.text()
        number = registre.NumberChecker()
        count = 0
        try:
            password.main(pw)
            count += 1
        except registre.PasswordError as e:
            self.plane_text.appendPlainText(e.args[0])
        try:
            number.main(ph)
            count += 1
        except registre.NumberError as e:
            self.plane_text.appendPlainText(e.args[0])
        if count == 2:
            self.plane_text.setPlainText("You've been successfully registered")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
