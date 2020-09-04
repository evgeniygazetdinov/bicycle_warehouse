from widgets.main_table import CustomTableWithGoods
from PySide2 import QtWidgets
from library.db import Bicycle_db
import datetime


class CustomCashierTable(CustomTableWithGoods):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)
        # self.display_items()
        # date_from.setDate(QDate(datetime.now()-timedelta(days=7)))
        # date_to.setDate(QDate(datetime.now()-timedelta(days=7)))




    def display_items(self, date_from, date_by):
        def get_casher_elements():
            query = f'SELECT * from basket where dated between {date_from} and {date_by}'
            db = Bicycle_db()
            res = (db.insert(query))
            return res

        def from_sql_to_dict(goods):
            res = tuple()
            for value in goods:
                ids = value[0]
                price = value[2]
                qty = value[3]
                total_price = value[4]
                article = value[5]
                payment = value[6]
                profit = value[7]
                dated = value[8]
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
        list_with_goods = from_sql_to_dict(items)
        # row = len(list_with_goods)
        # self.insertRow(row)
        # self.setRowCount(row)
        # self.setSortingEnabled(False)
        # self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # for good in list_with_goods:
        #     row -= 1
        #     item = NumericItem()
        #     item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        #     item.setData(QtCore.Qt.DisplayRole, good["article"])
        #     self.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
        #     item.setData(QtCore.Qt.DisplayRole, good["name"])
        #     self.setItem(row, 1, QtWidgets.QTableWidgetItem(item))

        #     if good["buy"] == int(good["buy"]):
        #         item.setData(QtCore.Qt.DisplayRole, int(good["buy"]))
        #         self.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
        #     else:
        #         item.setData(QtCore.Qt.DisplayRole, good["buy"])
        #         self.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
        #     if good["sell"] == int(good["sell"]):
        #         item.setData(QtCore.Qt.DisplayRole, int(good["sell"]))
        #         self.setItem(row, 4, QtWidgets.QTableWidgetItem(item))
        #     else:
        #         item.setData(QtCore.Qt.DisplayRole, (good["sell"]))
        #         self.setItem(row, 4, QtWidgets.QTableWidgetItem(item))
        #     item = ProcentItem()
        #     item.setData(
        #         QtCore.Qt.EditRole,
        #         str(self.calculate_sell_price(good["sell"], good["buy"]))+'%',
        #     )
        #     self.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
        #     item = NumericItem()
        #     item.setData(QtCore.Qt.DisplayRole, (good["qty"]))
        #     self.setItem(row, 5, QtWidgets.QTableWidgetItem(item))
        #     item.setData(QtCore.Qt.DisplayRole, (good["sell_uah"]))
        #     self.setItem(row, 6, QtWidgets.QTableWidgetItem(item))
        # self.setSortingEnabled(True)
        # self.horizontalHeader().sortIndicatorOrder()
        # self.sortItems(3, Qt.AscendingOrder)