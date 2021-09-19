import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 900, 480)
        self.setWindowTitle('Throw-o-Matic')

        self.first_line = QLineEdit(self)
        self.first_line.move(50, 100)
        self.second_line = QLineEdit(self)
        self.second_line.move(400, 100)
        self.btn = QPushButton('->', self)
        self.btn.move(250, 100)
        self.btn.clicked.connect(self.button)
        self.second_line.setDisabled(True)
        self.count = 1

    def button(self):
        if self.count % 2 == 0:
            self.btn.setText('->')
            self.first_line.setText(f'{self.second_line.text()}')
            self.second_line.setText("")
        else:
            self.btn.setText('<-')
            self.second_line.setText(f'{self.first_line.text()}')
            self.first_line.setText("")
            self.first_line.setDisabled(True)
        self.count += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
