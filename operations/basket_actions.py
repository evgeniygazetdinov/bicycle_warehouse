from PySide2 import QtCore, QtGui, QtWidgets
from library.db import Bicycle_db
import datetime
import time


class BasketActions:
    def __init__(self):
        self.total = 0
        self.total_profit = 0
        self.total_magazine = 0
        self.total_work = 0
        self.total_expenses = 0
        self.total_advances = 0

    def get_date_time_from_widget(self, now_year, widget):
        dt = widget.dateTime()
        dt_string = dt.toString(widget.displayFormat())
        string = dt_string.split()
        day_mon = string[0]
        hour_min = string[-1]
        res = day_mon + "/" + str(now_year) + " " + hour_min + ":00"
        print(res)
        return res

    def setDefaultTime(self):
        now = datetime.datetime.now()
        from_date = QtCore.QDateTime(now.year, now.month, now.day, 00, 00, 0)
        to_date = QtCore.QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(from_date)
        self.dateTimeEdit_2.setDateTime(to_date)
        self.dateTimeEdit.setDisplayFormat("dd/MM hh:mm")
        self.dateTimeEdit_2.setDisplayFormat("dd/MM hh:mm")
        from_date_string = self.get_date_time_from_widget(now.year, self.dateTimeEdit)
        to_date_string = self.get_date_time_from_widget(now.year, self.dateTimeEdit_2)

    def basket_actions(self):
        # self.setDefaultTime()
        # self.calcutate_table_values()
        # self.pushButton_10.clicked.connect(lambda: print("3e"))
        pass

    def calcutate_table_values(self):
        #return list with values from argument
        
