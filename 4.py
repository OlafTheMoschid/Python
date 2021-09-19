import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QPlainTextEdit


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 900, 480)
        self.setWindowTitle('Morse')

        self.abc = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
                    13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: ' '}

        self.d = {0: '•-', 1: '-•••', 2: '-•-•', 3: '-••', 4: '•', 5: '••-•', 6: '--•', 7: '••••', 8: '••', 9: '•---', 10: '-•-', 11: '•-••', 12: '--', 13: '-•',
                  14: '---', 15: '•--•', 16: '--•-', 17: '•-•', 18: '•••', 19: '-', 20: '••-', 21: '•••-', 22: '•--', 23: '-••-', 24: '-•--', 25: '--••', 26: ' '}

        self.lng = len(self.abc)

        self.first_line = QLineEdit(self)
        self.first_line.move(50, 100)
        self.first_line.resize(800, 20)
        self.second_line = QLineEdit(self)
        self.second_line.move(50, 130)
        self.second_line.resize(800, 20)

        self.first_line.setDisabled(True)
        self.second_line.setDisabled(True)

        self.a = [0] * self.lng

        for i in range(self.lng):
            x = self.abc.get(i)
            self.a[i] = QPushButton(x, self)
            self.a[i].resize(20, 25)
            self.a[i].move(50 + i * 30, 50)
            self.a[i].clicked.connect(self.buttons)

    def buttons(self):
        send = self.sender()
        for i in range(self.lng):
            if self.a[i] == send:
                self.first_line.insert(str(self.abc.get(i)))
                self.second_line.insert(str(self.d.get(i)) + " ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
