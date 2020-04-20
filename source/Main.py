import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt

from source.pages.MoneyManagement import MoneyManagement

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = MoneyManagement(MainWindow)

    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    # MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
    # MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
    MainWindow.show()
    sys.exit(app.exec_())
