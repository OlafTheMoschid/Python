from pytestqt import qtbot
from PyQt5 import QtCore

from checkboxes import Programm

def test_changeText(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    
def test_changeText_turnToRed(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: red;"
    
def test_changeText_turnToRed_moveToNorth(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: red;"
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 0

def test_changeText_turnToRed_moveToNorth_reshape(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: red;"
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 0
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 75
    
def test_changeText_turnToRed_moveToNorth_reshape_dissapear(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_5, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: red;"
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 0
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 75
    assert widget.pushButton.isHidden() == True
    
def test_turnToRed_moveToNorth_reshape(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    assert widget.pushButton.styleSheet() == "background: red;"
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 0
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 75
    
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 40
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 23
    
def test_turnToRed_dissapear(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_5, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.isHidden() == True
    
    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_5, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm button"
    assert widget.pushButton.isHidden() == False
    
def test_changeText_reshape_dissapear(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_5, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 75
    assert widget.pushButton.isHidden() == True
    
    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm button"
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 23
    assert widget.pushButton.isHidden() == True
    
def test_changeText_turnToRed_moveToNorth_reshape_dissapear2(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_5, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: red;"
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 0
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 75
    assert widget.pushButton.isHidden() == True
    
    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_4, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_5, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm button"
    assert widget.pushButton.styleSheet() == "background: lightgrey;"
    assert widget.pushButton.x() == 190 and widget.pushButton.y() == 40
    assert widget.pushButton.width() == 75 and widget.pushButton.height() == 23
    assert widget.pushButton.isHidden() == False
    
def test_changeText_turnToRed2(qtbot):
    widget = Programm()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.checkBox, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: red;"
    qtbot.mouseClick(widget.checkBox_2, QtCore.Qt.LeftButton)
    assert widget.pushButton.text() == "I'm changed"
    assert widget.pushButton.styleSheet() == "background: lightgrey;"