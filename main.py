import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QSettings, QEvent, QCoreApplication, QRect
from mainUi import Ui_MainWindow

ORGANIZATION_NAME = 'PlayerApp.inc'
ORGANIZATION_DOMAIN = 'player.com'
APPLICATION_NAME = 'Player App'

SETTINGS_GEOMETRY = 'settings/geometry'
SETTINGS_FILE_NAME_LABEL = 'settings/labels/file_name'
SETTINGS_TRACK_POSITION = 'settings/track/position'
SETTINGS_TRACK_VOLUME = 'settings/track/volume'


class Programm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.audioTypes = ['mp3', 'ogg', 'wav']
        self.progressBar.setStyleSheet(
            "#progressBar::chunk {background-color: #a29aa0;}")

        self.act_open.triggered.connect(self.openFile)

        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.viewport().installEventFilter(self)
        types = ['text/uri-list']
        types.extend(self.tableWidget.mimeTypes())
        self.tableWidget.mimeTypes = lambda: types

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setHorizontalHeaderLabels(['file', 'name'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.cellDoubleClicked.connect(self.playFile)
        self.btn_stop.clicked.connect(self.stop_btn)
        self.btn_pause.clicked.connect(self.pause_btn)
        self.btn_play.clicked.connect(self.play_btn)
        self.btn_next.clicked.connect(self.next_btn)
        self.btn_prev.clicked.connect(self.prev_btn)
        self.sld_volume.valueChanged[int].connect(self.volumeChanging)
        self.sld_track.valueChanged[int].connect(self.trackPositionChanging)

        self.player = QMediaPlayer()
        self.player.durationChanged.connect(self.trackDuration)
        self.player.positionChanged.connect(self.trackPosition)

        settings = QSettings()
        check_geometry = settings.value(
            SETTINGS_GEOMETRY, self.geometry(), QRect)
        check_lbl_file = settings.value(SETTINGS_FILE_NAME_LABEL, '', type=str)
        check_track_position = settings.value(
            SETTINGS_TRACK_POSITION, 0, type=int)
        check_track_volume = settings.value(SETTINGS_TRACK_VOLUME, 1, type=int)

        self.setGeometry(check_geometry)
        self.lbl_name.setText(check_lbl_file)

        self.player.setVolume(check_track_volume)
        self.sld_volume.setValue(check_track_volume)
        self.player.setPosition(check_track_position)
        self.sld_track.setValue(check_track_position)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.removeFromTable()
            self.next_btn()

    def openFile(self):
        self.fname = QFileDialog.getOpenFileName(
            self, 'Choise the audio file', '', 'mp3 (*.mp3);;All files (*)')
        self.addToTable(self.fname[0])

    def eventFilter(self, source, event):
        if (event.type() == QEvent.Drop and
                event.mimeData().hasUrls()):
            for url in event.mimeData().urls():
                self.addToTable(url.toLocalFile())
            return True
        return super().eventFilter(source, event)

    def addToTable(self, name):
        if name.split('/')[-1][-3:] not in self.audioTypes:
            return
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        buf = QTableWidgetItem(name)
        buf.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        buf1 = QTableWidgetItem(name.split('/')[-1])
        buf1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, buf)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, buf1)

    def removeFromTable(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def playFile(self, row, column):
        settings = QSettings()
        self.lbl_name.setText(self.tableWidget.item(row, 1).text())
        media = QUrl.fromLocalFile(self.tableWidget.item(row, 0).text())
        content = QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()
        settings.setValue(SETTINGS_FILE_NAME_LABEL, self.lbl_name.text())
        settings.sync()

    def stop_btn(self):
        self.player.stop()

    def pause_btn(self):
        self.player.pause()

    def play_btn(self):
        self.player.play()

    def next_btn(self):
        if self.tableWidget.rowCount() < 2 or self.tableWidget.currentRow() == self.tableWidget.rowCount() - 1:
            return
        self.tableWidget.setCurrentCell(self.tableWidget.currentRow() + 1, 1)
        self.playFile(self.tableWidget.currentRow(), 0)

    def prev_btn(self):
        if self.tableWidget.rowCount() < 2 or self.tableWidget.currentRow() == 0:
            return
        self.tableWidget.setCurrentCell(self.tableWidget.currentRow() - 1, 1)
        self.playFile(self.tableWidget.currentRow(), 0)

    def volumeChanging(self, value):
        settings = QSettings()
        self.player.setVolume(value)
        settings.setValue(SETTINGS_TRACK_VOLUME, value)
        settings.sync()

    def trackPositionChanging(self, value):
        settings = QSettings()
        self.player.setPosition(value)
        settings.setValue(SETTINGS_TRACK_POSITION, value)
        settings.sync()

    def trackDuration(self, duration):
        self.sld_track.setMaximum(duration)
        self.progressBar.setMaximum(duration)
        m = duration // 1000 // 60
        s = duration // 1000 % 60
        self.lbl_time_2.setText(f'- {m:>1}:{s:0>2}')

    def trackPosition(self, position):
        self.progressBar.setValue(position)
        self.sld_track.setValue(position)
        m = position // 1000 // 60
        s = position // 1000 % 60
        self.lbl_time.setText(f'{m:>1}:{s:0>2}')

    def closeEvent(self, event):
        self.check_geometry = self.geometry()
        settings = QSettings()
        settings.setValue(SETTINGS_GEOMETRY, self.geometry())
        settings.sync()


if __name__ == '__main__':
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QApplication(sys.argv)
    prog = Programm()
    prog.show()
    sys.exit(app.exec())
