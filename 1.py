import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5 import QtCore
from ui1 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = "F:/rez.csv"
        self.initUI()
        self.loadData()
        self.findWiner()
        self.fillFilters()

    def initUI(self):
        self.schoolFilter.addItem(None)
        self.classFilter.addItem(None)
        self.schoolFilter.currentIndexChanged.connect(self.applyFilters)
        self.classFilter.currentIndexChanged.connect(self.applyFilters)

    def parseParticipiantInfo(self, elem):
        return tuple(elem.split("-")[2:-1])

    def fillFilters(self):
        schools = set()
        classes = set()
        for row in range(self.tableWidget.rowCount()):
            info = self.parseParticipiantInfo(
                self.tableWidget.item(row, 2).text())

            if info[0] not in schools:
                self.schoolFilter.addItem(info[0])
                schools.add(info[0])

            if info[1] not in classes:
                self.classFilter.addItem(info[1])
                classes.add(info[1])

    def loadData(self, school=None, partClass=None):
        with open(self.fname, encoding="utf-8") as data:
            reader = csv.reader(data, delimiter=',')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)

            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                info = self.parseParticipiantInfo(row[2])

                if school or partClass:
                    for j, elem in enumerate(row):
                        if j in [1, 2, 7]:
                            if ((school == info[0] and partClass == info[1])
                                or (school == info[0] and not partClass)
                                    or (partClass == info[1] and not school)):
                                self.tableWidget.setItem(
                                    i, j, QTableWidgetItem(elem))
                else:
                    for j, elem in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

    def applyFilters(self):
        self.tableWidget.clear()
        self.tableWidget.clear()
        self.loadData(self.schoolFilter.currentText(),
                      self.classFilter.currentText())
        self.tableWidget.sortItems(7, QtCore.Qt.DescendingOrder)
        self.clearEmpties()
        self.setColourToWinner()

    def clearEmpties(self):
        for row in range(self.tableWidget.rowCount() - 1, -1, -1):
            if not self.tableWidget.item(row, 2):
                self.tableWidget.removeRow(row)

        for col in range(self.tableWidget.columnCount() - 1, -1, -1):
            if not self.tableWidget.item(0, col):
                self.tableWidget.removeColumn(col)

    def findWiner(self):
        self.logins0 = []
        self.logins1 = []
        self.logins2 = []
        s = set()
        for row in range(self.tableWidget.rowCount()):
            s.add(self.tableWidget.item(row, 7).text())
        s = list(map(int, s))
        s.sort(reverse=True)
        for row in range(self.tableWidget.rowCount()):
            if str(s[0]) == self.tableWidget.item(row, 7).text():
                self.logins0.append(self.tableWidget.item(row, 2).text())
            if str(s[1]) == self.tableWidget.item(row, 7).text():
                self.logins1.append(self.tableWidget.item(row, 2).text())
            if str(s[2]) == self.tableWidget.item(row, 7).text():
                self.logins2.append(self.tableWidget.item(row, 2).text())

    def setColourToWinner(self):
        if self.schoolFilter.currentText() or self.classFilter.currentText():
            if self.tableWidget.rowCount():
                for row in range(self.tableWidget.rowCount()):
                    if self.tableWidget.item(row, 1).text() in self.logins0:
                        for i in range(3):
                            self.tableWidget.item(
                                row, i).setBackground(QColor("Yellow"))
                    if self.tableWidget.item(row, 1).text() in self.logins1:
                        for i in range(3):
                            self.tableWidget.item(
                                row, i).setBackground(QColor("Grey"))
                    if self.tableWidget.item(row, 1).text() in self.logins2:
                        for i in range(3):
                            self.tableWidget.item(
                                row, i).setBackground(QColor("Orange"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
