#!/usr/bin/python
import sys
from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication,
    QTableWidget,
    QMainWindow,
)
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import *


class Example(QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

    def initUI(self, window):
        window.setObjectName("MainWindow")
        window.resize(800, 600)
        self.vLayoutMain = QVBoxLayout()
        self.tab = QTabWidget()
        self.Widget1 = QWidget(self.tab)
        self.vLayoutTab1 = QVBoxLayout()
        self.Table1 = QTableWidget(self.tab)
        self.Widget2 = QWidget(self.tab)
        self.vLayoutTab2 = QVBoxLayout()
        self.Table2 = QTableWidget
        self.Table1 = QTableWidget(5, 5, self.Widget1)
        self.vLayoutTab1.addWidget(self.Table1)
        self.tab.addTab(self.Widget1, "Tab 1")
        self.Table2 = QTableWidget(5, 5, self.Widget2)
        self.vLayoutTab2.addWidget(self.Table2)
        self.tab.addTab(self.Widget2, "Tab 2")

        self.vLayoutMain.addWidget(self.tab)
        # self.tab.setCurrentIndex(0)
        self.tab.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Example()
    ui.initUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
