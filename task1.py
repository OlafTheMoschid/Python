import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QRect, QCoreApplication, QSettings
from ui1 import Ui_MainWindow

ORGANIZATION_NAME = 'Example App'
ORGANIZATION_DOMAIN = 'example.com'
APPLICATION_NAME = 'QSettings program'

SETTINGS_RADIOBUTTON = 'settings/radioButton'
SETTINGS_CHECKBOX = 'settings/checkBox'
SETTINGS_LINEEDIT = 'settings/lineEdit'
SETTINGS_GEOMETRY = 'settings/geometry'
SETTINGS_COUNT = 'settings/count'


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        settings = QSettings()
        check_radioButton = settings.value(
            SETTINGS_RADIOBUTTON, False, type=bool)
        check_checkBox = settings.value(SETTINGS_CHECKBOX, False, type=bool)
        check_lineEdit = settings.value(SETTINGS_LINEEDIT, '', type=str)
        check_geometry = settings.value(
            SETTINGS_GEOMETRY, self.geometry(), QRect)
        check_count = settings.value(SETTINGS_COUNT, 0, type=int)

        self.radioButton.setChecked(check_radioButton)
        self.checkBox.setChecked(check_checkBox)
        self.lineEdit.setText(check_lineEdit)
        self.setGeometry(check_geometry)
        self.count = check_count

        self.radioButton.clicked.connect(self.save_radioButton_settings)
        self.checkBox.clicked.connect(self.save_checkBox_settings)
        self.lineEdit.textEdited.connect(self.save_lineEdit_settings)

        if self.count % 10 == 0 and self.count > 0:
            self.congratz_label()
        else:
            self.label.setText('')

    def save_radioButton_settings(self):
        settings = QSettings()
        settings.setValue(SETTINGS_RADIOBUTTON, self.radioButton.isChecked())
        settings.sync()

    def save_checkBox_settings(self):
        settings = QSettings()
        settings.setValue(SETTINGS_CHECKBOX, self.checkBox.isChecked())
        settings.sync()

    def save_lineEdit_settings(self):
        settings = QSettings()
        settings.setValue(SETTINGS_LINEEDIT, self.lineEdit.text())
        settings.sync()

    def congratz_label(self):
        self.label.setText(
            "Congratulations!\nYou opened this application \n10 times in a row!\nWell done!")

    def closeEvent(self, event):
        self.check_geometry = self.geometry()
        settings = QSettings()
        settings.setValue(SETTINGS_GEOMETRY, self.geometry())
        settings.setValue(SETTINGS_COUNT, self.count + 1)
        settings.sync()


if __name__ == '__main__':
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
