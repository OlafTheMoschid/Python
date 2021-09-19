import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QCheckBox


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 900, 480)
        self.setWindowTitle('CheckBox')

        self.first_line = QLineEdit(self)
        self.first_line.move(50, 100)
        self.second_line = QLineEdit(self)
        self.second_line.move(400, 100)
        self.btn = QPushButton('->', self)
        self.btn.move(250, 100)

        self.chb1 = QCheckBox(self)
        self.chb1.move(50, 150)
        self.chb2 = QCheckBox(self)
        self.chb2.move(400, 150)
        self.chb3 = QCheckBox(self)
        self.chb3.move(250, 150)

        self.chb1.clicked.connect(self.hideWidget)
        self.chb2.clicked.connect(self.hideWidget)
        self.chb3.clicked.connect(self.hideWidget)

    def hideWidget(self):
        self.first_line.hide() if self.chb1.isChecked() else self.first_line.show()
        self.second_line.hide() if self.chb2.isChecked() else self.second_line.show()
        self.btn.hide() if self.chb3.isChecked() else self.btn.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
