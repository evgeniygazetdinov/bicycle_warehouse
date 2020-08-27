from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog
from widgets.good_form import GoodsForm
from widgets.custom_widgets import NumericItem,ProcentItem
from library.db import Bicycle_db


class CustomTableWithGoods(QtWidgets.QTableWidget):
    def __init__(self, parent=None, values=None, category_widget=None):
        QtWidgets.QTableWidget.__init__(self, parent)
        self.values = values
        self.last_added_category = "Всі"
        self.category_widget = category_widget
        self.sortItems(0, QtCore.Qt.AscendingOrder)
        self.setSortingEnabled(True)
        self.goods_from_table = []
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def parse_row(self, by_row=None):
        columns = self.columnCount()
        names = []
        values = []

        for i in range(columns):
            names.append(self.horizontalHeaderItem(i).text())
        if by_row:
            for i in range(columns):
                values.append(self.item(by_row, i).text())
        else:
            for i in range(columns):
                values.append(self.item(self.currentRow(), i).text())
        return dict(zip(names, values))

    def find_in_table_by_name(self, name_for_search):
        res = []
        rows = self.rowCount()
        for row in range(rows):
            if self.item(row, 0).text() == name_for_search:
                # value = self.parse_row(row)
                return row

    def from_sqlgoods_to_dict(self, goods):
        res = tuple()
        for value in goods:
            # article_old = value[0]
            name = value[1]
            qty = value[2]
            buy = value[3]
            sell = value[4]
            profit = value[5]
            category = value[6]
            currency = value[7]
            sell_uah = value[8]
            article = value[9]
            data = {
                "name": name,
                "qty": qty,
                "buy": buy,
                "sell": sell,
                "profit": profit,
                "category": category,
                "currency": currency,
                "sell_uah": sell_uah,
                "article": article,
            }
            res += (data,)
            self.goods_from_table = res
        return res

    def get_goods(self, category_name=False, display_all=None):
        db = Bicycle_db()
        if display_all or category_name == "Всі":
            goods = db.edit("Select * from goods")
            db.close()
            return self.from_sqlgoods_to_dict(goods)
        else:
            if category_name is None:
                category_name = "Всі"
            category_id = db.select(
                'SELECT id from categories  where name like "%{}%"'.format(
                    category_name
                )
            )
            goods = db.edit(
                'Select * from goods where category like "%{}%";'.format(category_id[0])
            )
            db.close()
            return self.from_sqlgoods_to_dict(goods)

    def calculate_sell_price(self, sell, buy):
        dif = abs(float(buy) - float(sell))
        return int(str(int(round((dif / buy) * 100, 1))))

    def display_goods(self, category=False, for_search=False):
        list_with_goods = []
        if category:
            list_with_goods = self.get_goods(category)
        else:
            list_with_goods = self.get_goods(display_all=True)
        row = len(list_with_goods)
        self.insertRow(row)
        self.setRowCount(row)
        self.setSortingEnabled(False)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        for good in list_with_goods:
            row -= 1
            item = NumericItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.DisplayRole, good["article"])
            self.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, good["name"])
            self.setItem(row, 1, QtWidgets.QTableWidgetItem(item))

            if good["buy"] == int(good["buy"]):
                item.setData(QtCore.Qt.DisplayRole, int(good["buy"]))
                self.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
            else:
                item.setData(QtCore.Qt.DisplayRole, good["buy"])
                self.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
            if good["sell"] == int(good["sell"]):
                item.setData(QtCore.Qt.DisplayRole, int(good["sell"]))
                self.setItem(row, 4, QtWidgets.QTableWidgetItem(item))
            else:
                item.setData(QtCore.Qt.DisplayRole, (good["sell"]))
                self.setItem(row, 4, QtWidgets.QTableWidgetItem(item))
            item = ProcentItem()
            item.setData(
                QtCore.Qt.EditRole,
                str(self.calculate_sell_price(good["sell"], good["buy"]))+'%',
            )
            self.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
            item = NumericItem()
            item.setData(QtCore.Qt.DisplayRole, (good["qty"]))
            self.setItem(row, 5, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["sell_uah"]))
            self.setItem(row, 6, QtWidgets.QTableWidgetItem(item))
        self.setSortingEnabled(True)
        self.horizontalHeader().sortIndicatorOrder()
        self.sortItems(3, Qt.AscendingOrder)
    
    def clean_table(self):
        while self.rowCount() > 0:
            self.removeRow(0)

    def update_table(self):
        db = Bicycle_db()
        cat = "Всі"
        self.display_goods()

    def remove_values_from_row(self):
        pass

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu(self)
        add_Action = menu.addAction("добавить")
        edit_Action = menu.addAction("редактировать")
        remove_Action = menu.addAction("удалить")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == add_Action:
            widget = QDialog()
            ui = GoodsForm(table=self)
            ui.setupUi(widget)
            widget.exec_()
        if action == remove_Action:
            reply = QtWidgets.QMessageBox.question(
                self,
                "Удалить товар?",
                "Вы уверенны что хотите удалить?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No,
            )
            if reply == QtWidgets.QMessageBox.Yes:
                values = self.parse_row()
                if values["Кол-во."] != "0":
                    # widget = QDialog()
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.showMessage("товар с количеством удалить нельзя")
                else:
                    db = Bicycle_db()
                    db.insert(
                        "DELETE FROM goods WHERE article LIKE '%{}%'".format(
                            values["Арт"]
                        )
                    )
                    self.update_table()
                    db.close()

        if action == edit_Action:
            widget = QDialog()
            ui = GoodsForm(
                table=self,
                values=self.parse_row(),
                category_widget=self.category_widget,
            )
            ui.setupUi(widget)
            widget.exec_()

