# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cat.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 80, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 0, 80, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 121, 31))
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 60, 194, 25))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(0, 90, 194, 25))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 60, 101, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.cashier = QtWidgets.QListView(self.centralwidget)
        self.cashier.setGeometry(QtCore.QRect(0, 120, 801, 181))
        self.cashier.setObjectName("cashier")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 0, 80, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.dateTimeEdit.raise_()
        self.dateTimeEdit_2.raise_()
        self.pushButton_4.raise_()
        self.cashier.raise_()
        self.pushButton.raise_()
        self.pushButton_5.raise_()
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        self.pushButton_4.clicked.connect(self.cashier.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.pushButton.setText(_translate("Window", "Tовары"))
        self.pushButton_2.setText(_translate("Window", "Касса/Стат"))
        self.pushButton_3.setText(_translate("Window", "Наличие"))
        self.label.setText(_translate("Window", "TextLabel"))
        self.pushButton_4.setText(_translate("Window", "показать"))
        self.pushButton_5.setText(_translate("Window", "PushButton"))

