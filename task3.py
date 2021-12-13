import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui3 import Ui_MainWindow

class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, QDragEnterEvent):
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()
 
    def dropEvent(self, QDropEvent):
        txt_path = QDropEvent.mimeData().text().replace('file:///', '')
        if txt_path[-3:] == 'txt':
            f = open(txt_path, mode="r", encoding="utf-8")
            self.textBrowser.setText(f.read())
        else:
            self.textBrowser.setText('Wrong file type. Only .txt files can be loaded!')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
