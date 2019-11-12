# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\qq567\Documents\code\DS_homework\course_design\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.letKeyword = QtWidgets.QLineEdit(self.centralwidget)
        self.letKeyword.setGeometry(QtCore.QRect(70, 40, 411, 21))
        self.letKeyword.setObjectName("letKeyword")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(490, 40, 75, 23))
        self.btnSearch.setObjectName("btnSearch")
        self.lblSearch = QtWidgets.QLabel(self.centralwidget)
        self.lblSearch.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.lblSearch.setObjectName("lblSearch")
        self.tbrList = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbrList.setGeometry(QtCore.QRect(70, 70, 491, 611))
        self.tbrList.setObjectName("tbrList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.letKeyword.returnPressed.connect(self.btnSearch.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DYJ的sina搜索"))
        self.letKeyword.setText(_translate("MainWindow", "（请在此处输入关键字）"))
        self.btnSearch.setText(_translate("MainWindow", "开始搜索"))
        self.lblSearch.setText(_translate("MainWindow", "关键字："))

