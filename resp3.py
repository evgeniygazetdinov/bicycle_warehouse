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
from PySide2 import QtWidgets


class Example(QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        table = QTableWidget()
        table.show()
        hbox = QHBoxLayout()
        # hbox.setGeometry(10,100,100,100)
        hbox.addStretch(10000)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addWidget(table)
        vbox.addStretch(100)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Buttons")
