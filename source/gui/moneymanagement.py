# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moneymanagement.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MoneyManagement(object):
    def setupUi(self, MoneyManagement):
        MoneyManagement.setObjectName("MoneyManagement")
        MoneyManagement.resize(1205, 759)
        self.centralwidget = QtWidgets.QWidget(MoneyManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.exitMain = QtWidgets.QPushButton(self.centralwidget)
        self.exitMain.setGeometry(QtCore.QRect(1000, 60, 181, 41))
        self.exitMain.setObjectName("exitMain")
        self.minimize_tuopan = QtWidgets.QPushButton(self.centralwidget)
        self.minimize_tuopan.setGeometry(QtCore.QRect(1000, 140, 181, 41))
        self.minimize_tuopan.setObjectName("minimize_tuopan")
        self.minimize_renwulan = QtWidgets.QPushButton(self.centralwidget)
        self.minimize_renwulan.setGeometry(QtCore.QRect(1000, 210, 181, 41))
        self.minimize_renwulan.setObjectName("minimize_renwulan")
        MoneyManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MoneyManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MoneyManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MoneyManagement)
        self.statusbar.setObjectName("statusbar")
        MoneyManagement.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MoneyManagement)
        QtCore.QMetaObject.connectSlotsByName(MoneyManagement)

    def retranslateUi(self, MoneyManagement):
        _translate = QtCore.QCoreApplication.translate
        MoneyManagement.setWindowTitle(_translate("MoneyManagement", "MainWindow"))
        self.exitMain.setText(_translate("MoneyManagement", "退出程序"))
        self.minimize_tuopan.setText(_translate("MoneyManagement", "最小化到托盘"))
        self.minimize_renwulan.setText(_translate("MoneyManagement", "最小化到任务栏"))
        self.menu.setTitle(_translate("MoneyManagement", "理财管理软件"))

