# -*- coding: utf-8 -*-
from widgets.cart_table import CartTable
from widgets.custom_widgets import NumericItem, ProcentItem
from PySide2 import QtWidgets, Qt, QtCore
from library.db import Bicycle_db
import datetime
import re


class CustomCashierTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)

    def display_items(self, date_from, date_by):
        def get_casher_elements():
            query = f'SELECT * from basket where dated between "{date_from}" and "{date_by}"'
            db = Bicycle_db()
            res = db.insert(query)
            return res

        def find_type_by_name(name):
            if re.match(r"Аванс", name, re.IGNORECASE):
                return "AB"
            if name == "Знижка":
                return "CK"
            if (
                name == "Матеріали майстерні"
                or re.match(r"Собівартість", name, re.IGNORECASE)
                or re.match(r"Витрати", name, re.IGNORECASE)
            ):
                return "PC"
            if name == "Робота майстерні":
                return "PБ"
            else:
                return "ПР"

        def from_sql_to_dict(goods):
            res = tuple()
            print(len(goods))
            for value in goods:
                ids = value[0]
                price = value[1]
                qty = value[2]
                total_price = value[3]
                article = value[4]
                payment = value[5]
                profit = value[6]
                dated = value[7]
                name = value[9]
                data = {
                    "id": ids,
                    "price": price,
                    "qty": qty,
                    "total_price": total_price,
                    "article": article,
                    "payment": payment,
                    "profit": profit,
                    "dated": dated,
                    "name": name,
                }
                res += (data,)
            return res

        items = get_casher_elements()
        try:
            print(items[1])
        except:
            pass
        list_with_goods = from_sql_to_dict(items)
        try:
            print(list_with_goods[1])
        except:
            pass
        row = len(list_with_goods)
        self.insertRow(row)
        self.setRowCount(row)
        self.setSortingEnabled(False)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        for good in list_with_goods:
            row -= 1
            item = NumericItem()
            # item.setFlags(Qt.ItemIsEditable)
            item.setData(QtCore.Qt.DisplayRole, good["dated"])
            self.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, good["article"])
            self.setItem(row, 1, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["name"]))
            self.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, good["qty"])
            self.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["total_price"]))
            self.setItem(row, 4, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.EditRole, good["profit"])
            self.setItem(row, 5, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (find_type_by_name(good["name"])))
            self.setItem(row, 6, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["payment"]))
            self.setItem(row, 7, QtWidgets.QTableWidgetItem(item))
        self.setSortingEnabled(True)
        self.horizontalHeader().sortIndicatorOrder()

    def clean_table(self):
        while self.rowCount() > 0:
            self.removeRow(0)

    def find_values_in_table(self, find_by_value, need_column):
        def row_parser(self, row):
            columns = self.columnCount()
            names = []
            values = []

            for i in range(columns):
                names.append(self.horizontalHeaderItem(i).text())
            for i in range(columns):
                    values.append(self.item(row, i).text())
            return dict(zip(names, values))

        res = []
        rows = self.rowCount()
        for row in range(rows):
            row_value = self.item(row,need_column).text()
            if find_by_value == row_value:
                res.append(row_parser(self,row))
        return res