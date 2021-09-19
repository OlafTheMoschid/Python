import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QPlainTextEdit


class Programm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 900, 480)
        self.setWindowTitle('Menu')

        self.menu = {"hamburger": 80, "cheeseburger": 90, "french fries": 50}
        self.menul = list(self.menu)

        self.lng = len(self.menu)

        self.meal = [0] * self.lng
        self.price = [0] * self.lng
        self.btn1 = [0] * self.lng
        self.btn2 = [0] * self.lng
        self.cnt = [0] * self.lng
        self.count = [0] * self.lng

        self.sum = 0

        for i in range(self.lng):
            self.meal[i] = QLabel(str(self.menul[i]), self)
            self.meal[i].move(50, 50 + i * 30)

            self.meal[i] = QLabel(
                "price : " + str(self.menu.get(self.menul[i])) + " rub", self)
            self.meal[i].move(200, 50 + i * 30)

            self.btn1[i] = QPushButton("+", self)
            self.btn1[i].resize(30, 18)
            self.btn1[i].move(270, 48 + i * 30)
            self.btn1[i].clicked.connect(self.button1)

            self.btn2[i] = QPushButton("-", self)
            self.btn2[i].resize(30, 18)
            self.btn2[i].move(300, 48 + i * 30)
            self.btn2[i].clicked.connect(self.button2)

            self.cnt[i] = QLabel("count : " + str(self.count[i]), self)
            self.cnt[i].move(350, 50 + i * 30)

        self.btn2.append(QPushButton("sum", self))
        self.btn2[-1].resize(30, 20)
        self.btn2[-1].move(300, 48 + (self.lng + 1) * 30)
        self.btn2[-1].clicked.connect(self.summ)

        self.check = QPlainTextEdit(self)
        self.check.move(450, 50)
        self.check.resize(350, 400)

    def button1(self):
        send = self.sender()
        for i in range(self.lng):
            if self.btn1[i] == send:
                self.count[i] += 1
                self.cnt[i].setText("count : " + str(self.count[i]))
                self.sum += self.menu.get(self.menul[i])

    def button2(self):
        send = self.sender()
        for i in range(self.lng):
            if self.btn2[i] == send:
                if self.count[i] < 1:
                    break
                else:
                    self.count[i] -= 1
                self.cnt[i].setText("count : " + str(self.count[i]))
                self.sum -= self.menu.get(self.menul[i])

    def summ(self):
        for i in range(self.lng):
            if self.count[i] != 0:
                self.check.appendPlainText(str(self.menul[i]) + " \t\tcount : " + str(
                    self.count[i]) + "\tprice : " + str(self.menu.get(self.menul[i])) + " rub")
        self.check.appendPlainText("\n\n")
        self.check.appendPlainText("Summary \t\t\tprice : " + str(self.sum))
        self.check.setUpdatesEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
