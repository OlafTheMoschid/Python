import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui6 import Ui_MainWindow

class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.clipboard = QApplication.clipboard()
        self.pushButton.clicked.connect(self.clipboardCopy)
        self.pushButton_2.clicked.connect(self.clipboardPaste)
        
    def clipboardCopy(self):
        self.clipboard.setText(self.textEdit.toPlainText())
 
    def clipboardPaste(self):
        self.textEdit_2.setText(self.clipboard.text())

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
