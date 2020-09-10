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

    def update_labels(self):
        def calculate_by(dict_with_values,value_for_calculate):
            total = 0
            for item in dict_with_values:
                total+= int(item[value_for_calculate])
            return total

        all_usiall_buy = self.tableWidget_6.find_values_in_table("ПР",6)
        all_works = self.tableWidget_6.find_values_in_table("PБ",6)
        all_sales = self.tableWidget_6.find_values_in_table("CK",6)
        all_expense = self.tableWidget_6.find_values_in_table('PC',6)
        all_prepaid = self.tableWidget_6.find_values_in_table("AB",6)

    
        
        profit_usiall_buy = calculate_by(all_usiall_buy, 'Прибыль')
        profit_works = calculate_by(all_works, 'Прибыль')
        profit_sales = calculate_by(all_sales, 'Прибыль')


        sum_usiall_buy = calculate_by(all_usiall_buy,"Сумма" )
        sum_works = calculate_by(all_works,"Сумма" )
        sum_sales = calculate_by(all_sales,"Сумма" )
        sum_expense =  calculate_by(all_expense,"Сумма" )
        sum_prepaid = calculate_by(all_prepaid,"Сумма" )


        total_profit = (profit_usiall_buy + profit_works) + profit_sales
        total_sum = (sum_usiall_buy + sum_works) + sum_sales
        total_magazine = (sum_usiall_buy + sum_sales)
        total_work = sum_works
        total_expense = sum_expense
        total_prepaid = sum_prepaid
        self.label_17.setText(str(total_sum))
        self.label_19.setText(str(total_profit))
        self.label_32.setText(str(total_magazine))
        self.label_34.setText(str(total_work))
        self.label_36.setText(str(total_expense))
        self.label_40.setText(str(total_prepaid))




    def get_basket_items_by_date(self):
        self.tableWidget_6.clean_table()
        now = datetime.datetime.now()
        from_date_string = self.get_date_time_from_widget(now.year, self.dateTimeEdit)
        to_date_string = self.get_date_time_from_widget(now.year, self.dateTimeEdit_2)
        self.tableWidget_6.display_items(from_date_string, to_date_string)
        self.update_labels()
       
    
    def basket_actions(self):
        self.setDefaultTime()
        self.pushButton_10.clicked.connect(self.get_basket_items_by_date)
