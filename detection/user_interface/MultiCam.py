 -*- coding: utf-8 -*-

#**************************** Designed by Bekir ÖZTÜRK ************


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 510)
        MainWindow.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"background-color: rgb(30, 0, 0);\n"
"background-color: rgb(20, 25, 75);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.toolButton_restore = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_restore.sizePolicy().hasHeightForWidth())
        self.toolButton_restore.setSizePolicy(sizePolicy)
        self.toolButton_restore.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_restore.setMaximumSize(QtCore.QSize(45, 45))
        self.toolButton_restore.setStyleSheet("QToolButton{\n"
"border-radius:8px;\n"
"    \n"
"    \n"
"    image: url(:/icon/icons8-restore-window-48.png);\n"
"}\n"
"QToolButton:pressed {\n"
"\n"
"padding :4px;\n"
"\n"
"\n"
"}\n"
"QToolButton:hover {\n"
"border-radius:10px;\n"
" border: 1px solid  rgb(136, 138, 133); \n"
"background-color:rgb(83, 82, 87);\n"
"\n"
"  \n"
"}")
        self.toolButton_restore.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-restore-window-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_restore.setIcon(icon)
        self.toolButton_restore.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_restore.setShortcut("")
        self.toolButton_restore.setAutoRaise(True)
        self.toolButton_restore.setObjectName("toolButton_restore")
        self.horizontalLayout_10.addWidget(self.toolButton_restore)
        self.toolButton_exit = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_exit.sizePolicy().hasHeightForWidth())
        self.toolButton_exit.setSizePolicy(sizePolicy)
        self.toolButton_exit.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_exit.setMaximumSize(QtCore.QSize(45, 45))
        self.toolButton_exit.setStyleSheet("QToolButton{\n"
"border-radius:8px;\n"
"    \n"
"    image: url(:/icon/exit.png);\n"
"}\n"
"QToolButton:pressed {\n"
"\n"
"padding :12px;\n"
"\n"
"\n"
"\n"
"}\n"
"QToolButton:hover {\n"
"border-radius:10px;\n"
" border: 1px solid  rgb(136, 138, 133); \n"
"background-color:rgb(83, 82, 87);\n"
"\n"
"  \n"
"}")
        self.toolButton_exit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_exit.setIcon(icon1)
        self.toolButton_exit.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_exit.setShortcut("")
        self.toolButton_exit.setAutoRaise(True)
        self.toolButton_exit.setObjectName("toolButton_exit")
        self.horizontalLayout_10.addWidget(self.toolButton_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Screen_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Screen_1.sizePolicy().hasHeightForWidth())
        self.Screen_1.setSizePolicy(sizePolicy)
        self.Screen_1.setMaximumSize(QtCore.QSize(700, 700))
        self.Screen_1.setStyleSheet("QLabel{\n"
"border: 1px solid rgb(114, 159, 207);\n"
"    \n"
"    image: url(:/icons/icons8-no-camera-48.png);\n"
"}")
        self.Screen_1.setFrameShape(QtWidgets.QFrame.Box)
        self.Screen_1.setText("")
        self.Screen_1.setObjectName("Screen_1")
        self.horizontalLayout_11.addWidget(self.Screen_1)
        self.Screen_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Screen_2.sizePolicy().hasHeightForWidth())
        self.Screen_2.setSizePolicy(sizePolicy)
        self.Screen_2.setMaximumSize(QtCore.QSize(700, 700))
        self.Screen_2.setStyleSheet("QLabel{\n"
"border: 1px solid rgb(114, 159, 207);\n"
"        \n"
"    image: url(:/icons/icons8-no-camera-48.png);\n"
"}")
        self.Screen_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Screen_2.setText("")
        self.Screen_2.setObjectName("Screen_2")
        self.horizontalLayout_11.addWidget(self.Screen_2)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 23pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 202, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.Button_Play_Pause_1 = QtWidgets.QToolButton(self.centralwidget)
        self.Button_Play_Pause_1.setStyleSheet("QToolButton{\n"
"    border-radius:5px;\n"
"    image: url(:/icons/icons8-play-96.png);\n"
"}\n"
"QToolButton:checked {\n"
"    border-radius:5px;\n"
"    image: url(:/icons/icons8-pause-48.png);\n"
"    background-color:rgb(83, 82, 87);\n"
"    padding :2px;\n"
"}\n"
"QToolButton:hover {\n"
"    border-radius:5px;\n"
"     border: 1px solid  rgb(136, 138, 133); \n"
"    background-color:rgb(83, 82, 87);\n"
"}\n"
"")
        self.Button_Play_Pause_1.setText("")
        self.Button_Play_Pause_1.setIconSize(QtCore.QSize(40, 40))
        self.Button_Play_Pause_1.setCheckable(True)
        self.Button_Play_Pause_1.setChecked(False)
        self.Button_Play_Pause_1.setObjectName("Button_Play_Pause_1")
        self.horizontalLayout_2.addWidget(self.Button_Play_Pause_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.Button_Play_Pause_2 = QtWidgets.QToolButton(self.centralwidget)
        self.Button_Play_Pause_2.setStyleSheet("QToolButton{\n"
"    border-radius:5px;\n"
"    image: url(:/icons/icons8-play-96.png);\n"
"}\n"
"QToolButton:checked {\n"
"    border-radius:5px;\n"
"    image: url(:/icons/icons8-pause-96.png);\n"
"    background-color:rgb(83, 82, 87);\n"
"    padding :2px;\n"
"}\n"
"QToolButton:hover {\n"
"    border-radius:5px;\n"
"     border: 1px solid  rgb(136, 138, 133); \n"
"    background-color:rgb(83, 82, 87);\n"
"}")
        self.Button_Play_Pause_2.setText("")
        self.Button_Play_Pause_2.setIconSize(QtCore.QSize(40, 40))
        self.Button_Play_Pause_2.setCheckable(True)
        self.Button_Play_Pause_2.setChecked(False)
        self.Button_Play_Pause_2.setObjectName("Button_Play_Pause_2")
        self.horizontalLayout_6.addWidget(self.Button_Play_Pause_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 20)
        self.verticalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolButton_exit.clicked.connect(MainWindow.close)
        self.toolButton_restore.clicked.connect(MainWindow.showFullScreen)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_restore.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Restore</span></p></body></html>"))
        self.toolButton_exit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Ctrl+Q</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Detectron2"))
        self.label_2.setText(_translate("MainWindow", "MobileNet SSD"))
import sys
sys.path.insert(1, './icons')
import icons_rc

