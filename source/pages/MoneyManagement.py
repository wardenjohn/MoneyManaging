import cv2
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QMenu, QAction
from source.gui.moneymanagement import Ui_MoneyManagement

class MoneyManagement(Ui_MoneyManagement):
    def __init__(self, MoneyManagement):
        super().setupUi(MoneyManagement)
        self.exitMain.clicked.connect(self.exit_main)
        self.minimize_tuopan.clicked.connect(self.minimize_to_tuopan)
        self.minimize_renwulan.clicked.connect(self.minimize_to_mission)

    def exit_main(self):
        exit(0)

    def minimize_to_tuopan(self):
        self.tray = QSystemTrayIcon()  # 创建系统托盘对象
        self.icon = QIcon('./../../resource/money_mini.ico')  # 创建图标
        self.tray.setIcon(self.icon)  # 设置系统托盘图标
        self.tray.activated.connect(self.iconClicked)  # 设置托盘点击事件处理函数
        self.tray_menu = QMenu(QApplication.desktop())  # 创建菜单
        self.RestoreAction = QAction(u'还原 ', self, self.show)  # 添加一级菜单动作选项(还原主窗口)
        # self.QuitAction = QAction(u'退出 ', self, triggered=qApp.quit)  # 添加一级菜单动作选项(退出程序)
        self.tray_menu.addAction(self.RestoreAction)  # 为菜单添加动作
        # self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu)  # 设置系统托盘菜单

    def minimize_to_mission(self):
        exit(0)

    def iconClicked(self, reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        print('click')
        if reason == 1:  # 2是双击
            self.show()

    def show(self):
        try:
            self.parent_window.show()
        except Exception as e:
            print(e)
