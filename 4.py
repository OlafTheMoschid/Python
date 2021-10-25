import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui4 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionCreate.triggered.connect(self.create)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)

    def open(self):
        fn = QFileDialog.getOpenFileName(
            self, 'Open file', '', "Text files (*.txt)")[0]
        try:
            f = open(fn, 'r+', encoding='utf8')
            self.textBrowser.setText(f.read())
            f.close()
        except:
            pass  # чтобы приложение не закрывалось, если не выбрать файл

    def save(self):
        fn = QFileDialog.getSaveFileName(
            self, 'Save file', '', "Text files (*.txt)")[0]
        try:
            o = open(fn, 'w', encoding='utf8')
            o.write(self.textBrowser.toPlainText())
            o.close()
        except:
            pass  # чтобы приложение не закрывалось, если не выбрать файл

    def create(self):
        self.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
