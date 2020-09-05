from widgets.cart_table import CartTable
from widgets.custom_widgets import NumericItem, ProcentItem
from PySide2 import QtWidgets, Qt, QtCore
from library.db import Bicycle_db
import datetime


class CustomCashierTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)

    



    def display_items(self, date_from, date_by):
        def get_casher_elements():
            query = f'SELECT * from basket where dated between "{date_from}" and "{date_by}"'
            db = Bicycle_db()
            res = (db.insert(query))
            return res

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
                    "name": name
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
            item.setData(QtCore.Qt.EditRole,good["profit"])
            self.setItem(row, 5, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["profit"]))
            self.setItem(row, 6, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["payment"]))
            self.setItem(row, 7, QtWidgets.QTableWidgetItem(item))
        self.setSortingEnabled(True)
        self.horizontalHeader().sortIndicatorOrder()

    def clean_table(self):
        while self.rowCount() > 0:
            self.removeRow(0)
