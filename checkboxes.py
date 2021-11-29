import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from ui9 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.setStyleSheet('background: lightgrey;')
        self.checkBox.stateChanged.connect(self.changeText)
        self.checkBox_2.stateChanged.connect(self.turnToRed)
        self.checkBox_3.stateChanged.connect(self.moveToNorth)
        self.checkBox_4.stateChanged.connect(self.reshapeButton)
        self.checkBox_5.stateChanged.connect(self.dissapear)

    def changeText(self, state):
        if state == Qt.Checked:
            self.pushButton.setText("I'm changed")
        else:
            self.pushButton.setText("I'm button")

    def turnToRed(self, state):
        if state == Qt.Checked:
            self.pushButton.setStyleSheet('background: red;')
        else:
            self.pushButton.setStyleSheet('background: lightgrey;')

    def moveToNorth(self, state):
        if state == Qt.Checked:
            self.pushButton.move(190, 0)
        else:
            self.pushButton.move(190, 40)

    def reshapeButton(self, state):
        if state == Qt.Checked:
            self.pushButton.resize(75, 75)
        else:
            self.pushButton.resize(75, 23)

    def dissapear(self, state):
        if state == Qt.Checked:
            self.pushButton.setHidden(True)
        else:
            self.pushButton.setHidden(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
