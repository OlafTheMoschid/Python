from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_red = QtWidgets.QPushButton(self.centralwidget)
        self.btn_red.setGeometry(QtCore.QRect(550, 20, 81, 23))
        self.btn_red.setObjectName("btn_red")
        self.btn_green = QtWidgets.QPushButton(self.centralwidget)
        self.btn_green.setGeometry(QtCore.QRect(550, 50, 81, 23))
        self.btn_green.setObjectName("btn_green")
        self.btn_blue = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blue.setGeometry(QtCore.QRect(550, 80, 81, 23))
        self.btn_blue.setObjectName("btn_blue")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(650, 30, 81, 23))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(650, 70, 81, 23))
        self.btn_right.setObjectName("btn_right")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_red.setText(_translate("MainWindow", "Red Channel"))
        self.btn_green.setText(_translate("MainWindow", "Green Channel"))
        self.btn_blue.setText(_translate("MainWindow", "Blue Channel"))
        self.btn_left.setText(_translate("MainWindow", "Rotate on left"))
        self.btn_right.setText(_translate("MainWindow", "Rotate on right"))
