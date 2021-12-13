from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QLabel, QListView
import sys

class ListWidget1(QListWidget):
    def dropEvent(self, e):
        temp = e.source().currentItem()
        self.addItem(temp.text())
        e.source().takeItem(e.source().row(e.source().currentItem()))   
    
class ListWidget(QListWidget):
    def dragEnterEvent(self, e):
        if e.source() != self and self.count() < 4:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        temp = e.source().currentItem()
        self.addItem(temp.text())
        e.source().takeItem(e.source().row(e.source().currentItem()))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 300)

        self.myListWidget1 = ListWidget1()
        self.myListWidget2 = ListWidget()

        self.myListWidget1.setViewMode(QListView.IconMode)
        self.myListWidget2.setViewMode(QListView.ListMode)

        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        self.appLayout = QVBoxLayout()
        self.appLayout.setSpacing(10)
        
        self.appLayout.addWidget(self.myListWidget1)
        self.appLayout.addWidget(self.myListWidget2)

        listWidgetItem1 = QListWidgetItem("Item1")
        listWidgetItem2 = QListWidgetItem("Item2")
        listWidgetItem3 = QListWidgetItem("Item3")
        listWidgetItem4 = QListWidgetItem("Item4")
        listWidgetItem5 = QListWidgetItem("Item5")
        listWidgetItem6 = QListWidgetItem("Item6")
        listWidgetItem7 = QListWidgetItem("Item7")
        self.myListWidget1.insertItem(1, listWidgetItem1)
        self.myListWidget1.insertItem(2, listWidgetItem2)
        self.myListWidget1.insertItem(3, listWidgetItem3)
        self.myListWidget1.insertItem(4, listWidgetItem4)
        self.myListWidget1.insertItem(5, listWidgetItem5)
        self.myListWidget1.insertItem(6, listWidgetItem6)
        self.myListWidget1.insertItem(7, listWidgetItem7)
        
        if self.myListWidget2.count() > 4:
            self.myListWidget2.setAcceptDrops(False)
        
        self.setLayout(self.appLayout)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
