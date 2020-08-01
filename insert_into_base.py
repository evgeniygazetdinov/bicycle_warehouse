import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel,QDialog)
from db import Bicycle_db

class Insert_Into_Window(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
                          # <===

    def setupUi(self, Insert_FORM):
        Insert_FORM.setObjectName("Insert_FORM")
        Insert_FORM.resize(940, 220)
        self.tableWidget = QtWidgets.QTableWidget(Insert_FORM)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 801, 721))
        self.tableWidget.setMaximumSize(QtCore.QSize(801, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Aрт.Ст")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(192, 252, 187))
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton = QtWidgets.QPushButton(Insert_FORM)
        self.pushButton.setGeometry(QtCore.QRect(810, 10, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Insert_FORM)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 140, 111, 41))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color:green")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Insert_FORM)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 40, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Insert_FORM)
        QtCore.QMetaObject.connectSlotsByName(Insert_FORM)

    def retranslateUi(self, Insert_FORM):
        _translate = QtCore.QCoreApplication.translate
        Insert_FORM.setWindowTitle(_translate("Insert_FORM", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Insert_FORM", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Insert_FORM", "Арт.H"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Insert_FORM", "Название"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Insert_FORM", "закупка"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Insert_FORM", "нац"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Insert_FORM", "Продаж."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Insert_FORM", "К-ть"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Insert_FORM", "ГРН"))
        self.pushButton.setText(_translate("Insert_FORM", "добавить строку"))
        self.pushButton_2.setText(_translate("Insert_FORM", "загрузить в базу"))
        self.pushButton_3.setText(_translate("Insert_FORM", "удалить строку"))
        self.add_action()


    def add_action(self):
        self.pushButton.clicked.connect(self.add_row)
        self.pushButton_3.clicked.connect(self.remove_row)
        self.pushButton_2.clicked.connect(self.upload_to_base)


    def add_row(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def remove_row(self,selected):
        rowPosition = self.tableWidget.rowCount()
        if rowPosition <= 1:
            pass
        else:
            self.tableWidget.removeRow(rowPosition-1)
    
        
            

    def get_values_from_table(self):
        values = []
        headers = []
        for column in range(self.tableWidget.columnCount()):
            header = self.tableWidget.horizontalHeaderItem(column)
            if header is not None:
                    headers.append(header.text())
        for row in range(self.tableWidget.rowCount()):
            rowdata = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    rowdata.append(item.text())
                else:
                    rowdata.append('""')

            values.append(dict(zip(headers,rowdata)))
        return values
    
    def upload_to_base(self):
        res = []
        db = Bicycle_db()
        #add course
        values = self.get_values_from_table()
        for row in values:
            values = ','.join(map(str, row.values()))
            db.edit("insert into goods(article, article_old, name, qty, buy, profit, category, sell_uah ) values({});".format(values))
        print('executed')
        


 