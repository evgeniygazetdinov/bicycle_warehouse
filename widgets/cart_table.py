from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog
from widgets.good_form import GoodsForm
from widgets.main_table import CustomTableWithGoods
from library.db import Bicycle_db


class CartTable(CustomTableWithGoods):
    def __init__(self, parent=None, profit=None, total=None):
        QtWidgets.QTableWidget.__init__(self, parent)

        self.sortItems(0, QtCore.Qt.AscendingOrder)
        self.setSortingEnabled(True)
        self.profit = profit
        self.total = total

    def get_values_from_cart(self):
        names = []
        values = []
        in_cart = []
        if self.rowCount():
            row = self.rowCount()
            column = self.columnCount()
            #
            for x in range(self.rowCount()):
                for i in range(column):
                    names.append(self.horizontalHeaderItem(i).text())
                for i in range(column):
                    values.append(self.item(x, i).text())

                in_cart.append(dict(zip(names, values)))
            return in_cart

    def clean_table(self):
        while self.rowCount() > 0:
            self.removeRow(0)
        if self.profit:
            self.profit.setText("")
        if self.total:
            self.total.setText("")

    def contextMenuEvent(self, event):
        pass
