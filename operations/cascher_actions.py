from PySide2 import QtCore, QtGui, QtWidgets
from library.db import Bicycle_db
import datetime
import time


class BasketActions:
    def get_date_time_from_widget(self, now_year, widget):
        dt = widget.dateTime()
        dt_string = dt.toString(widget.displayFormat())
        string = dt_string.split()

        day_mon = string[0]
        day = (day_mon.split("/"))[0]
        mon = (day_mon.split("/"))[-1]
        day_mon = mon + "/" + day
        hour_min = string[-1]
        res = day_mon + "/" + str(now_year)[-2:] + " " + hour_min + ":00"
        return res

    def setDefaultTime(self):
        now = datetime.datetime.now()
        from_date = QtCore.QDateTime(now.year, now.month, now.day, 00, 00, 0)
        to_date = QtCore.QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(from_date)
        self.dateTimeEdit_2.setDateTime(to_date)
        self.dateTimeEdit.setDisplayFormat("dd/MM hh:mm")
        self.dateTimeEdit_2.setDisplayFormat("dd/MM hh:mm")
        self.get_basket_items_by_date()

    def get_basket_items_by_date(self):
        self.tableWidget_6.clean_table()
        now = datetime.datetime.now()
        from_date_string = self.get_date_time_from_widget(now.year, self.dateTimeEdit)
        to_date_string = self.get_date_time_from_widget(now.year, self.dateTimeEdit_2)
        self.tableWidget_6.display_items(from_date_string, to_date_string)

    def basket_actions(self):
        self.setDefaultTime()
        self.pushButton_10.clicked.connect(self.get_basket_items_by_date)
