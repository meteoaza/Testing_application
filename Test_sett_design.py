# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_sett_design.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(550, 262)
        Frame.setMaximumSize(QtCore.QSize(550, 263))
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tryLine = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tryLine.sizePolicy().hasHeightForWidth())
        self.tryLine.setSizePolicy(sizePolicy)
        self.tryLine.setMaximumSize(QtCore.QSize(30, 16777215))
        self.tryLine.setObjectName("tryLine")
        self.gridLayout.addWidget(self.tryLine, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.mark2Line = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mark2Line.sizePolicy().hasHeightForWidth())
        self.mark2Line.setSizePolicy(sizePolicy)
        self.mark2Line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.mark2Line.setObjectName("mark2Line")
        self.gridLayout.addWidget(self.mark2Line, 6, 2, 1, 1)
        self.colBox = QtWidgets.QCheckBox(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colBox.sizePolicy().hasHeightForWidth())
        self.colBox.setSizePolicy(sizePolicy)
        self.colBox.setMaximumSize(QtCore.QSize(30, 16777215))
        self.colBox.setText("")
        self.colBox.setObjectName("colBox")
        self.gridLayout.addWidget(self.colBox, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        self.ranBox = QtWidgets.QCheckBox(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ranBox.sizePolicy().hasHeightForWidth())
        self.ranBox.setSizePolicy(sizePolicy)
        self.ranBox.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ranBox.setText("")
        self.ranBox.setObjectName("ranBox")
        self.gridLayout.addWidget(self.ranBox, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.mark5Line = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mark5Line.sizePolicy().hasHeightForWidth())
        self.mark5Line.setSizePolicy(sizePolicy)
        self.mark5Line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.mark5Line.setObjectName("mark5Line")
        self.gridLayout.addWidget(self.mark5Line, 3, 2, 1, 1)
        self.mark4Line = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mark4Line.sizePolicy().hasHeightForWidth())
        self.mark4Line.setSizePolicy(sizePolicy)
        self.mark4Line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.mark4Line.setObjectName("mark4Line")
        self.gridLayout.addWidget(self.mark4Line, 4, 2, 1, 1)
        self.mark3Line = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mark3Line.sizePolicy().hasHeightForWidth())
        self.mark3Line.setSizePolicy(sizePolicy)
        self.mark3Line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.mark3Line.setObjectName("mark3Line")
        self.gridLayout.addWidget(self.mark3Line, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Настройки"))
        self.label_4.setText(_translate("Frame", "Оценка 5"))
        self.label_11.setText(_translate("Frame", "%"))
        self.label_9.setText(_translate("Frame", "%"))
        self.label_10.setText(_translate("Frame", "%"))
        self.label_8.setText(_translate("Frame", "%"))
        self.label_3.setText(_translate("Frame", "Количество вопросов"))
        self.label_2.setText(_translate("Frame", "Случайный выбор"))
        self.label_6.setText(_translate("Frame", "Оценка 3"))
        self.label_5.setText(_translate("Frame", "Оценка 4"))
        self.label.setText(_translate("Frame", "Подсказка цветом"))
        self.label_7.setText(_translate("Frame", "Оценка 2"))


