# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_design.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 779)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1184, 779))
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0.329773, angle:0, stop:0.0227273 rgba(27, 124, 158, 192), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.answer3 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer3.sizePolicy().hasHeightForWidth())
        self.answer3.setSizePolicy(sizePolicy)
        self.answer3.setMinimumSize(QtCore.QSize(0, 0))
        self.answer3.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer3.setFont(font)
        self.answer3.setObjectName("answer3")
        self.gridLayout.addWidget(self.answer3, 4, 1, 1, 1)
        self.answer5 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer5.sizePolicy().hasHeightForWidth())
        self.answer5.setSizePolicy(sizePolicy)
        self.answer5.setMinimumSize(QtCore.QSize(0, 0))
        self.answer5.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer5.setFont(font)
        self.answer5.setObjectName("answer5")
        self.gridLayout.addWidget(self.answer5, 6, 1, 1, 1)
        self.answer4 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer4.sizePolicy().hasHeightForWidth())
        self.answer4.setSizePolicy(sizePolicy)
        self.answer4.setMinimumSize(QtCore.QSize(0, 0))
        self.answer4.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer4.setFont(font)
        self.answer4.setObjectName("answer4")
        self.gridLayout.addWidget(self.answer4, 5, 1, 1, 1)
        self.checkBox5 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox5.sizePolicy().hasHeightForWidth())
        self.checkBox5.setSizePolicy(sizePolicy)
        self.checkBox5.setText("")
        self.checkBox5.setObjectName("checkBox5")
        self.gridLayout.addWidget(self.checkBox5, 6, 0, 1, 1)
        self.checkBox4 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox4.sizePolicy().hasHeightForWidth())
        self.checkBox4.setSizePolicy(sizePolicy)
        self.checkBox4.setText("")
        self.checkBox4.setObjectName("checkBox4")
        self.gridLayout.addWidget(self.checkBox4, 5, 0, 1, 1)
        self.question = QtWidgets.QTextBrowser(self.centralwidget)
        self.question.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.question.setFont(font)
        self.question.setStyleSheet("alternate-background-color: qconicalgradient(cx:1, cy:0.329773, angle:0,\n"
"                         stop:0.295455 rgba(46, 124, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"                     ")
        self.question.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.question.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.question.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.question.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.question.setObjectName("question")
        self.gridLayout.addWidget(self.question, 0, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.print.sizePolicy().hasHeightForWidth())
        self.print.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.print.setFont(font)
        self.print.setAutoFillBackground(False)
        self.print.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\n"
"                                 stop:0.215909 rgba(38, 174, 23, 255), stop:1 rgba(255, 255, 255, 255));\n"
"                             ")
        self.print.setObjectName("print")
        self.gridLayout_3.addWidget(self.print, 0, 2, 1, 1)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setAutoFillBackground(False)
        self.next.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\n"
"                                 stop:0.215909 rgba(38, 174, 23, 255), stop:1 rgba(255, 255, 255, 255));\n"
"                             ")
        self.next.setObjectName("next")
        self.gridLayout_3.addWidget(self.next, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 8, 1, 2, 1)
        self.checkBox3 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox3.sizePolicy().hasHeightForWidth())
        self.checkBox3.setSizePolicy(sizePolicy)
        self.checkBox3.setText("")
        self.checkBox3.setObjectName("checkBox3")
        self.gridLayout.addWidget(self.checkBox3, 4, 0, 1, 1)
        self.answer2 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer2.sizePolicy().hasHeightForWidth())
        self.answer2.setSizePolicy(sizePolicy)
        self.answer2.setMinimumSize(QtCore.QSize(0, 0))
        self.answer2.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer2.setFont(font)
        self.answer2.setObjectName("answer2")
        self.gridLayout.addWidget(self.answer2, 3, 1, 1, 1)
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox1.sizePolicy().hasHeightForWidth())
        self.checkBox1.setSizePolicy(sizePolicy)
        self.checkBox1.setText("")
        self.checkBox1.setObjectName("checkBox1")
        self.gridLayout.addWidget(self.checkBox1, 2, 0, 1, 1)
        self.answer1 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer1.sizePolicy().hasHeightForWidth())
        self.answer1.setSizePolicy(sizePolicy)
        self.answer1.setMinimumSize(QtCore.QSize(0, 0))
        self.answer1.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer1.setFont(font)
        self.answer1.setObjectName("answer1")
        self.gridLayout.addWidget(self.answer1, 2, 1, 1, 1)
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox2.sizePolicy().hasHeightForWidth())
        self.checkBox2.setSizePolicy(sizePolicy)
        self.checkBox2.setText("")
        self.checkBox2.setObjectName("checkBox2")
        self.gridLayout.addWidget(self.checkBox2, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.infoLine = QtWidgets.QLabel(self.centralwidget)
        self.infoLine.setMinimumSize(QtCore.QSize(700, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.infoLine.setFont(font)
        self.infoLine.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.infoLine.setFrameShape(QtWidgets.QFrame.Box)
        self.infoLine.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoLine.setText("")
        self.infoLine.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLine.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoLine.setObjectName("infoLine")
        self.gridLayout.addWidget(self.infoLine, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setStyleSheet("color: rgb(0, 0, 161);")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.menu.addAction(self.open)
        self.menu.addAction(self.settings)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menu.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TECT_M"))
        self.question.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Rounded MT Bold\'; font-size:25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                         </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                          </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                      </p></body></html>"))
        self.print.setText(_translate("MainWindow", "Печать"))
        self.next.setText(_translate("MainWindow", "Далее"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.settings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.about.setText(_translate("MainWindow", "О программе"))


