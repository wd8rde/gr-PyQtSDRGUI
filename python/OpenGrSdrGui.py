# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opengrsdrgui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenGRSDR(object):
    def setupUi(self, OpenGRSDR):
        OpenGRSDR.setObjectName("OpenGRSDR")
        OpenGRSDR.setWindowModality(QtCore.Qt.WindowModal)
        OpenGRSDR.resize(1582, 569)
        OpenGRSDR.setMinimumSize(QtCore.QSize(900, 300))
        OpenGRSDR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        OpenGRSDR.setFont(font)
        OpenGRSDR.setStyleSheet("QWidget { \n"
"background: #323232;\n"
"color: #E5E5E5;\n"
"border: 0px;\n"
"}\n"
"/***********************************************/\n"
"QPushButton {\n"
"border: 1px solid #000000;\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #333333,  stop: 1 #2e2e2e);\n"
"color: #EBEBEB;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #c2c2c2, stop:0.5 #959595, stop:0.55 #959595, stop: 1 #707070);\n"
"}\n"
"QPushButton:disabled {\n"
"color: #787878;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"}\n"
"QPushButton:flat {\n"
"border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton::checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.55 #366436, stop: 1 #4e9d4e);\n"
"}\n"
"QPushButton:default {\n"
"border-color: navy; /* make the default button prominent */\n"
"}\n"
"/***********************************************/\n"
"QSlider::groove:horizontal {\n"
"background-color: #141414;\n"
"position: absolute; /* абсолютная позиция в 4px слева и справа от виджета. установка полей виджета также будет работать... */\n"
"height: 15px;\n"
"left: 2px; right: 2px;\n"
"border: 0px;\n"
"margin: 0px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"width: 28 px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BFBFBF, stop: 1 #707070);\n"
"border: 0px;\n"
"margin: 1px 1;\n"
"border-radius: 1px;\n"
"}\n"
"/***********************************************/\n"
"QToolButton { /* all types of tool button */ \n"
"border: 1px solid #000000;\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #333333,  stop: 1 #2e2e2e);\n"
"color: #EBEBEB;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #c2c2c2, stop:0.5 #959595, stop:0.55 #959595, stop: 1 #707070);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.55 #366436, stop: 1 #4e9d4e);\n"
"}\n"
"/***********************************************/\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"    background-color: rgb(40, 40, 40, 0);\n"
"    border-color: rgb(100, 100, 100);\n"
"    margin: 2px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(146, 146, 146);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:images/checkbutton_unchacked.png);\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(146, 146, 146);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(:images/checkbutton_unchacked.png);\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(:images/checkbutton_unchacked.png);\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    image: url(:images/checkbutton_unchacked_disable.png);\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"    border: 1px solid;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-color: rgb(80, 80, 80);\n"
"}\n"
"/***********************************************/\n"
"QSpinBox{\n"
"    background-color: rgb(52, 52, 52);\n"
"    border: 1px solid;\n"
"    border-color: black;\n"
"    color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(70, 150, 70);\n"
"}\n"
"QSpinBox:disabled{\n"
"    background-color: rgb(52, 52, 52);\n"
"    border: 1px solid;\n"
"    border-color: rgb(160, 160, 160);\n"
"    min-width: 55px;\n"
"    min-height: 18px;\n"
"    color: rgb(160, 160, 160);\n"
"    selection-background-color: rgb(70, 150, 70);\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"    image: url(:images/arrows/arrow-up.png);\n"
"    border-width: 1px;\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"    image: url(:images/arrows/arrow-up.png);\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; \n"
"    width: 16px;\n"
"    image: url(:images/arrows/arrow-down.png);\n"
"    border-width: 1px;\n"
"    border-top-width: 0;\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"    image: url(:images/arrows/arrow-down.png);\n"
"}\n"
"/***pbVoicePlay*********************************/\n"
"QPushButton#pbVoicePlay {\n"
"border: 1px solid #000000;\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #333333,  stop: 1 #2e2e2e);\n"
"color: #EBEBEB;\n"
"image: url(://images/play_unpress.png);\n"
"}\n"
"QPushButton#pbVoicePlay:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #c2c2c2, stop:0.5 #959595, stop:0.55 #959595, stop: 1 #707070);\n"
"image: url(://images/play_unpress.png);\n"
"}\n"
"QPushButton#pbVoicePlay:disabled {\n"
"color: #787878;\n"
"image: url(://images/play_disable.png);\n"
"}\n"
"QPushButton#pbVoicePlay:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"image: url(://images/play_press.png);\n"
"}\n"
"QPushButton#pbVoicePlay:pressed:hover {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"image: url(://images/play_press.png);\n"
"}\n"
"QPushButton#pbVoicePlay::checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.55 #366436, stop: 1 #4e9d4e);\n"
"image: url(://images/play_press.png);\n"
"}\n"
"/***pbVoiceRec**********************************/\n"
"QPushButton#pbVoiceRec {\n"
"border: 1px solid #000000;\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #333333,  stop: 1 #2e2e2e);\n"
"color: #EBEBEB;\n"
"image: url(://images/rec_unpress.png);\n"
"}\n"
"QPushButton#pbVoiceRec:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #c2c2c2, stop:0.5 #959595, stop:0.55 #959595, stop: 1 #707070);\n"
"image: url(://images/rec_unpress.png);\n"
"}\n"
"QPushButton#pbVoiceRec:disabled {\n"
"color: #787878;\n"
"image: url(://images/rec_disable.png);\n"
"}\n"
"QPushButton#pbVoiceRec:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"image: url(://images/rec_press.png);\n"
"}\n"
"QPushButton#pbVoiceRec:pressed:hover {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"image: url(://images/rec_press.png);\n"
"}\n"
"QPushButton#pbVoiceRec::checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.55 #366436, stop: 1 #4e9d4e);\n"
"image: url(://images/rec_press.png);\n"
"}\n"
"/***********************************************/\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenGRSDR)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wdgTopPanel = QtWidgets.QWidget(OpenGRSDR)
        self.wdgTopPanel.setMinimumSize(QtCore.QSize(0, 24))
        self.wdgTopPanel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.wdgTopPanel.setStyleSheet("QWidget {\n"
"        background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #616161, stop:0.5 #323232, stop: 1 #323232);\n"
"}\n"
"\n"
"QPushButton {\n"
"border: 1px solid #000000;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"color: #EBEBEB;\n"
"}\n"
"\n"
"QPushButton#pbTime {\n"
"border: 0px;\n"
"background-color: transparent;\n"
"color: #EBEBEB;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton#pbTime:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #c2c2c2, stop:0.5 #959595, stop:0.55 #959595, stop: 1 #707070);\n"
"}\n"
"QPushButton:pressed, QPushButton#pbTime:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"}\n"
"\n"
"\n"
"QPushButton#pbStart{\n"
"    border: 1px solid;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(235, 235, 235);\n"
"}\n"
"QPushButton#pbStart:disabled{\n"
"    border: 1px solid;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(120, 120, 120);\n"
"}\n"
"QPushButton#pbStart:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(109, 109, 109, 255), stop:1 rgba(194, 194, 194, 255));\n"
"}\n"
"QPushButton#pbStart:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(129, 44, 44, 255), stop:0.6875 rgba(149, 44, 44, 255), stop:1 rgba(225, 45, 45, 255));\n"
"}\n"
"QPushButton#pbStart:pressed:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(129, 44, 44, 255), stop:0.6875 rgba(149, 44, 44, 255), stop:1 rgba(225, 45, 45, 255));\n"
"}\n"
"QPushButton#pbStart::checked{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(129, 44, 44, 255), stop:0.6875 rgba(149, 44, 44, 255), stop:1 rgba(225, 45, 45, 255));\n"
"}\n"
"QPushButton#pbStart::checked:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(129, 44, 44, 255), stop:0.6875 rgba(149, 44, 44, 255), stop:1 rgba(225, 45, 45, 255));\n"
"}\n"
"\n"
"")
        self.wdgTopPanel.setObjectName("wdgTopPanel")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.wdgTopPanel)
        self.horizontalLayout_3.setContentsMargins(3, 0, 2, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbStart = QtWidgets.QPushButton(self.wdgTopPanel)
        self.pbStart.setMinimumSize(QtCore.QSize(60, 20))
        self.pbStart.setMaximumSize(QtCore.QSize(60, 20))
        self.pbStart.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/power-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbStart.setIcon(icon)
        self.pbStart.setCheckable(True)
        self.pbStart.setObjectName("pbStart")
        self.horizontalLayout_3.addWidget(self.pbStart)
        self.lbVersion = QtWidgets.QLabel(self.wdgTopPanel)
        self.lbVersion.setObjectName("lbVersion")
        self.horizontalLayout_3.addWidget(self.lbVersion)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lbDate = QtWidgets.QLabel(self.wdgTopPanel)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbDate.setFont(font)
        self.lbDate.setObjectName("lbDate")
        self.horizontalLayout_3.addWidget(self.lbDate)
        self.pbTime = QtWidgets.QPushButton(self.wdgTopPanel)
        self.pbTime.setMinimumSize(QtCore.QSize(100, 18))
        self.pbTime.setMaximumSize(QtCore.QSize(100, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pbTime.setFont(font)
        self.pbTime.setCheckable(False)
        self.pbTime.setObjectName("pbTime")
        self.horizontalLayout_3.addWidget(self.pbTime)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pbCwMacro = QtWidgets.QPushButton(self.wdgTopPanel)
        self.pbCwMacro.setEnabled(True)
        self.pbCwMacro.setMinimumSize(QtCore.QSize(60, 18))
        self.pbCwMacro.setMaximumSize(QtCore.QSize(60, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbCwMacro.setFont(font)
        self.pbCwMacro.setCheckable(False)
        self.pbCwMacro.setObjectName("pbCwMacro")
        self.horizontalLayout_3.addWidget(self.pbCwMacro)
        self.pbOptions = QtWidgets.QPushButton(self.wdgTopPanel)
        self.pbOptions.setMinimumSize(QtCore.QSize(60, 18))
        self.pbOptions.setMaximumSize(QtCore.QSize(60, 18))
        self.pbOptions.setCheckable(False)
        self.pbOptions.setObjectName("pbOptions")
        self.horizontalLayout_3.addWidget(self.pbOptions)
        self.pbAbout = QtWidgets.QPushButton(self.wdgTopPanel)
        self.pbAbout.setMinimumSize(QtCore.QSize(60, 18))
        self.pbAbout.setMaximumSize(QtCore.QSize(60, 18))
        self.pbAbout.setCheckable(False)
        self.pbAbout.setObjectName("pbAbout")
        self.horizontalLayout_3.addWidget(self.pbAbout)
        self.widget_14 = QtWidgets.QWidget(self.wdgTopPanel)
        self.widget_14.setMinimumSize(QtCore.QSize(22, 0))
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_3.addWidget(self.widget_14)
        self.verticalLayout.addWidget(self.wdgTopPanel)
        self.widget_3 = QtWidgets.QWidget(OpenGRSDR)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(2, 0, 1, 1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setMinimumSize(QtCore.QSize(79, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(120, 40))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setContentsMargins(1, 0, 1, 0)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 1, 1, 1)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.pbTone = QtWidgets.QPushButton(self.widget_7)
        self.pbTone.setMinimumSize(QtCore.QSize(0, 18))
        self.pbTone.setMaximumSize(QtCore.QSize(37, 21))
        self.pbTone.setCheckable(True)
        self.pbTone.setObjectName("pbTone")
        self.gridLayout.addWidget(self.pbTone, 0, 2, 1, 1)
        self.pbMox = QtWidgets.QPushButton(self.widget_7)
        self.pbMox.setEnabled(False)
        self.pbMox.setMinimumSize(QtCore.QSize(0, 18))
        self.pbMox.setMaximumSize(QtCore.QSize(37, 21))
        self.pbMox.setCheckable(True)
        self.pbMox.setObjectName("pbMox")
        self.gridLayout.addWidget(self.pbMox, 0, 1, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setMinimumSize(QtCore.QSize(120, 0))
        self.widget_8.setMaximumSize(QtCore.QSize(120, 40))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setContentsMargins(1, 0, 1, 0)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 1, 1, 1)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pbMute = QtWidgets.QPushButton(self.widget_8)
        self.pbMute.setMinimumSize(QtCore.QSize(0, 18))
        self.pbMute.setMaximumSize(QtCore.QSize(37, 21))
        self.pbMute.setCheckable(True)
        self.pbMute.setObjectName("pbMute")
        self.gridLayout_2.addWidget(self.pbMute, 1, 1, 1, 1)
        self.pbVoicePlay = QtWidgets.QPushButton(self.widget_8)
        self.pbVoicePlay.setEnabled(False)
        self.pbVoicePlay.setMinimumSize(QtCore.QSize(0, 18))
        self.pbVoicePlay.setMaximumSize(QtCore.QSize(37, 21))
        self.pbVoicePlay.setCheckable(True)
        self.pbVoicePlay.setObjectName("pbVoicePlay")
        self.gridLayout_2.addWidget(self.pbVoicePlay, 1, 3, 1, 1)
        self.pbVoiceRec = QtWidgets.QPushButton(self.widget_8)
        self.pbVoiceRec.setEnabled(False)
        self.pbVoiceRec.setMinimumSize(QtCore.QSize(0, 18))
        self.pbVoiceRec.setMaximumSize(QtCore.QSize(37, 21))
        self.pbVoiceRec.setCheckable(True)
        self.pbVoiceRec.setObjectName("pbVoiceRec")
        self.gridLayout_2.addWidget(self.pbVoiceRec, 1, 4, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addWidget(self.widget_8)
        self.widget_13 = QtWidgets.QWidget(self.widget_3)
        self.widget_13.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_13.setMaximumSize(QtCore.QSize(230, 16777215))
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setContentsMargins(1, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pbAtten = QtWidgets.QPushButton(self.widget_13)
        self.pbAtten.setMinimumSize(QtCore.QSize(0, 18))
        self.pbAtten.setMaximumSize(QtCore.QSize(60, 21))
        self.pbAtten.setCheckable(True)
        self.pbAtten.setChecked(False)
        self.pbAtten.setObjectName("pbAtten")
        self.horizontalLayout_14.addWidget(self.pbAtten)
        self.pbPreamp = QtWidgets.QToolButton(self.widget_13)
        self.pbPreamp.setMinimumSize(QtCore.QSize(50, 18))
        self.pbPreamp.setMaximumSize(QtCore.QSize(80, 21))
        self.pbPreamp.setCheckable(True)
        self.pbPreamp.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.pbPreamp.setObjectName("pbPreamp")
        self.horizontalLayout_14.addWidget(self.pbPreamp)
        self.pbPa = QtWidgets.QPushButton(self.widget_13)
        self.pbPa.setMinimumSize(QtCore.QSize(0, 18))
        self.pbPa.setMaximumSize(QtCore.QSize(90, 21))
        self.pbPa.setCheckable(True)
        self.pbPa.setChecked(False)
        self.pbPa.setObjectName("pbPa")
        self.horizontalLayout_14.addWidget(self.pbPa)
        self.horizontalLayout_2.addWidget(self.widget_13)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.swVolume = QtWidgets.QStackedWidget(self.widget_3)
        self.swVolume.setObjectName("swVolume")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.page_11)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.slVol = QtWidgets.QSlider(self.page_11)
        self.slVol.setMouseTracking(True)
        self.slVol.setMaximum(100)
        self.slVol.setProperty("value", 50)
        self.slVol.setOrientation(QtCore.Qt.Horizontal)
        self.slVol.setObjectName("slVol")
        self.horizontalLayout_15.addWidget(self.slVol)
        self.swVolume.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.page_12)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.slMonVol = QtWidgets.QSlider(self.page_12)
        self.slMonVol.setMouseTracking(True)
        self.slMonVol.setMinimum(1)
        self.slMonVol.setMaximum(60)
        self.slMonVol.setPageStep(1)
        self.slMonVol.setProperty("value", 30)
        self.slMonVol.setOrientation(QtCore.Qt.Horizontal)
        self.slMonVol.setObjectName("slMonVol")
        self.horizontalLayout_16.addWidget(self.slMonVol)
        self.swVolume.addWidget(self.page_12)
        self.horizontalLayout_2.addWidget(self.swVolume)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.slAgc = QtWidgets.QSlider(self.widget_3)
        self.slAgc.setMinimumSize(QtCore.QSize(0, 19))
        self.slAgc.setMouseTracking(True)
        self.slAgc.setMinimum(-20)
        self.slAgc.setMaximum(120)
        self.slAgc.setProperty("value", 85)
        self.slAgc.setOrientation(QtCore.Qt.Horizontal)
        self.slAgc.setObjectName("slAgc")
        self.horizontalLayout_2.addWidget(self.slAgc)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.slDrive = QtWidgets.QSlider(self.widget_3)
        self.slDrive.setMouseTracking(True)
        self.slDrive.setMaximum(10000)
        self.slDrive.setOrientation(QtCore.Qt.Horizontal)
        self.slDrive.setObjectName("slDrive")
        self.horizontalLayout_2.addWidget(self.slDrive)
        self.swMicSpeed = QtWidgets.QStackedWidget(self.widget_3)
        self.swMicSpeed.setObjectName("swMicSpeed")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.page_9)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbMic = QtWidgets.QLabel(self.page_9)
        self.lbMic.setObjectName("lbMic")
        self.horizontalLayout_12.addWidget(self.lbMic)
        self.slMic = QtWidgets.QSlider(self.page_9)
        self.slMic.setMouseTracking(True)
        self.slMic.setMaximum(70)
        self.slMic.setPageStep(1)
        self.slMic.setProperty("value", 10)
        self.slMic.setOrientation(QtCore.Qt.Horizontal)
        self.slMic.setObjectName("slMic")
        self.horizontalLayout_12.addWidget(self.slMic)
        self.swMicSpeed.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.page_10)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_20 = QtWidgets.QLabel(self.page_10)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_13.addWidget(self.label_20)
        self.slSpeed = QtWidgets.QSlider(self.page_10)
        self.slSpeed.setMouseTracking(True)
        self.slSpeed.setMinimum(1)
        self.slSpeed.setMaximum(60)
        self.slSpeed.setPageStep(1)
        self.slSpeed.setProperty("value", 30)
        self.slSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.slSpeed.setObjectName("slSpeed")
        self.horizontalLayout_13.addWidget(self.slSpeed)
        self.sbSWSpeed = QtWidgets.QSpinBox(self.page_10)
        self.sbSWSpeed.setMinimumSize(QtCore.QSize(0, 20))
        self.sbSWSpeed.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sbSWSpeed.setStyleSheet("QWidget { \n"
"  background: #343946;\n"
"border: 1px solid #0e0e0e;\n"
"color: #E5E5E5;\n"
"}\n"
"")
        self.sbSWSpeed.setFrame(True)
        self.sbSWSpeed.setMinimum(1)
        self.sbSWSpeed.setMaximum(60)
        self.sbSWSpeed.setProperty("value", 25)
        self.sbSWSpeed.setObjectName("sbSWSpeed")
        self.horizontalLayout_13.addWidget(self.sbSWSpeed)
        self.swMicSpeed.addWidget(self.page_10)
        self.horizontalLayout_2.addWidget(self.swMicSpeed)
        self.pbAutoFreqMaxLevel = QtWidgets.QPushButton(self.widget_3)
        self.pbAutoFreqMaxLevel.setMinimumSize(QtCore.QSize(35, 18))
        self.pbAutoFreqMaxLevel.setMaximumSize(QtCore.QSize(16777215, 21))
        self.pbAutoFreqMaxLevel.setObjectName("pbAutoFreqMaxLevel")
        self.horizontalLayout_2.addWidget(self.pbAutoFreqMaxLevel)
        self.cbPanInfo = QtWidgets.QCheckBox(self.widget_3)
        self.cbPanInfo.setChecked(True)
        self.cbPanInfo.setObjectName("cbPanInfo")
        self.horizontalLayout_2.addWidget(self.cbPanInfo)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(OpenGRSDR)
        self.widget.setMinimumSize(QtCore.QSize(0, 18))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(500, 40))
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(1, 0, 1, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pbAM = QtWidgets.QPushButton(self.widget_5)
        self.pbAM.setMinimumSize(QtCore.QSize(0, 18))
        self.pbAM.setMaximumSize(QtCore.QSize(80, 21))
        self.pbAM.setStyleSheet("")
        self.pbAM.setCheckable(True)
        self.pbAM.setAutoExclusive(True)
        self.pbAM.setObjectName("pbAM")
        self.gridLayout_3.addWidget(self.pbAM, 0, 0, 1, 1)
        self.pbSAM = QtWidgets.QPushButton(self.widget_5)
        self.pbSAM.setMinimumSize(QtCore.QSize(0, 18))
        self.pbSAM.setMaximumSize(QtCore.QSize(80, 21))
        self.pbSAM.setStyleSheet("Synchronus Amplitude Modulation")
        self.pbSAM.setCheckable(True)
        self.pbSAM.setAutoExclusive(True)
        self.pbSAM.setObjectName("pbSAM")
        self.gridLayout_3.addWidget(self.pbSAM, 0, 1, 1, 1)
        self.pbFMN = QtWidgets.QPushButton(self.widget_5)
        self.pbFMN.setMinimumSize(QtCore.QSize(0, 18))
        self.pbFMN.setMaximumSize(QtCore.QSize(80, 21))
        self.pbFMN.setStyleSheet("Frequency Modulation Narrow")
        self.pbFMN.setCheckable(True)
        self.pbFMN.setAutoExclusive(True)
        self.pbFMN.setObjectName("pbFMN")
        self.gridLayout_3.addWidget(self.pbFMN, 0, 10, 1, 1)
        self.pbUSB = QtWidgets.QPushButton(self.widget_5)
        self.pbUSB.setMinimumSize(QtCore.QSize(0, 18))
        self.pbUSB.setMaximumSize(QtCore.QSize(80, 21))
        self.pbUSB.setStyleSheet("")
        self.pbUSB.setCheckable(True)
        self.pbUSB.setAutoExclusive(True)
        self.pbUSB.setObjectName("pbUSB")
        self.gridLayout_3.addWidget(self.pbUSB, 0, 4, 1, 1)
        self.pbDIGU = QtWidgets.QPushButton(self.widget_5)
        self.pbDIGU.setMinimumSize(QtCore.QSize(0, 18))
        self.pbDIGU.setMaximumSize(QtCore.QSize(80, 21))
        self.pbDIGU.setStyleSheet("Digital Mode Upper Side Band")
        self.pbDIGU.setCheckable(True)
        self.pbDIGU.setAutoExclusive(True)
        self.pbDIGU.setObjectName("pbDIGU")
        self.gridLayout_3.addWidget(self.pbDIGU, 0, 15, 1, 1)
        self.pbDRM = QtWidgets.QPushButton(self.widget_5)
        self.pbDRM.setMinimumSize(QtCore.QSize(0, 18))
        self.pbDRM.setMaximumSize(QtCore.QSize(80, 21))
        self.pbDRM.setStyleSheet("Digital Radio Mondiale (Filtered only)")
        self.pbDRM.setCheckable(True)
        self.pbDRM.setAutoExclusive(True)
        self.pbDRM.setObjectName("pbDRM")
        self.gridLayout_3.addWidget(self.pbDRM, 0, 16, 1, 1)
        self.pbSPEC = QtWidgets.QPushButton(self.widget_5)
        self.pbSPEC.setMinimumSize(QtCore.QSize(0, 18))
        self.pbSPEC.setMaximumSize(QtCore.QSize(80, 21))
        self.pbSPEC.setStyleSheet("Spectrum Mode")
        self.pbSPEC.setCheckable(True)
        self.pbSPEC.setAutoExclusive(True)
        self.pbSPEC.setObjectName("pbSPEC")
        self.gridLayout_3.addWidget(self.pbSPEC, 0, 13, 1, 1)
        self.pbDIGL = QtWidgets.QPushButton(self.widget_5)
        self.pbDIGL.setMinimumSize(QtCore.QSize(0, 18))
        self.pbDIGL.setMaximumSize(QtCore.QSize(80, 21))
        self.pbDIGL.setStyleSheet("Digital Mode Lower Side Band")
        self.pbDIGL.setCheckable(True)
        self.pbDIGL.setAutoExclusive(True)
        self.pbDIGL.setObjectName("pbDIGL")
        self.gridLayout_3.addWidget(self.pbDIGL, 0, 14, 1, 1)
        self.pbCWU = QtWidgets.QPushButton(self.widget_5)
        self.pbCWU.setMinimumSize(QtCore.QSize(0, 18))
        self.pbCWU.setMaximumSize(QtCore.QSize(80, 21))
        self.pbCWU.setStyleSheet("")
        self.pbCWU.setCheckable(True)
        self.pbCWU.setAutoExclusive(True)
        self.pbCWU.setObjectName("pbCWU")
        self.gridLayout_3.addWidget(self.pbCWU, 0, 6, 1, 1)
        self.pbCWL = QtWidgets.QPushButton(self.widget_5)
        self.pbCWL.setMinimumSize(QtCore.QSize(0, 18))
        self.pbCWL.setMaximumSize(QtCore.QSize(80, 21))
        self.pbCWL.setStyleSheet("")
        self.pbCWL.setCheckable(True)
        self.pbCWL.setAutoExclusive(True)
        self.pbCWL.setObjectName("pbCWL")
        self.gridLayout_3.addWidget(self.pbCWL, 0, 5, 1, 1)
        self.pbDSB = QtWidgets.QPushButton(self.widget_5)
        self.pbDSB.setMinimumSize(QtCore.QSize(0, 18))
        self.pbDSB.setMaximumSize(QtCore.QSize(80, 21))
        self.pbDSB.setStyleSheet("")
        self.pbDSB.setCheckable(True)
        self.pbDSB.setAutoExclusive(True)
        self.pbDSB.setObjectName("pbDSB")
        self.gridLayout_3.addWidget(self.pbDSB, 0, 2, 1, 1)
        self.pbLSB = QtWidgets.QPushButton(self.widget_5)
        self.pbLSB.setMinimumSize(QtCore.QSize(0, 18))
        self.pbLSB.setMaximumSize(QtCore.QSize(80, 21))
        self.pbLSB.setStyleSheet("")
        self.pbLSB.setCheckable(True)
        self.pbLSB.setChecked(True)
        self.pbLSB.setAutoExclusive(True)
        self.pbLSB.setObjectName("pbLSB")
        self.gridLayout_3.addWidget(self.pbLSB, 0, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout.addWidget(self.widget_5)
        self.groupBox_band = QtWidgets.QGroupBox(self.widget)
        self.groupBox_band.setEnabled(True)
        self.groupBox_band.setMinimumSize(QtCore.QSize(260, 0))
        self.groupBox_band.setMaximumSize(QtCore.QSize(20000, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.groupBox_band.setFont(font)
        self.groupBox_band.setStyleSheet("")
        self.groupBox_band.setObjectName("groupBox_band")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_band)
        self.horizontalLayout_8.setContentsMargins(1, 0, 1, 0)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb15M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb15M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb15M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb15M.setCheckable(True)
        self.pb15M.setAutoExclusive(True)
        self.pb15M.setObjectName("pb15M")
        self.gridLayout_4.addWidget(self.pb15M, 0, 6, 1, 1)
        self.pb17M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb17M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb17M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb17M.setCheckable(True)
        self.pb17M.setAutoExclusive(True)
        self.pb17M.setObjectName("pb17M")
        self.gridLayout_4.addWidget(self.pb17M, 0, 5, 1, 1)
        self.pb160M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb160M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb160M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb160M.setCheckable(True)
        self.pb160M.setChecked(True)
        self.pb160M.setAutoExclusive(True)
        self.pb160M.setObjectName("pb160M")
        self.gridLayout_4.addWidget(self.pb160M, 0, 0, 1, 1)
        self.pb80M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb80M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb80M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb80M.setCheckable(True)
        self.pb80M.setAutoExclusive(True)
        self.pb80M.setObjectName("pb80M")
        self.gridLayout_4.addWidget(self.pb80M, 0, 1, 1, 1)
        self.pb40M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb40M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb40M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb40M.setCheckable(True)
        self.pb40M.setAutoExclusive(True)
        self.pb40M.setObjectName("pb40M")
        self.gridLayout_4.addWidget(self.pb40M, 0, 2, 1, 1)
        self.pb30M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb30M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb30M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb30M.setCheckable(True)
        self.pb30M.setAutoExclusive(True)
        self.pb30M.setObjectName("pb30M")
        self.gridLayout_4.addWidget(self.pb30M, 0, 3, 1, 1)
        self.pb20M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb20M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb20M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb20M.setCheckable(True)
        self.pb20M.setAutoExclusive(True)
        self.pb20M.setObjectName("pb20M")
        self.gridLayout_4.addWidget(self.pb20M, 0, 4, 1, 1)
        self.pb12M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb12M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb12M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb12M.setCheckable(True)
        self.pb12M.setAutoExclusive(True)
        self.pb12M.setObjectName("pb12M")
        self.gridLayout_4.addWidget(self.pb12M, 0, 7, 1, 1)
        self.pb10M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb10M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb10M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb10M.setCheckable(True)
        self.pb10M.setAutoExclusive(True)
        self.pb10M.setObjectName("pb10M")
        self.gridLayout_4.addWidget(self.pb10M, 0, 8, 1, 1)
        self.pb6M = QtWidgets.QPushButton(self.groupBox_band)
        self.pb6M.setMinimumSize(QtCore.QSize(0, 18))
        self.pb6M.setMaximumSize(QtCore.QSize(120, 21))
        self.pb6M.setCheckable(True)
        self.pb6M.setAutoExclusive(True)
        self.pb6M.setObjectName("pb6M")
        self.gridLayout_4.addWidget(self.pb6M, 0, 9, 1, 1)
        self.pbGEN = QtWidgets.QPushButton(self.groupBox_band)
        self.pbGEN.setMinimumSize(QtCore.QSize(0, 18))
        self.pbGEN.setMaximumSize(QtCore.QSize(120, 21))
        self.pbGEN.setCheckable(True)
        self.pbGEN.setAutoExclusive(True)
        self.pbGEN.setObjectName("pbGEN")
        self.gridLayout_4.addWidget(self.pbGEN, 0, 10, 1, 1)
        self.horizontalLayout_8.addLayout(self.gridLayout_4)
        self.horizontalLayout.addWidget(self.groupBox_band)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(OpenGRSDR)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_4.setStyleSheet("QWidget {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #323232, stop:0.06 #000000, stop:0.94 #000000, stop: 1 #323232);\n"
"border: 0px;\n"
"}\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setMinimumSize(QtCore.QSize(320, 0))
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_12.setStyleSheet("QWidget {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton { /* all types of tool button */ \n"
"color: #969696;\n"
"border: 0px solid #2e3236; /*#848584;*/\n"
"border-radius: 0px;\n"
"background-color: #323232;\n"
"}\n"
"\n"
"QPushButton:hover { /* all types of tool button */\n"
"color: #C8C8C8;\n"
"border: 1px solid #a75e16; /*#848584;*/\n"
"border-radius: 0px;\n"
"background-color:#646464;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #998A23;\n"
"color: WHITE;\n"
"border: 0px solid #124159;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"background-color: #998A23;\n"
"color: WHITE;\n"
"border: 0px solid #124159;\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QPushButton::menu-button {\n"
"border: 1px solid gray;\n"
"border-top-right-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"/* 16px width + 4px for border = 20px allocated above */\n"
"width: 16px;\n"
"}\n"
"\n"
"QPushButton::menu-arrow {\n"
"image: url(downarrow.png);\n"
"}\n"
"\n"
"QPushButton::menu-arrow:open {\n"
"top: 1px; left: 1px; /* shift it a bit */\n"
"}\n"
"\n"
"QToolButton { /* all types of tool button */ \n"
"color:  #F9CEB8; /*#00FF00;*/\n"
"border: 1px solid  #F9CEB8; /*#00B000;*/\n"
"border-radius: 0px;\n"
"/*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #e7e7e7, stop:0.45 #c8c9c9, stop:0.5 #bcbebc, stop: 1 #818382);*/\n"
"}\n"
"\n"
"QToolButton:hover { /* all types of tool button */\n"
"color: white;\n"
"border: 1px solid #F9CEB8; /* green;*/\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"color:  white; /*#00FF00;*/\n"
"border: 1px solid  #F9CEB8; /*#00B000;*/\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"color:  #F9CEB8; /*#00FF00;*/\n"
"border: 1px solid  #F9CEB8; /*#00B000;*/\n"
"\n"
"}")
        self.widget_12.setObjectName("widget_12")
        self.gridWidget_2 = QtWidgets.QWidget(self.widget_12)
        self.gridWidget_2.setGeometry(QtCore.QRect(3, 35, 200, 12))
        self.gridWidget_2.setStyleSheet("QPushButton {\n"
"border: 0px solid #000000;\n"
"border-radius: 0px;\n"
"background-color:#323232;\n"
"color: #969696;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #646464;\n"
"color: #C8C8C8;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: #787878;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #998A23;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"background-color: #007D00;\n"
"color: #FFFFFF;\n"
"}")
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setHorizontalSpacing(1)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pbAtoB = QtWidgets.QPushButton(self.gridWidget_2)
        self.pbAtoB.setMinimumSize(QtCore.QSize(0, 12))
        self.pbAtoB.setMaximumSize(QtCore.QSize(80, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbAtoB.setFont(font)
        self.pbAtoB.setCheckable(False)
        self.pbAtoB.setChecked(False)
        self.pbAtoB.setObjectName("pbAtoB")
        self.gridLayout_7.addWidget(self.pbAtoB, 1, 2, 1, 1)
        self.pbSplit = QtWidgets.QPushButton(self.gridWidget_2)
        self.pbSplit.setMinimumSize(QtCore.QSize(0, 12))
        self.pbSplit.setMaximumSize(QtCore.QSize(80, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbSplit.setFont(font)
        self.pbSplit.setCheckable(True)
        self.pbSplit.setChecked(False)
        self.pbSplit.setObjectName("pbSplit")
        self.gridLayout_7.addWidget(self.pbSplit, 1, 0, 1, 1)
        self.pbAswapB = QtWidgets.QPushButton(self.gridWidget_2)
        self.pbAswapB.setMinimumSize(QtCore.QSize(0, 12))
        self.pbAswapB.setMaximumSize(QtCore.QSize(80, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbAswapB.setFont(font)
        self.pbAswapB.setCheckable(False)
        self.pbAswapB.setChecked(False)
        self.pbAswapB.setObjectName("pbAswapB")
        self.gridLayout_7.addWidget(self.pbAswapB, 1, 4, 1, 1)
        self.pbAfromB = QtWidgets.QPushButton(self.gridWidget_2)
        self.pbAfromB.setMinimumSize(QtCore.QSize(0, 12))
        self.pbAfromB.setMaximumSize(QtCore.QSize(80, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbAfromB.setFont(font)
        self.pbAfromB.setCheckable(False)
        self.pbAfromB.setChecked(False)
        self.pbAfromB.setObjectName("pbAfromB")
        self.gridLayout_7.addWidget(self.pbAfromB, 1, 3, 1, 1)
        self.pbRx2 = QtWidgets.QPushButton(self.gridWidget_2)
        self.pbRx2.setMinimumSize(QtCore.QSize(0, 12))
        self.pbRx2.setMaximumSize(QtCore.QSize(80, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbRx2.setFont(font)
        self.pbRx2.setCheckable(True)
        self.pbRx2.setChecked(False)
        self.pbRx2.setObjectName("pbRx2")
        self.gridLayout_7.addWidget(self.pbRx2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_12)
        self.label_4.setGeometry(QtCore.QRect(212, 5, 8, 12))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.wdgVfoB = QtWidgets.QWidget(self.widget_12)
        self.wdgVfoB.setGeometry(QtCore.QRect(20, 3, 172, 31))
        self.wdgVfoB.setMinimumSize(QtCore.QSize(172, 31))
        self.wdgVfoB.setMaximumSize(QtCore.QSize(158, 31))
        self.wdgVfoB.setObjectName("wdgVfoB")
        self.pbVfoB = QtWidgets.QPushButton(self.widget_12)
        self.pbVfoB.setEnabled(True)
        self.pbVfoB.setGeometry(QtCore.QRect(204, 20, 24, 13))
        self.pbVfoB.setMinimumSize(QtCore.QSize(24, 13))
        self.pbVfoB.setMaximumSize(QtCore.QSize(24, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pbVfoB.setFont(font)
        self.pbVfoB.setStyleSheet("QPushButton { /* all types of tool button */ \n"
"color: #969696;\n"
"border: 0px solid #2e3236;\n"
"border-radius: 0px;\n"
"background-color: #323232;\n"
"}\n"
"\n"
"QPushButton:hover { /* all types of tool button */\n"
"color:#C8C8C8;\n"
"border: 0px solid rgb(255, 0, 0);\n"
"background-color: #646464;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: white;\n"
"border: 0px solid rgb(255, 0, 0); \n"
"background-color: #A30932;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"color: white;\n"
"border: 0px solid rgb(255, 0, 0);\n"
"background-color: #A30932;\n"
"}")
        self.pbVfoB.setCheckable(True)
        self.pbVfoB.setChecked(False)
        self.pbVfoB.setObjectName("pbVfoB")
        self.pbVfoB_Up_Band = QtWidgets.QPushButton(self.widget_12)
        self.pbVfoB_Up_Band.setGeometry(QtCore.QRect(3, 3, 14, 14))
        self.pbVfoB_Up_Band.setMinimumSize(QtCore.QSize(0, 0))
        self.pbVfoB_Up_Band.setMaximumSize(QtCore.QSize(14, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbVfoB_Up_Band.setFont(font)
        self.pbVfoB_Up_Band.setStyleSheet("QPushButton {\n"
"/*color: #ceeefa;*/ /*E5E5E5;*/\n"
"border: 1px solid #2e3236; /*#124159;*/\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #bfbfbf, stop:0.45 #515253, stop:0.5 #25272b, stop: 1 #2e3236);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #eeeeee, stop:0.5 #5b5e63, stop:0.55 #363b3d, stop: 1 #5d606b);\n"
"color: WHITE;\n"
"border: 1px solid #2e3236;\n"
"}\n"
"QPushButton:disabled {\n"
"border: 1px solid #2e3236; /*#124159;*/\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #bfbfbf, stop:0.45 #515253, stop:0.5 #25272b, stop: 1 #2e3236);\n"
"color: #959595;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f4d4b4, stop:0.45 #b77738, stop:0.5 #a7601b, stop: 1 #884d12);\n"
"/*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #267194, stop:0.45 #307FA4, stop:0.5 #3987AC, stop: 1 #549EC1); */\n"
"color: WHITE;\n"
"border: 1px solid #124159;\n"
"}\n"
"QPushButton:flat {\n"
"border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton::checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f4d4b4, stop:0.45 #b77738, stop:0.5 #a7601b, stop: 1 #884d12);\n"
"color: WHITE;\n"
"border: 1px solid #124159;\n"
"}\n"
"QPushButton:default {\n"
"border-color: navy; /* make the default button prominent */\n"
"}")
        self.pbVfoB_Up_Band.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/spin/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVfoB_Up_Band.setIcon(icon1)
        self.pbVfoB_Up_Band.setIconSize(QtCore.QSize(10, 10))
        self.pbVfoB_Up_Band.setCheckable(False)
        self.pbVfoB_Up_Band.setObjectName("pbVfoB_Up_Band")
        self.pbVfoB_Down_Band = QtWidgets.QPushButton(self.widget_12)
        self.pbVfoB_Down_Band.setGeometry(QtCore.QRect(3, 18, 14, 14))
        self.pbVfoB_Down_Band.setMinimumSize(QtCore.QSize(0, 0))
        self.pbVfoB_Down_Band.setMaximumSize(QtCore.QSize(14, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbVfoB_Down_Band.setFont(font)
        self.pbVfoB_Down_Band.setStyleSheet("QPushButton {\n"
"/*color: #ceeefa;*/ /*E5E5E5;*/\n"
"border: 1px solid #2e3236; /*#124159;*/\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #bfbfbf, stop:0.45 #515253, stop:0.5 #25272b, stop: 1 #2e3236);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #eeeeee, stop:0.5 #5b5e63, stop:0.55 #363b3d, stop: 1 #5d606b);\n"
"color: WHITE;\n"
"border: 1px solid #2e3236;\n"
"}\n"
"QPushButton:disabled {\n"
"border: 1px solid #2e3236; /*#124159;*/\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #bfbfbf, stop:0.45 #515253, stop:0.5 #25272b, stop: 1 #2e3236);\n"
"color: #959595;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f4d4b4, stop:0.45 #b77738, stop:0.5 #a7601b, stop: 1 #884d12);\n"
"/*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #267194, stop:0.45 #307FA4, stop:0.5 #3987AC, stop: 1 #549EC1); */\n"
"color: WHITE;\n"
"border: 1px solid #124159;\n"
"}\n"
"QPushButton:flat {\n"
"border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton::checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f4d4b4, stop:0.45 #b77738, stop:0.5 #a7601b, stop: 1 #884d12);\n"
"color: WHITE;\n"
"border: 1px solid #124159;\n"
"}\n"
"QPushButton:default {\n"
"border-color: navy; /* make the default button prominent */\n"
"}")
        self.pbVfoB_Down_Band.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/spin/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVfoB_Down_Band.setIcon(icon2)
        self.pbVfoB_Down_Band.setIconSize(QtCore.QSize(10, 10))
        self.pbVfoB_Down_Band.setCheckable(False)
        self.pbVfoB_Down_Band.setObjectName("pbVfoB_Down_Band")
        self.horizontalLayout_5.addWidget(self.widget_12)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setEnabled(True)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setStyleSheet("QWidget {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton { \n"
"color: #C5C5C5;\n"
"border: 0px;\n"
"min-width: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"color: White;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(279, 5, 8, 12))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_6.setPalette(palette)
        self.label_6.setStyleSheet("QWidget {\n"
"background-color: #000000;\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.pbVfoA = QtWidgets.QPushButton(self.widget_2)
        self.pbVfoA.setEnabled(True)
        self.pbVfoA.setGeometry(QtCore.QRect(270, 20, 24, 13))
        self.pbVfoA.setMinimumSize(QtCore.QSize(10, 13))
        self.pbVfoA.setMaximumSize(QtCore.QSize(24, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pbVfoA.setFont(font)
        self.pbVfoA.setStyleSheet("QPushButton { /* all types of tool button */ \n"
"color: #969696;\n"
"border: 0px solid #2e3236;\n"
"border-radius: 0px;\n"
"background-color: #323232;\n"
"}\n"
"\n"
"QPushButton:hover { /* all types of tool button */\n"
"color:#C8C8C8;\n"
"border: 0px solid rgb(255, 0, 0);\n"
"background-color: #646464;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: white;\n"
"border: 0px solid rgb(255, 0, 0); \n"
"background-color: #A30932;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"color: white;\n"
"border: 0px solid rgb(255, 0, 0);\n"
"background-color: #A30932;\n"
"}")
        self.pbVfoA.setCheckable(True)
        self.pbVfoA.setChecked(True)
        self.pbVfoA.setObjectName("pbVfoA")
        self.pbLock = QtWidgets.QPushButton(self.widget_2)
        self.pbLock.setGeometry(QtCore.QRect(3, 7, 30, 13))
        self.pbLock.setMinimumSize(QtCore.QSize(10, 13))
        self.pbLock.setMaximumSize(QtCore.QSize(30, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pbLock.setFont(font)
        self.pbLock.setStatusTip("")
        self.pbLock.setStyleSheet("QPushButton {\n"
"border: 0px solid #000000;\n"
"border-radius: 0px;\n"
"background-color:#323232;\n"
"color: #969696;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #646464;\n"
"color: #C8C8C8;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: #787878;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #B42F00;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"background-color: #B42F00;\n"
"color: #FFFFFF;\n"
"}")
        self.pbLock.setCheckable(True)
        self.pbLock.setChecked(False)
        self.pbLock.setObjectName("pbLock")
        self.widget_23 = QtWidgets.QWidget(self.widget_2)
        self.widget_23.setGeometry(QtCore.QRect(213, 3, 52, 16))
        self.widget_23.setStyleSheet("QWidget {\n"
"background-color: #000000;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: 0px solid #000000;\n"
"border-radius: 0px;\n"
"background-color:#323232;\n"
"color: #969696;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #646464;\n"
"color: #C8C8C8;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: #787878;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #998A23;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"background-color: #998A23;\n"
"color: #FFFFFF;\n"
"}")
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbFdown = QtWidgets.QPushButton(self.widget_23)
        self.pbFdown.setMinimumSize(QtCore.QSize(10, 12))
        self.pbFdown.setMaximumSize(QtCore.QSize(120, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pbFdown.setFont(font)
        self.pbFdown.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/arrows/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbFdown.setIcon(icon3)
        self.pbFdown.setCheckable(False)
        self.pbFdown.setObjectName("pbFdown")
        self.horizontalLayout_4.addWidget(self.pbFdown)
        self.pbFlist = QtWidgets.QPushButton(self.widget_23)
        self.pbFlist.setMinimumSize(QtCore.QSize(10, 12))
        self.pbFlist.setMaximumSize(QtCore.QSize(13, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbFlist.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/arrows/arrow-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbFlist.setIcon(icon4)
        self.pbFlist.setCheckable(False)
        self.pbFlist.setObjectName("pbFlist")
        self.horizontalLayout_4.addWidget(self.pbFlist)
        self.pbFup = QtWidgets.QPushButton(self.widget_23)
        self.pbFup.setMinimumSize(QtCore.QSize(10, 12))
        self.pbFup.setMaximumSize(QtCore.QSize(120, 12))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pbFup.setFont(font)
        self.pbFup.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/arrows/arrow-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbFup.setIcon(icon5)
        self.pbFup.setCheckable(False)
        self.pbFup.setObjectName("pbFup")
        self.horizontalLayout_4.addWidget(self.pbFup)
        self.pbFdown.raise_()
        self.pbFup.raise_()
        self.pbFlist.raise_()
        self.widget_24 = QtWidgets.QWidget(self.widget_2)
        self.widget_24.setGeometry(QtCore.QRect(221, 22, 44, 24))
        self.widget_24.setMinimumSize(QtCore.QSize(42, 0))
        self.widget_24.setStyleSheet("QWidget {\n"
"background-color: #000000;\n"
"}")
        self.widget_24.setObjectName("widget_24")
        self.glScale2 = QtWidgets.QHBoxLayout(self.widget_24)
        self.glScale2.setContentsMargins(0, 0, 0, 0)
        self.glScale2.setSpacing(1)
        self.glScale2.setObjectName("glScale2")
        self.pbDg2 = QtWidgets.QPushButton(self.widget_24)
        self.pbDg2.setMinimumSize(QtCore.QSize(10, 16))
        self.pbDg2.setMaximumSize(QtCore.QSize(16, 30))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(22)
        self.pbDg2.setFont(font)
        self.pbDg2.setObjectName("pbDg2")
        self.glScale2.addWidget(self.pbDg2)
        self.pbDg1 = QtWidgets.QPushButton(self.widget_24)
        self.pbDg1.setMinimumSize(QtCore.QSize(10, 16))
        self.pbDg1.setMaximumSize(QtCore.QSize(16, 30))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(22)
        self.pbDg1.setFont(font)
        self.pbDg1.setObjectName("pbDg1")
        self.glScale2.addWidget(self.pbDg1)
        self.pbDg0 = QtWidgets.QPushButton(self.widget_24)
        self.pbDg0.setMinimumSize(QtCore.QSize(10, 16))
        self.pbDg0.setMaximumSize(QtCore.QSize(16, 30))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(22)
        self.pbDg0.setFont(font)
        self.pbDg0.setObjectName("pbDg0")
        self.glScale2.addWidget(self.pbDg0)
        self.widget_25 = QtWidgets.QWidget(self.widget_2)
        self.widget_25.setGeometry(QtCore.QRect(38, 9, 183, 39))
        self.widget_25.setStyleSheet("QWidget {\n"
"background-color: #000000;\n"
"}")
        self.widget_25.setObjectName("widget_25")
        self.glScale1 = QtWidgets.QGridLayout(self.widget_25)
        self.glScale1.setContentsMargins(0, 0, 0, 0)
        self.glScale1.setHorizontalSpacing(1)
        self.glScale1.setVerticalSpacing(0)
        self.glScale1.setObjectName("glScale1")
        self.pbDg6 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg6.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg6.setFont(font)
        self.pbDg6.setObjectName("pbDg6")
        self.glScale1.addWidget(self.pbDg6, 0, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_25)
        self.pushButton_16.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(36)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.glScale1.addWidget(self.pushButton_16, 0, 8, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_25)
        self.pushButton_15.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(36)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.glScale1.addWidget(self.pushButton_15, 0, 4, 1, 1)
        self.pbDg7 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg7.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg7.setFont(font)
        self.pbDg7.setObjectName("pbDg7")
        self.glScale1.addWidget(self.pbDg7, 0, 2, 1, 1)
        self.pbDg8 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg8.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg8.setFont(font)
        self.pbDg8.setObjectName("pbDg8")
        self.glScale1.addWidget(self.pbDg8, 0, 1, 1, 1)
        self.pbDg3 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg3.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg3.setFont(font)
        self.pbDg3.setObjectName("pbDg3")
        self.glScale1.addWidget(self.pbDg3, 0, 7, 1, 1)
        self.pbDg4 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg4.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg4.setFont(font)
        self.pbDg4.setObjectName("pbDg4")
        self.glScale1.addWidget(self.pbDg4, 0, 6, 1, 1)
        self.pbDg5 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg5.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg5.setFont(font)
        self.pbDg5.setObjectName("pbDg5")
        self.glScale1.addWidget(self.pbDg5, 0, 5, 1, 1)
        self.pbDg9 = QtWidgets.QPushButton(self.widget_25)
        self.pbDg9.setMinimumSize(QtCore.QSize(10, 16))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(32)
        self.pbDg9.setFont(font)
        self.pbDg9.setObjectName("pbDg9")
        self.glScale1.addWidget(self.pbDg9, 0, 0, 1, 1)
        self.label_6.raise_()
        self.pbVfoA.raise_()
        self.pbLock.raise_()
        self.widget_24.raise_()
        self.widget_25.raise_()
        self.widget_23.raise_()
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.widget_11 = QtWidgets.QWidget(self.widget_4)
        self.widget_11.setMinimumSize(QtCore.QSize(289, 0))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_11.setStyleSheet("QPushButton { /* all types of tool button */ \n"
"color: #050505;\n"
"border: 0px solid #2e3236; /*#848584;*/\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #e7e7e7, stop:0.45 #c8c9c9, stop:0.5 #bcbebc, stop: 1 #818382);\n"
"}\n"
"\n"
"QPushButton:hover { /* all types of tool button */\n"
"color: #050505;\n"
"border: 1px solid #a75e16; /*#848584;*/\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #e7e7e7, stop:0.45 #c8c9c9, stop:0.5 #bcbebc, stop: 1 #818382);\n"
"}\n"
"\n"
"/*QPushButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #737372, stop:0.45 #b0b1b0, stop:0.5 #c2c1c2, stop: 1 #c2c1c2);\n"
"color: #050505;\n"
"border: 1px solid #2e3236;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #737372, stop:0.45 #b0b1b0, stop:0.5 #c2c1c2, stop: 1 #c2c1c2);\n"
"color: #050505;\n"
"border: 1px solid #2e3236;\n"
"}*/\n"
"\n"
"QPushButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f4d4b4, stop:0.45 #b77738, stop:0.5 #a7601b, stop: 1 #884d12);\n"
"/*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #267194, stop:0.45 #307FA4, stop:0.5 #3987AC, stop: 1 #549EC1); */\n"
"color: WHITE;\n"
"border: 0px solid #124159;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f4d4b4, stop:0.45 #b77738, stop:0.5 #a7601b, stop: 1 #884d12);\n"
"color: WHITE;\n"
"border: 0px solid #124159;\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QPushButton::menu-button {\n"
"border: 1px solid gray;\n"
"border-top-right-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"/* 16px width + 4px for border = 20px allocated above */\n"
"width: 16px;\n"
"}\n"
"\n"
"QPushButton::menu-arrow {\n"
"image: url(downarrow.png);\n"
"}\n"
"\n"
"QPushButton::menu-arrow:open {\n"
"top: 1px; left: 1px; /* shift it a bit */\n"
"}\n"
"\n"
"QToolButton { /* all types of tool button */ \n"
"color: #A0A0A0;\n"
"border: 1px solid #2e3236; /*#848584;*/\n"
"border-radius: 4px;\n"
"/*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #e7e7e7, stop:0.45 #c8c9c9, stop:0.5 #bcbebc, stop: 1 #818382);*/\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:hover { /* all types of tool button */\n"
"color: #A0A0A0;\n"
"border: 1px solid green;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"color: #00FF00;\n"
"border: 1px solid #00B000;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"/*background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #737372, stop:0.45 #b0b1b0, stop:0.5 #c2c1c2, stop: 1 #c2c1c2);\n"
"color: #050505;\n"
"border: 1px solid #2e3236;*/\n"
"color: #00FF00;\n"
"border: 1px solid #00B000;\n"
"\n"
"}\n"
"")
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_16 = QtWidgets.QWidget(self.widget_11)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wdgSmeter = QtWidgets.QFrame(self.widget_16)
        self.wdgSmeter.setMinimumSize(QtCore.QSize(0, 36))
        self.wdgSmeter.setMaximumSize(QtCore.QSize(16777215, 36))
        self.wdgSmeter.setStyleSheet("QWidget { \n"
"background: #000000;\n"
"color: #E5E5E5;\n"
"border: 0px solid #124159;\n"
"}\n"
"\n"
"QMenu {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #e7e7e7, stop:0.45 #c8c9c9, stop:0.5 #bcbebc, stop: 1 #818382);\n"
"     margin: 2px; /* some spacing around the menu */\n"
" }\n"
"\n"
" QMenu::item {\n"
"     padding: 2px 25px 2px 20px;\n"
"     border: 1px solid transparent; /* reserve space for selection border */\n"
" }\n"
"\n"
" QMenu::item:selected {\n"
"     border-color: darkblue;\n"
"     background: rgba(100, 100, 100, 150);\n"
" }\n"
"\n"
" QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"     background: gray;\n"
"     border: 1px inset gray;\n"
"     position: absolute;\n"
"     top: 1px;\n"
"     right: 1px;\n"
"     bottom: 1px;\n"
"     left: 1px;\n"
" }\n"
"\n"
" QMenu::separator {\n"
"     height: 2px;\n"
"     background: lightblue;\n"
"     margin-left: 10px;\n"
"     margin-right: 5px;\n"
" }\n"
"\n"
" QMenu::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" ")
        self.wdgSmeter.setObjectName("wdgSmeter")
        self.verticalLayout_3.addWidget(self.wdgSmeter)
        self.verticalLayout_2.addWidget(self.widget_16)
        self.horizontalLayout_5.addWidget(self.widget_11)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_17 = QtWidgets.QWidget(OpenGRSDR)
        self.widget_17.setMinimumSize(QtCore.QSize(0, 18))
        self.widget_17.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_19 = QtWidgets.QWidget(self.widget_17)
        self.widget_19.setMinimumSize(QtCore.QSize(320, 18))
        self.widget_19.setStyleSheet("QToolButton { /* all types of tool button */ \n"
"border: 1px solid #000000;\n"
"border-radius: 0px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #333333,  stop: 1 #2e2e2e);\n"
"color: #EBEBEB;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:hover { /* all types of tool button */\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #c2c2c2, stop:0.5 #959595, stop:0.55 #959595, stop: 1 #707070);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.5 #366436, stop: 1 #4A944A);\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #325C32, stop:0.45 #366436, stop:0.55 #366436, stop: 1 #4e9d4e);\n"
"\n"
"}")
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_17.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_5.setHorizontalSpacing(2)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pbXitOn = QtWidgets.QPushButton(self.widget_19)
        self.pbXitOn.setMinimumSize(QtCore.QSize(40, 18))
        self.pbXitOn.setMaximumSize(QtCore.QSize(40, 20))
        self.pbXitOn.setCheckable(True)
        self.pbXitOn.setChecked(False)
        self.pbXitOn.setObjectName("pbXitOn")
        self.gridLayout_5.addWidget(self.pbXitOn, 1, 1, 1, 1)
        self.horizontalWidget_3 = QtWidgets.QWidget(self.widget_19)
        self.horizontalWidget_3.setMaximumSize(QtCore.QSize(105, 16777215))
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_17 = QtWidgets.QLabel(self.horizontalWidget_3)
        self.label_17.setMinimumSize(QtCore.QSize(40, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_17.setPalette(palette)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_20.addWidget(self.label_17)
        self.pbStep = QtWidgets.QToolButton(self.horizontalWidget_3)
        self.pbStep.setMinimumSize(QtCore.QSize(60, 14))
        self.pbStep.setMaximumSize(QtCore.QSize(60, 18))
        self.pbStep.setCheckable(False)
        self.pbStep.setChecked(False)
        self.pbStep.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.pbStep.setObjectName("pbStep")
        self.horizontalLayout_20.addWidget(self.pbStep)
        self.gridLayout_5.addWidget(self.horizontalWidget_3, 1, 5, 1, 1)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.widget_19)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_14 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_14.setMinimumSize(QtCore.QSize(40, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_14.setPalette(palette)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_21.addWidget(self.label_14)
        self.cbAGC = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.cbAGC.setModelColumn(0)
        self.cbAGC.setObjectName("cbAGC")
        self.cbAGC.addItem("")
        self.cbAGC.addItem("")
        self.cbAGC.addItem("")
        self.horizontalLayout_21.addWidget(self.cbAGC)
        self.gridLayout_5.addWidget(self.horizontalWidget_2, 1, 2, 1, 1)
        self.pbRitOn = QtWidgets.QPushButton(self.widget_19)
        self.pbRitOn.setMinimumSize(QtCore.QSize(40, 18))
        self.pbRitOn.setMaximumSize(QtCore.QSize(40, 20))
        self.pbRitOn.setCheckable(True)
        self.pbRitOn.setChecked(False)
        self.pbRitOn.setObjectName("pbRitOn")
        self.gridLayout_5.addWidget(self.pbRitOn, 1, 0, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(self.widget_19)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_22.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.gridLayout_5.addWidget(self.horizontalWidget, 1, 6, 1, 1)
        self.horizontalLayout_17.addLayout(self.gridLayout_5)
        self.horizontalLayout_6.addWidget(self.widget_19)
        self.widget_21 = QtWidgets.QWidget(self.widget_17)
        self.widget_21.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_21.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_19.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_18.setSpacing(2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.pbBin = QtWidgets.QPushButton(self.widget_21)
        self.pbBin.setMinimumSize(QtCore.QSize(0, 18))
        self.pbBin.setMaximumSize(QtCore.QSize(40, 21))
        self.pbBin.setCheckable(True)
        self.pbBin.setChecked(False)
        self.pbBin.setObjectName("pbBin")
        self.gridLayout_18.addWidget(self.pbBin, 1, 1, 1, 1)
        self.pbNb = QtWidgets.QPushButton(self.widget_21)
        self.pbNb.setMinimumSize(QtCore.QSize(26, 18))
        self.pbNb.setMaximumSize(QtCore.QSize(40, 21))
        self.pbNb.setCheckable(True)
        self.pbNb.setObjectName("pbNb")
        self.gridLayout_18.addWidget(self.pbNb, 1, 3, 1, 1)
        self.pbNb2 = QtWidgets.QPushButton(self.widget_21)
        self.pbNb2.setMinimumSize(QtCore.QSize(26, 18))
        self.pbNb2.setMaximumSize(QtCore.QSize(40, 21))
        self.pbNb2.setCheckable(True)
        self.pbNb2.setObjectName("pbNb2")
        self.gridLayout_18.addWidget(self.pbNb2, 1, 4, 1, 1)
        self.pbNr = QtWidgets.QPushButton(self.widget_21)
        self.pbNr.setMinimumSize(QtCore.QSize(26, 18))
        self.pbNr.setMaximumSize(QtCore.QSize(40, 21))
        self.pbNr.setCheckable(True)
        self.pbNr.setObjectName("pbNr")
        self.gridLayout_18.addWidget(self.pbNr, 1, 2, 1, 1)
        self.pbAnf = QtWidgets.QPushButton(self.widget_21)
        self.pbAnf.setMinimumSize(QtCore.QSize(26, 18))
        self.pbAnf.setMaximumSize(QtCore.QSize(40, 21))
        self.pbAnf.setStatusTip("")
        self.pbAnf.setCheckable(True)
        self.pbAnf.setObjectName("pbAnf")
        self.gridLayout_18.addWidget(self.pbAnf, 1, 5, 1, 1)
        self.widget_22 = QtWidgets.QWidget(self.widget_21)
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_18.addWidget(self.widget_22, 1, 0, 1, 1)
        self.widget_26 = QtWidgets.QWidget(self.widget_21)
        self.widget_26.setObjectName("widget_26")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_26)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_18.addWidget(self.widget_26, 1, 6, 1, 1)
        self.horizontalLayout_19.addLayout(self.gridLayout_18)
        self.horizontalLayout_6.addWidget(self.widget_21)
        self.widget_20 = QtWidgets.QWidget(self.widget_17)
        self.widget_20.setMinimumSize(QtCore.QSize(0, 18))
        self.widget_20.setObjectName("widget_20")
        self.widget1 = QtWidgets.QWidget(self.widget_20)
        self.widget1.setGeometry(QtCore.QRect(10, 0, 611, 20))
        self.widget1.setObjectName("widget1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pbF0 = QtWidgets.QPushButton(self.widget1)
        self.pbF0.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF0.setMaximumSize(QtCore.QSize(160, 22))
        self.pbF0.setCheckable(True)
        self.pbF0.setChecked(False)
        self.pbF0.setAutoExclusive(True)
        self.pbF0.setObjectName("pbF0")
        self.gridLayout_8.addWidget(self.pbF0, 0, 0, 1, 1)
        self.pbF1 = QtWidgets.QPushButton(self.widget1)
        self.pbF1.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF1.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF1.setCheckable(True)
        self.pbF1.setChecked(False)
        self.pbF1.setAutoExclusive(True)
        self.pbF1.setObjectName("pbF1")
        self.gridLayout_8.addWidget(self.pbF1, 0, 1, 1, 1)
        self.pbF2 = QtWidgets.QPushButton(self.widget1)
        self.pbF2.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF2.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF2.setCheckable(True)
        self.pbF2.setChecked(False)
        self.pbF2.setAutoExclusive(True)
        self.pbF2.setObjectName("pbF2")
        self.gridLayout_8.addWidget(self.pbF2, 0, 2, 1, 1)
        self.pbF3 = QtWidgets.QPushButton(self.widget1)
        self.pbF3.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF3.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF3.setCheckable(True)
        self.pbF3.setChecked(False)
        self.pbF3.setAutoExclusive(True)
        self.pbF3.setObjectName("pbF3")
        self.gridLayout_8.addWidget(self.pbF3, 0, 3, 1, 1)
        self.pbF4 = QtWidgets.QPushButton(self.widget1)
        self.pbF4.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF4.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF4.setCheckable(True)
        self.pbF4.setChecked(True)
        self.pbF4.setAutoExclusive(True)
        self.pbF4.setObjectName("pbF4")
        self.gridLayout_8.addWidget(self.pbF4, 0, 4, 1, 1)
        self.pbF5 = QtWidgets.QPushButton(self.widget1)
        self.pbF5.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF5.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF5.setCheckable(True)
        self.pbF5.setChecked(False)
        self.pbF5.setAutoExclusive(True)
        self.pbF5.setObjectName("pbF5")
        self.gridLayout_8.addWidget(self.pbF5, 0, 5, 1, 1)
        self.pbF6 = QtWidgets.QPushButton(self.widget1)
        self.pbF6.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF6.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF6.setCheckable(True)
        self.pbF6.setChecked(False)
        self.pbF6.setAutoExclusive(True)
        self.pbF6.setObjectName("pbF6")
        self.gridLayout_8.addWidget(self.pbF6, 0, 6, 1, 1)
        self.pbF7 = QtWidgets.QPushButton(self.widget1)
        self.pbF7.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF7.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF7.setCheckable(True)
        self.pbF7.setChecked(False)
        self.pbF7.setAutoExclusive(True)
        self.pbF7.setObjectName("pbF7")
        self.gridLayout_8.addWidget(self.pbF7, 0, 7, 1, 1)
        self.pbF8 = QtWidgets.QPushButton(self.widget1)
        self.pbF8.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF8.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF8.setCheckable(True)
        self.pbF8.setChecked(False)
        self.pbF8.setAutoExclusive(True)
        self.pbF8.setObjectName("pbF8")
        self.gridLayout_8.addWidget(self.pbF8, 0, 8, 1, 1)
        self.pbF9 = QtWidgets.QPushButton(self.widget1)
        self.pbF9.setMinimumSize(QtCore.QSize(0, 18))
        self.pbF9.setMaximumSize(QtCore.QSize(160, 21))
        self.pbF9.setCheckable(True)
        self.pbF9.setChecked(False)
        self.pbF9.setAutoExclusive(True)
        self.pbF9.setObjectName("pbF9")
        self.gridLayout_8.addWidget(self.pbF9, 0, 9, 1, 1)
        self.pbLpan = QtWidgets.QPushButton(self.widget1)
        self.pbLpan.setMinimumSize(QtCore.QSize(0, 18))
        self.pbLpan.setMaximumSize(QtCore.QSize(18, 21))
        self.pbLpan.setCheckable(True)
        self.pbLpan.setChecked(False)
        self.pbLpan.setObjectName("pbLpan")
        self.gridLayout_8.addWidget(self.pbLpan, 0, 10, 1, 1)
        self.pbMemPan = QtWidgets.QPushButton(self.widget1)
        self.pbMemPan.setMinimumSize(QtCore.QSize(0, 18))
        self.pbMemPan.setMaximumSize(QtCore.QSize(18, 21))
        self.pbMemPan.setCheckable(True)
        self.pbMemPan.setChecked(False)
        self.pbMemPan.setObjectName("pbMemPan")
        self.gridLayout_8.addWidget(self.pbMemPan, 0, 11, 1, 1)
        self.horizontalLayout_6.addWidget(self.widget_20)
        self.verticalLayout.addWidget(self.widget_17)
        self.WdgLpanel = QtWidgets.QWidget(OpenGRSDR)
        self.WdgLpanel.setMinimumSize(QtCore.QSize(290, 50))
        self.WdgLpanel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WdgLpanel.setStyleSheet("QSlider::groove:horizontal {\n"
"background-color: #141414;\n"
"position: absolute; \n"
"height: 13px;\n"
"left: 2px; right: 2px;\n"
"border: 0px;\n"
"margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 20 px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BFBFBF, stop: 1 #707070);\n"
"border: 0px;\n"
"margin: 1px 1;\n"
"border-radius: 1px;\n"
"}\n"
"")
        self.WdgLpanel.setObjectName("WdgLpanel")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.WdgLpanel)
        self.gridLayout_14.setContentsMargins(3, 3, 3, 0)
        self.gridLayout_14.setHorizontalSpacing(12)
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.WdgLpanel_7 = QtWidgets.QWidget(self.WdgLpanel)
        self.WdgLpanel_7.setMinimumSize(QtCore.QSize(100, 50))
        self.WdgLpanel_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WdgLpanel_7.setObjectName("WdgLpanel_7")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.WdgLpanel_7)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setHorizontalSpacing(2)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.sbVarLowFreq = QtWidgets.QSpinBox(self.WdgLpanel_7)
        self.sbVarLowFreq.setMinimumSize(QtCore.QSize(45, 20))
        self.sbVarLowFreq.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sbVarLowFreq.setMinimum(-15000)
        self.sbVarLowFreq.setMaximum(15000)
        self.sbVarLowFreq.setObjectName("sbVarLowFreq")
        self.gridLayout_15.addWidget(self.sbVarLowFreq, 1, 1, 1, 1)
        self.sbVarHighFreq = QtWidgets.QSpinBox(self.WdgLpanel_7)
        self.sbVarHighFreq.setMinimumSize(QtCore.QSize(45, 20))
        self.sbVarHighFreq.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sbVarHighFreq.setMinimum(-15000)
        self.sbVarHighFreq.setMaximum(15000)
        self.sbVarHighFreq.setObjectName("sbVarHighFreq")
        self.gridLayout_15.addWidget(self.sbVarHighFreq, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.WdgLpanel_7)
        self.label_18.setObjectName("label_18")
        self.gridLayout_15.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.WdgLpanel_7)
        self.label_19.setObjectName("label_19")
        self.gridLayout_15.addWidget(self.label_19, 1, 0, 1, 1)
        self.pbMemUpFreq = QtWidgets.QPushButton(self.WdgLpanel_7)
        self.pbMemUpFreq.setMinimumSize(QtCore.QSize(18, 16))
        self.pbMemUpFreq.setObjectName("pbMemUpFreq")
        self.gridLayout_15.addWidget(self.pbMemUpFreq, 0, 2, 1, 1)
        self.pbMemDownFreq = QtWidgets.QPushButton(self.WdgLpanel_7)
        self.pbMemDownFreq.setMinimumSize(QtCore.QSize(0, 16))
        self.pbMemDownFreq.setObjectName("pbMemDownFreq")
        self.gridLayout_15.addWidget(self.pbMemDownFreq, 1, 2, 1, 1)
        self.gridLayout_14.addWidget(self.WdgLpanel_7, 1, 8, 1, 1)
        self.WdgLpanel_6 = QtWidgets.QWidget(self.WdgLpanel)
        self.WdgLpanel_6.setMinimumSize(QtCore.QSize(100, 50))
        self.WdgLpanel_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WdgLpanel_6.setObjectName("WdgLpanel_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.WdgLpanel_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.WdgLpanel_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.WdgLpanel_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.WdgLpanel_6)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 2, 1, 1, 1)
        self.pbEqOn = QtWidgets.QPushButton(self.WdgLpanel_6)
        self.pbEqOn.setMinimumSize(QtCore.QSize(19, 16))
        self.pbEqOn.setMaximumSize(QtCore.QSize(19, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbEqOn.setFont(font)
        self.pbEqOn.setCheckable(True)
        self.pbEqOn.setChecked(False)
        self.pbEqOn.setObjectName("pbEqOn")
        self.gridLayout_6.addWidget(self.pbEqOn, 0, 0, 1, 1)
        self.pbEqRx = QtWidgets.QPushButton(self.WdgLpanel_6)
        self.pbEqRx.setMinimumSize(QtCore.QSize(19, 16))
        self.pbEqRx.setMaximumSize(QtCore.QSize(19, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbEqRx.setFont(font)
        self.pbEqRx.setCheckable(True)
        self.pbEqRx.setChecked(True)
        self.pbEqRx.setObjectName("pbEqRx")
        self.gridLayout_6.addWidget(self.pbEqRx, 1, 0, 1, 1)
        self.pbEqTx = QtWidgets.QPushButton(self.WdgLpanel_6)
        self.pbEqTx.setMinimumSize(QtCore.QSize(19, 16))
        self.pbEqTx.setMaximumSize(QtCore.QSize(19, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbEqTx.setFont(font)
        self.pbEqTx.setCheckable(True)
        self.pbEqTx.setChecked(False)
        self.pbEqTx.setObjectName("pbEqTx")
        self.gridLayout_6.addWidget(self.pbEqTx, 2, 0, 1, 1)
        self.swEq400Hz = QtWidgets.QStackedWidget(self.WdgLpanel_6)
        self.swEq400Hz.setObjectName("swEq400Hz")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.slRxEq400 = QtWidgets.QSlider(self.page_3)
        self.slRxEq400.setMinimum(-15)
        self.slRxEq400.setMaximum(15)
        self.slRxEq400.setOrientation(QtCore.Qt.Horizontal)
        self.slRxEq400.setObjectName("slRxEq400")
        self.verticalLayout_6.addWidget(self.slRxEq400)
        self.swEq400Hz.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.slTxEq400 = QtWidgets.QSlider(self.page_4)
        self.slTxEq400.setMinimum(-15)
        self.slTxEq400.setMaximum(15)
        self.slTxEq400.setOrientation(QtCore.Qt.Horizontal)
        self.slTxEq400.setObjectName("slTxEq400")
        self.verticalLayout_8.addWidget(self.slTxEq400)
        self.swEq400Hz.addWidget(self.page_4)
        self.gridLayout_6.addWidget(self.swEq400Hz, 0, 2, 1, 1)
        self.swEq1k5Hz = QtWidgets.QStackedWidget(self.WdgLpanel_6)
        self.swEq1k5Hz.setObjectName("swEq1k5Hz")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.slRxEq1k5 = QtWidgets.QSlider(self.page_5)
        self.slRxEq1k5.setMinimum(-15)
        self.slRxEq1k5.setMaximum(15)
        self.slRxEq1k5.setOrientation(QtCore.Qt.Horizontal)
        self.slRxEq1k5.setObjectName("slRxEq1k5")
        self.verticalLayout_9.addWidget(self.slRxEq1k5)
        self.swEq1k5Hz.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.slTxEq1k5 = QtWidgets.QSlider(self.page_6)
        self.slTxEq1k5.setMinimum(-15)
        self.slTxEq1k5.setMaximum(15)
        self.slTxEq1k5.setOrientation(QtCore.Qt.Horizontal)
        self.slTxEq1k5.setObjectName("slTxEq1k5")
        self.verticalLayout_12.addWidget(self.slTxEq1k5)
        self.swEq1k5Hz.addWidget(self.page_6)
        self.gridLayout_6.addWidget(self.swEq1k5Hz, 1, 2, 1, 1)
        self.swEq6kHz = QtWidgets.QStackedWidget(self.WdgLpanel_6)
        self.swEq6kHz.setObjectName("swEq6kHz")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.slRxEq6k = QtWidgets.QSlider(self.page_7)
        self.slRxEq6k.setMinimum(-15)
        self.slRxEq6k.setMaximum(15)
        self.slRxEq6k.setOrientation(QtCore.Qt.Horizontal)
        self.slRxEq6k.setObjectName("slRxEq6k")
        self.verticalLayout_10.addWidget(self.slRxEq6k)
        self.swEq6kHz.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.slTxEq6k = QtWidgets.QSlider(self.page_8)
        self.slTxEq6k.setMinimum(-15)
        self.slTxEq6k.setMaximum(15)
        self.slTxEq6k.setOrientation(QtCore.Qt.Horizontal)
        self.slTxEq6k.setObjectName("slTxEq6k")
        self.verticalLayout_11.addWidget(self.slTxEq6k)
        self.swEq6kHz.addWidget(self.page_8)
        self.gridLayout_6.addWidget(self.swEq6kHz, 2, 2, 1, 1)
        self.gridLayout_14.addWidget(self.WdgLpanel_6, 1, 0, 1, 1)
        self.widget_15 = QtWidgets.QWidget(self.WdgLpanel)
        self.widget_15.setMinimumSize(QtCore.QSize(70, 0))
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.widget_15)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setHorizontalSpacing(4)
        self.gridLayout_16.setVerticalSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.pbBal2 = QtWidgets.QPushButton(self.widget_15)
        self.pbBal2.setMinimumSize(QtCore.QSize(32, 16))
        self.pbBal2.setMaximumSize(QtCore.QSize(32, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pbBal2.setFont(font)
        self.pbBal2.setChecked(False)
        self.pbBal2.setObjectName("pbBal2")
        self.gridLayout_16.addWidget(self.pbBal2, 2, 2, 1, 1)
        self.sbRit = QtWidgets.QSpinBox(self.widget_15)
        self.sbRit.setMinimumSize(QtCore.QSize(0, 18))
        self.sbRit.setMinimum(-10000)
        self.sbRit.setMaximum(10000)
        self.sbRit.setObjectName("sbRit")
        self.gridLayout_16.addWidget(self.sbRit, 0, 3, 1, 1)
        self.sbXit = QtWidgets.QSpinBox(self.widget_15)
        self.sbXit.setMinimumSize(QtCore.QSize(0, 18))
        self.sbXit.setMinimum(-10000)
        self.sbXit.setMaximum(10000)
        self.sbXit.setObjectName("sbXit")
        self.gridLayout_16.addWidget(self.sbXit, 0, 1, 1, 1)
        self.pbRitReset = QtWidgets.QPushButton(self.widget_15)
        self.pbRitReset.setMinimumSize(QtCore.QSize(32, 16))
        self.pbRitReset.setMaximumSize(QtCore.QSize(32, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pbRitReset.setFont(font)
        self.pbRitReset.setChecked(False)
        self.pbRitReset.setObjectName("pbRitReset")
        self.gridLayout_16.addWidget(self.pbRitReset, 0, 2, 1, 1)
        self.pbXitReset = QtWidgets.QPushButton(self.widget_15)
        self.pbXitReset.setMinimumSize(QtCore.QSize(32, 16))
        self.pbXitReset.setMaximumSize(QtCore.QSize(32, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pbXitReset.setFont(font)
        self.pbXitReset.setChecked(False)
        self.pbXitReset.setObjectName("pbXitReset")
        self.gridLayout_16.addWidget(self.pbXitReset, 0, 0, 1, 1)
        self.slRx1Vol = QtWidgets.QSlider(self.widget_15)
        self.slRx1Vol.setMinimum(0)
        self.slRx1Vol.setMaximum(100)
        self.slRx1Vol.setPageStep(1)
        self.slRx1Vol.setProperty("value", 70)
        self.slRx1Vol.setOrientation(QtCore.Qt.Horizontal)
        self.slRx1Vol.setInvertedAppearance(False)
        self.slRx1Vol.setObjectName("slRx1Vol")
        self.gridLayout_16.addWidget(self.slRx1Vol, 1, 1, 1, 1)
        self.slRx2Vol = QtWidgets.QSlider(self.widget_15)
        self.slRx2Vol.setMinimum(0)
        self.slRx2Vol.setMaximum(100)
        self.slRx2Vol.setPageStep(1)
        self.slRx2Vol.setProperty("value", 70)
        self.slRx2Vol.setOrientation(QtCore.Qt.Horizontal)
        self.slRx2Vol.setInvertedAppearance(False)
        self.slRx2Vol.setObjectName("slRx2Vol")
        self.gridLayout_16.addWidget(self.slRx2Vol, 2, 1, 1, 1)
        self.slRx2Bal = QtWidgets.QSlider(self.widget_15)
        self.slRx2Bal.setMinimum(1)
        self.slRx2Bal.setMaximum(100)
        self.slRx2Bal.setPageStep(1)
        self.slRx2Bal.setProperty("value", 30)
        self.slRx2Bal.setOrientation(QtCore.Qt.Horizontal)
        self.slRx2Bal.setInvertedAppearance(False)
        self.slRx2Bal.setInvertedControls(True)
        self.slRx2Bal.setObjectName("slRx2Bal")
        self.gridLayout_16.addWidget(self.slRx2Bal, 2, 3, 1, 1)
        self.slRx1Bal = QtWidgets.QSlider(self.widget_15)
        self.slRx1Bal.setMinimum(1)
        self.slRx1Bal.setMaximum(100)
        self.slRx1Bal.setPageStep(1)
        self.slRx1Bal.setProperty("value", 30)
        self.slRx1Bal.setOrientation(QtCore.Qt.Horizontal)
        self.slRx1Bal.setInvertedAppearance(False)
        self.slRx1Bal.setInvertedControls(True)
        self.slRx1Bal.setObjectName("slRx1Bal")
        self.gridLayout_16.addWidget(self.slRx1Bal, 1, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget_15)
        self.label_21.setObjectName("label_21")
        self.gridLayout_16.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_15)
        self.label_22.setObjectName("label_22")
        self.gridLayout_16.addWidget(self.label_22, 2, 0, 1, 1)
        self.pbBal1 = QtWidgets.QPushButton(self.widget_15)
        self.pbBal1.setMinimumSize(QtCore.QSize(32, 16))
        self.pbBal1.setMaximumSize(QtCore.QSize(32, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pbBal1.setFont(font)
        self.pbBal1.setChecked(False)
        self.pbBal1.setObjectName("pbBal1")
        self.gridLayout_16.addWidget(self.pbBal1, 1, 2, 1, 1)
        self.gridLayout_14.addWidget(self.widget_15, 1, 1, 1, 1)
        self.WdgLpanel_5 = QtWidgets.QWidget(self.WdgLpanel)
        self.WdgLpanel_5.setMinimumSize(QtCore.QSize(100, 50))
        self.WdgLpanel_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WdgLpanel_5.setObjectName("WdgLpanel_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.WdgLpanel_5)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setHorizontalSpacing(2)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.slSql = QtWidgets.QSlider(self.WdgLpanel_5)
        self.slSql.setMinimum(-160)
        self.slSql.setMaximum(0)
        self.slSql.setOrientation(QtCore.Qt.Horizontal)
        self.slSql.setObjectName("slSql")
        self.gridLayout_11.addWidget(self.slSql, 0, 1, 1, 1)
        self.slGate = QtWidgets.QSlider(self.WdgLpanel_5)
        self.slGate.setMinimum(-165)
        self.slGate.setMaximum(0)
        self.slGate.setOrientation(QtCore.Qt.Horizontal)
        self.slGate.setObjectName("slGate")
        self.gridLayout_11.addWidget(self.slGate, 1, 1, 1, 1)
        self.pbSql = QtWidgets.QPushButton(self.WdgLpanel_5)
        self.pbSql.setMinimumSize(QtCore.QSize(32, 16))
        self.pbSql.setMaximumSize(QtCore.QSize(32, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbSql.setFont(font)
        self.pbSql.setCheckable(True)
        self.pbSql.setChecked(False)
        self.pbSql.setObjectName("pbSql")
        self.gridLayout_11.addWidget(self.pbSql, 0, 0, 1, 1)
        self.pbGate = QtWidgets.QPushButton(self.WdgLpanel_5)
        self.pbGate.setMinimumSize(QtCore.QSize(32, 16))
        self.pbGate.setMaximumSize(QtCore.QSize(32, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbGate.setFont(font)
        self.pbGate.setCheckable(True)
        self.pbGate.setChecked(False)
        self.pbGate.setObjectName("pbGate")
        self.gridLayout_11.addWidget(self.pbGate, 1, 0, 1, 1)
        self.sbSql = QtWidgets.QSpinBox(self.WdgLpanel_5)
        self.sbSql.setMinimumSize(QtCore.QSize(0, 20))
        self.sbSql.setMinimum(-165)
        self.sbSql.setMaximum(0)
        self.sbSql.setObjectName("sbSql")
        self.gridLayout_11.addWidget(self.sbSql, 0, 2, 1, 1)
        self.sbGate = QtWidgets.QSpinBox(self.WdgLpanel_5)
        self.sbGate.setMinimumSize(QtCore.QSize(0, 20))
        self.sbGate.setMinimum(-165)
        self.sbGate.setMaximum(0)
        self.sbGate.setObjectName("sbGate")
        self.gridLayout_11.addWidget(self.sbGate, 1, 2, 1, 1)
        self.gridLayout_14.addWidget(self.WdgLpanel_5, 1, 2, 1, 1)
        self.WdgLpanel_4 = QtWidgets.QWidget(self.WdgLpanel)
        self.WdgLpanel_4.setMinimumSize(QtCore.QSize(100, 50))
        self.WdgLpanel_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WdgLpanel_4.setObjectName("WdgLpanel_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.WdgLpanel_4)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.slSr = QtWidgets.QSlider(self.WdgLpanel_4)
        self.slSr.setMinimum(1)
        self.slSr.setMaximum(29)
        self.slSr.setPageStep(1)
        self.slSr.setProperty("value", 10)
        self.slSr.setOrientation(QtCore.Qt.Horizontal)
        self.slSr.setInvertedAppearance(True)
        self.slSr.setInvertedControls(False)
        self.slSr.setObjectName("slSr")
        self.gridLayout_10.addWidget(self.slSr, 2, 1, 1, 1)
        self.slWr = QtWidgets.QSlider(self.WdgLpanel_4)
        self.slWr.setMinimum(1)
        self.slWr.setMaximum(100)
        self.slWr.setPageStep(1)
        self.slWr.setProperty("value", 30)
        self.slWr.setOrientation(QtCore.Qt.Horizontal)
        self.slWr.setInvertedAppearance(True)
        self.slWr.setObjectName("slWr")
        self.gridLayout_10.addWidget(self.slWr, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.WdgLpanel_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.WdgLpanel_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 3, 0, 1, 1)
        self.gridLayout_14.addWidget(self.WdgLpanel_4, 1, 7, 1, 1)
        self.StWdg0 = QtWidgets.QStackedWidget(self.WdgLpanel)
        self.StWdg0.setObjectName("StWdg0")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setHorizontalSpacing(2)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pbComp = QtWidgets.QPushButton(self.page)
        self.pbComp.setMinimumSize(QtCore.QSize(34, 16))
        self.pbComp.setMaximumSize(QtCore.QSize(34, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbComp.setFont(font)
        self.pbComp.setCheckable(True)
        self.pbComp.setChecked(False)
        self.pbComp.setObjectName("pbComp")
        self.gridLayout_13.addWidget(self.pbComp, 0, 0, 1, 1)
        self.pbCpdr = QtWidgets.QPushButton(self.page)
        self.pbCpdr.setMinimumSize(QtCore.QSize(34, 16))
        self.pbCpdr.setMaximumSize(QtCore.QSize(34, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        self.pbCpdr.setFont(font)
        self.pbCpdr.setCheckable(True)
        self.pbCpdr.setChecked(False)
        self.pbCpdr.setObjectName("pbCpdr")
        self.gridLayout_13.addWidget(self.pbCpdr, 1, 0, 1, 1)
        self.slComp = QtWidgets.QSlider(self.page)
        self.slComp.setMaximum(20)
        self.slComp.setPageStep(2)
        self.slComp.setOrientation(QtCore.Qt.Horizontal)
        self.slComp.setObjectName("slComp")
        self.gridLayout_13.addWidget(self.slComp, 0, 1, 1, 1)
        self.slCpdr = QtWidgets.QSlider(self.page)
        self.slCpdr.setMaximum(10)
        self.slCpdr.setPageStep(1)
        self.slCpdr.setOrientation(QtCore.Qt.Horizontal)
        self.slCpdr.setObjectName("slCpdr")
        self.gridLayout_13.addWidget(self.slCpdr, 1, 1, 1, 1)
        self.sbComp = QtWidgets.QSpinBox(self.page)
        self.sbComp.setMinimumSize(QtCore.QSize(0, 20))
        self.sbComp.setMaximum(20)
        self.sbComp.setObjectName("sbComp")
        self.gridLayout_13.addWidget(self.sbComp, 0, 2, 1, 1)
        self.sbCpdr = QtWidgets.QSpinBox(self.page)
        self.sbCpdr.setMinimumSize(QtCore.QSize(0, 20))
        self.sbCpdr.setMaximum(10)
        self.sbCpdr.setObjectName("sbCpdr")
        self.gridLayout_13.addWidget(self.sbCpdr, 1, 2, 1, 1)
        self.StWdg0.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setHorizontalSpacing(2)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.slPitch = QtWidgets.QSlider(self.page_2)
        self.slPitch.setMinimum(50)
        self.slPitch.setMaximum(2500)
        self.slPitch.setSingleStep(5)
        self.slPitch.setPageStep(25)
        self.slPitch.setOrientation(QtCore.Qt.Horizontal)
        self.slPitch.setObjectName("slPitch")
        self.gridLayout_12.addWidget(self.slPitch, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_12.addWidget(self.label_15, 0, 0, 1, 1)
        self.sbPitch = QtWidgets.QSpinBox(self.page_2)
        self.sbPitch.setMinimumSize(QtCore.QSize(0, 20))
        self.sbPitch.setStyleSheet("QWidget { \n"
"border: 1px solid #0e0e0e;\n"
"color: #E5E5E5;\n"
"}")
        self.sbPitch.setMinimum(50)
        self.sbPitch.setMaximum(2500)
        self.sbPitch.setObjectName("sbPitch")
        self.gridLayout_12.addWidget(self.sbPitch, 0, 4, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.page_2)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.chbBreakIn = QtWidgets.QCheckBox(self.widget_10)
        self.chbBreakIn.setMinimumSize(QtCore.QSize(40, 0))
        self.chbBreakIn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.chbBreakIn.setChecked(False)
        self.chbBreakIn.setAutoRepeat(False)
        self.chbBreakIn.setAutoExclusive(False)
        self.chbBreakIn.setTristate(False)
        self.chbBreakIn.setObjectName("chbBreakIn")
        self.horizontalLayout_11.addWidget(self.chbBreakIn)
        self.gridLayout_12.addWidget(self.widget_10, 1, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.page_2)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 19))
        self.widget_9.setObjectName("widget_9")
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 31, 19))
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.widget_9, 1, 3, 1, 1)
        self.sbCwDelay = QtWidgets.QSpinBox(self.page_2)
        self.sbCwDelay.setMinimumSize(QtCore.QSize(45, 20))
        self.sbCwDelay.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sbCwDelay.setStyleSheet("QWidget { \n"
"border: 1px solid #0e0e0e;\n"
"color: #E5E5E5;\n"
"}")
        self.sbCwDelay.setFrame(True)
        self.sbCwDelay.setMinimum(10)
        self.sbCwDelay.setMaximum(5000)
        self.sbCwDelay.setProperty("value", 25)
        self.sbCwDelay.setObjectName("sbCwDelay")
        self.gridLayout_12.addWidget(self.sbCwDelay, 1, 4, 1, 1)
        self.StWdg0.addWidget(self.page_2)
        self.gridLayout_14.addWidget(self.StWdg0, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.WdgLpanel)
        self.line = QtWidgets.QFrame(OpenGRSDR)
        self.line.setMinimumSize(QtCore.QSize(0, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("QWidget {\n"
"        background: black;\n"
"        border: 0px solid #999999;\n"
"        color: #F9CEB8;\n"
"}\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.WdgMainGraph = QtWidgets.QWidget(OpenGRSDR)
        self.WdgMainGraph.setMinimumSize(QtCore.QSize(0, 40))
        self.WdgMainGraph.setStyleSheet("QWidget { \n"
"background-color: rgb(33, 33, 33);\n"
"border: 0px;\n"
"color: #E5E5E5;\n"
"}")
        self.WdgMainGraph.setObjectName("WdgMainGraph")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.WdgMainGraph)
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.WdgMainGraph)

        self.retranslateUi(OpenGRSDR)
        self.swVolume.setCurrentIndex(0)
        self.swMicSpeed.setCurrentIndex(0)
        self.swEq400Hz.setCurrentIndex(0)
        self.swEq1k5Hz.setCurrentIndex(0)
        self.swEq6kHz.setCurrentIndex(1)
        self.StWdg0.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OpenGRSDR)

    def retranslateUi(self, OpenGRSDR):
        _translate = QtCore.QCoreApplication.translate
        OpenGRSDR.setWindowTitle(_translate("OpenGRSDR", "OpenGRSdr"))
        self.pbStart.setToolTip(_translate("OpenGRSDR", "Start/Stop"))
        self.lbVersion.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">OpenGRSDR v0.01   github.com/wd8rde/opengrsdrgui</span></p></body></html>"))
        self.lbDate.setToolTip(_translate("OpenGRSDR", "Local/UTC Date"))
        self.lbDate.setText(_translate("OpenGRSDR", "Date: 27,12,2019    "))
        self.pbTime.setToolTip(_translate("OpenGRSDR", "Local/UTC Time"))
        self.pbTime.setText(_translate("OpenGRSDR", "Time: 03:40:45 "))
        self.pbCwMacro.setToolTip(_translate("OpenGRSDR", "CW Macros"))
        self.pbCwMacro.setText(_translate("OpenGRSDR", "CW Macro"))
        self.pbOptions.setToolTip(_translate("OpenGRSDR", "ExpertSDR options"))
        self.pbOptions.setText(_translate("OpenGRSDR", "Options"))
        self.pbAbout.setToolTip(_translate("OpenGRSDR", "About ExpertSDR"))
        self.pbAbout.setText(_translate("OpenGRSDR", "About"))
        self.pbTone.setText(_translate("OpenGRSDR", "TONE"))
        self.pbMox.setText(_translate("OpenGRSDR", "MOX"))
        self.pbMute.setText(_translate("OpenGRSDR", "MUT"))
        self.pbVoicePlay.setToolTip(_translate("OpenGRSDR", "PLAY"))
        self.pbVoiceRec.setToolTip(_translate("OpenGRSDR", "REC"))
        self.pbAtten.setToolTip(_translate("OpenGRSDR", "Enable monitor"))
        self.pbAtten.setText(_translate("OpenGRSDR", "RF Atten"))
        self.pbPreamp.setToolTip(_translate("OpenGRSDR", "Preamplifier"))
        self.pbPreamp.setText(_translate("OpenGRSDR", "RF preamp"))
        self.pbPa.setToolTip(_translate("OpenGRSDR", "Enable External Power Amplifier"))
        self.pbPa.setText(_translate("OpenGRSDR", "Audio preamp"))
        self.label.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">VOL:</span></p></body></html>"))
        self.label_2.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RF:</span></p></body></html>"))
        self.label_7.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Drive:</span></p></body></html>"))
        self.lbMic.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">MIC:</span></p></body></html>"))
        self.label_20.setText(_translate("OpenGRSDR", "Speed:"))
        self.pbAutoFreqMaxLevel.setToolTip(_translate("OpenGRSDR", "Auto tuning"))
        self.pbAutoFreqMaxLevel.setText(_translate("OpenGRSDR", "Auto"))
        self.cbPanInfo.setToolTip(_translate("OpenGRSDR", "Show panadapter infomation"))
        self.cbPanInfo.setText(_translate("OpenGRSDR", "Info  "))
        self.pbAM.setToolTip(_translate("OpenGRSDR", "Amplitude Modulation"))
        self.pbAM.setText(_translate("OpenGRSDR", "AM"))
        self.pbSAM.setText(_translate("OpenGRSDR", "SAM"))
        self.pbFMN.setText(_translate("OpenGRSDR", "NFM"))
        self.pbUSB.setToolTip(_translate("OpenGRSDR", "Up Side Band"))
        self.pbUSB.setText(_translate("OpenGRSDR", "USB"))
        self.pbDIGU.setText(_translate("OpenGRSDR", "DIGU"))
        self.pbDRM.setText(_translate("OpenGRSDR", "DRM"))
        self.pbSPEC.setText(_translate("OpenGRSDR", "SPEC"))
        self.pbDIGL.setText(_translate("OpenGRSDR", "DIGL"))
        self.pbCWU.setText(_translate("OpenGRSDR", "CWU"))
        self.pbCWL.setText(_translate("OpenGRSDR", "CWL"))
        self.pbDSB.setToolTip(_translate("OpenGRSDR", "Double Side Band"))
        self.pbDSB.setText(_translate("OpenGRSDR", "DSB"))
        self.pbLSB.setToolTip(_translate("OpenGRSDR", "Low Side Band"))
        self.pbLSB.setText(_translate("OpenGRSDR", "LSB"))
        self.pb15M.setText(_translate("OpenGRSDR", "15M"))
        self.pb17M.setText(_translate("OpenGRSDR", "17M"))
        self.pb160M.setText(_translate("OpenGRSDR", "160M"))
        self.pb80M.setText(_translate("OpenGRSDR", "80M"))
        self.pb40M.setText(_translate("OpenGRSDR", "40M"))
        self.pb30M.setText(_translate("OpenGRSDR", "30M"))
        self.pb20M.setText(_translate("OpenGRSDR", "20M"))
        self.pb12M.setText(_translate("OpenGRSDR", "12M"))
        self.pb10M.setText(_translate("OpenGRSDR", "10M"))
        self.pb6M.setText(_translate("OpenGRSDR", "6M"))
        self.pbGEN.setText(_translate("OpenGRSDR", "GEN"))
        self.pbAtoB.setToolTip(_translate("OpenGRSDR", "Copy VFO A to VFO B"))
        self.pbAtoB.setText(_translate("OpenGRSDR", "B<-A"))
        self.pbSplit.setToolTip(_translate("OpenGRSDR", "Enable Split Mode"))
        self.pbSplit.setText(_translate("OpenGRSDR", " SPLT "))
        self.pbAswapB.setToolTip(_translate("OpenGRSDR", "Swap VFO A with VFO B"))
        self.pbAswapB.setText(_translate("OpenGRSDR", "B<>A"))
        self.pbAfromB.setToolTip(_translate("OpenGRSDR", "Copy VFO B to VFO A"))
        self.pbAfromB.setText(_translate("OpenGRSDR", "B->A "))
        self.pbRx2.setToolTip(_translate("OpenGRSDR", "Enable second receiver"))
        self.pbRx2.setText(_translate("OpenGRSDR", "SubRX"))
        self.label_4.setText(_translate("OpenGRSDR", "B"))
        self.pbVfoB.setToolTip(_translate("OpenGRSDR", "<html><head/><body><p>RX2</p></body></html>"))
        self.pbVfoB.setText(_translate("OpenGRSDR", "TX"))
        self.label_6.setText(_translate("OpenGRSDR", "A"))
        self.pbVfoA.setToolTip(_translate("OpenGRSDR", "<html><head/><body><p>RX1</p></body></html>"))
        self.pbVfoA.setText(_translate("OpenGRSDR", "TX"))
        self.pbLock.setToolTip(_translate("OpenGRSDR", "Lock screen"))
        self.pbLock.setText(_translate("OpenGRSDR", "LOCK"))
        self.pbFdown.setToolTip(_translate("OpenGRSDR", "Back to previous station"))
        self.pbFup.setToolTip(_translate("OpenGRSDR", "Move to next station"))
        self.pbDg2.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg2.setText(_translate("OpenGRSDR", "8"))
        self.pbDg1.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg1.setText(_translate("OpenGRSDR", "9"))
        self.pbDg0.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg0.setText(_translate("OpenGRSDR", "0"))
        self.pbDg6.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg6.setText(_translate("OpenGRSDR", "4"))
        self.pushButton_16.setText(_translate("OpenGRSDR", "."))
        self.pushButton_15.setText(_translate("OpenGRSDR", "."))
        self.pbDg7.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg7.setText(_translate("OpenGRSDR", "3"))
        self.pbDg8.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg8.setText(_translate("OpenGRSDR", "2"))
        self.pbDg3.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg3.setText(_translate("OpenGRSDR", "7"))
        self.pbDg4.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg4.setText(_translate("OpenGRSDR", "6"))
        self.pbDg5.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg5.setText(_translate("OpenGRSDR", "5"))
        self.pbDg9.setToolTip(_translate("OpenGRSDR", "VfoA Frequency"))
        self.pbDg9.setText(_translate("OpenGRSDR", "8"))
        self.pbXitOn.setText(_translate("OpenGRSDR", " XIT "))
        self.label_17.setText(_translate("OpenGRSDR", "Step:"))
        self.pbStep.setText(_translate("OpenGRSDR", "100kHz   "))
        self.label_14.setText(_translate("OpenGRSDR", "AGC:"))
        self.cbAGC.setItemText(0, _translate("OpenGRSDR", "Slow"))
        self.cbAGC.setItemText(1, _translate("OpenGRSDR", "Med"))
        self.cbAGC.setItemText(2, _translate("OpenGRSDR", "Fast"))
        self.pbRitOn.setText(_translate("OpenGRSDR", " RIT "))
        self.pbBin.setToolTip(_translate("OpenGRSDR", "Binatural"))
        self.pbBin.setText(_translate("OpenGRSDR", "BIN"))
        self.pbNb.setToolTip(_translate("OpenGRSDR", "Noise Blanker"))
        self.pbNb.setText(_translate("OpenGRSDR", "NB"))
        self.pbNb2.setToolTip(_translate("OpenGRSDR", "Noise Blanker 2"))
        self.pbNb2.setText(_translate("OpenGRSDR", "NB2"))
        self.pbNr.setToolTip(_translate("OpenGRSDR", "Noise Redaction"))
        self.pbNr.setText(_translate("OpenGRSDR", "NR"))
        self.pbAnf.setToolTip(_translate("OpenGRSDR", "Automatic Notch filter"))
        self.pbAnf.setText(_translate("OpenGRSDR", "ANF"))
        self.pbF0.setText(_translate("OpenGRSDR", "500"))
        self.pbF1.setText(_translate("OpenGRSDR", "1.8K"))
        self.pbF2.setText(_translate("OpenGRSDR", "2K"))
        self.pbF3.setText(_translate("OpenGRSDR", "2.4K"))
        self.pbF4.setText(_translate("OpenGRSDR", "2.7K"))
        self.pbF5.setText(_translate("OpenGRSDR", "3.0K"))
        self.pbF6.setText(_translate("OpenGRSDR", "3.3K"))
        self.pbF7.setText(_translate("OpenGRSDR", "3.7K"))
        self.pbF8.setText(_translate("OpenGRSDR", "4.5K"))
        self.pbF9.setText(_translate("OpenGRSDR", "VAR"))
        self.pbLpan.setText(_translate("OpenGRSDR", "L"))
        self.pbMemPan.setText(_translate("OpenGRSDR", "<<"))
        self.sbVarLowFreq.setToolTip(_translate("OpenGRSDR", "Filter Low Frequency"))
        self.sbVarHighFreq.setToolTip(_translate("OpenGRSDR", "Filter High Frequency"))
        self.label_18.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">High:  </span></p></body></html>"))
        self.label_19.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Low:  </span></p></body></html>"))
        self.pbMemUpFreq.setText(_translate("OpenGRSDR", "U"))
        self.pbMemDownFreq.setText(_translate("OpenGRSDR", "D"))
        self.label_8.setText(_translate("OpenGRSDR", "EQ: 400"))
        self.label_9.setText(_translate("OpenGRSDR", "EQ: 1.5k"))
        self.label_10.setText(_translate("OpenGRSDR", "EQ: 6k"))
        self.pbEqOn.setToolTip(_translate("OpenGRSDR", "Enable equalizer"))
        self.pbEqOn.setText(_translate("OpenGRSDR", "ON"))
        self.pbEqRx.setText(_translate("OpenGRSDR", "RX"))
        self.pbEqTx.setText(_translate("OpenGRSDR", "TX"))
        self.pbBal2.setToolTip(_translate("OpenGRSDR", "Press for centered"))
        self.pbBal2.setText(_translate("OpenGRSDR", "Bal2:"))
        self.pbRitReset.setToolTip(_translate("OpenGRSDR", "RIT reset"))
        self.pbRitReset.setText(_translate("OpenGRSDR", "RIT:"))
        self.pbXitReset.setToolTip(_translate("OpenGRSDR", "XIT reset"))
        self.pbXitReset.setText(_translate("OpenGRSDR", "XIT:"))
        self.label_21.setText(_translate("OpenGRSDR", "RX1 Vol:"))
        self.label_22.setText(_translate("OpenGRSDR", "RX2 Vol:"))
        self.pbBal1.setToolTip(_translate("OpenGRSDR", "Press for centered"))
        self.pbBal1.setText(_translate("OpenGRSDR", "Bal1:"))
        self.pbSql.setToolTip(_translate("OpenGRSDR", "Squelch Enable"))
        self.pbSql.setText(_translate("OpenGRSDR", "SQL"))
        self.pbGate.setToolTip(_translate("OpenGRSDR", "Gate Enable"))
        self.pbGate.setText(_translate("OpenGRSDR", "GATE"))
        self.slSr.setToolTip(_translate("OpenGRSDR", "Spectrum Rate"))
        self.slWr.setToolTip(_translate("OpenGRSDR", "Watterfall rate"))
        self.label_11.setText(_translate("OpenGRSDR", "SR:"))
        self.label_12.setText(_translate("OpenGRSDR", "WR:"))
        self.pbComp.setText(_translate("OpenGRSDR", "COMP"))
        self.pbCpdr.setText(_translate("OpenGRSDR", "CPDR"))
        self.label_15.setText(_translate("OpenGRSDR", "Pitch F, Hz:"))
        self.chbBreakIn.setText(_translate("OpenGRSDR", "BrIn"))
        self.label_16.setText(_translate("OpenGRSDR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Delay:</span></p></body></html>"))

import images_rc
