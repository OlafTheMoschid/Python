import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ui6 import Ui_MainWindow


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)
        self.pushButton_4.clicked.connect(self.run4)
        self.pushButton_5.clicked.connect(self.run5)
        self.pushButton_6.clicked.connect(self.run6)
        self.pushButton_7.clicked.connect(self.run7)

    def initUI(self):
        self.fname = QFileDialog.getExistingDirectory(
            self, "Choise the directory", "")
        self.player = QMediaPlayer()
        self.player.setVolume(25)

    def run1(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '1.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()

    def run2(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '2.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()

    def run3(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '3.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()

    def run4(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '4.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()

    def run5(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '5.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()

    def run6(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '6.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()

    def run7(self):
        self.player.stop()
        media = QUrl.fromLocalFile(self.fname + '/' + '7.mp3')
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
