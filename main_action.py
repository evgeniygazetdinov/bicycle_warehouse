<<<<<<< HEAD
from PySide2 import QtWidgets, QtCore
from library.db import Bicycle_db
from operations.ui.main_ui_fixes import FixesMainWindow
from operations.finances_action import CartFinance_methods
from widgets.custom_widgets import NumericItem


class Views_Main_Window(FixesMainWindow, CartFinance_methods):
=======
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from good_form import GoodsForm
import sqlite3
from db import Bicycle_db
import re
from collections import OrderedDict
from main_ui_fixes import FixesMainWindow
from decimal import Decimal
import time
from random import randint
<<<<<<< HEAD
from custom_widgets import NumericItem, InputDialog
=======
from custom_widgets import NumericItem
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
from library.sublings import category_ids
from collections import defaultdict


<<<<<<< HEAD
class Views_Main_Window(FixesMainWindow):
>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e
=======


class Views_Main_Window(FixesMainWindow): 
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
    def __init__(self):
        self.current_row = {}
        self.goods_from_category = []
        self.cart_items = []
        self.total_price = 0
        self.total_income = 0
        self.course = 27.69
<<<<<<< HEAD

    def remove_item_in_cart_by_name(self, item_name):
        # check item in cartitem if in return cur qty in cart
        total_qty = 0
        for item in self.cart_items:
            if item["Название"] == item_name:
                self.cart_items.remove(item)
                self.update_total_price()
                break

    def remove_from_cart(self):
        # if item 1: remove from cart
        # if item many remove from list
        # if item in cart remove from list
        item_text = self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()
        qty_items_in_cart = self.if_item_in_cart(item_text)

        if qty_items_in_cart == 1:
            self.remove_item_in_cart_by_name(item_text)
            self.tableWidget_2.removeRow(self.tableWidget_2.currentRow())
        if qty_items_in_cart:
            self.remove_item_in_cart_by_name(item_text)
            item = NumericItem()
            row = self.tableWidget_2.find_in_table_by_name(item_text)
            item.setData(QtCore.Qt.DisplayRole, qty_items_in_cart)
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
        self.update_total_price()
=======

    def change_product_qty_in_cart(self):
        # get values
        if self.tableWidget_2.currentColumn() == 2:
            values = self.tableWidget_2.parse_row()
            counter = 0
            for cart_item in self.cart_items:
                counter += 1
                if cart_item["Название"] == values["название"]:
                    qty = cart_item["Кол-во."]
                    if int(cart_item["Кол-во."]) == 1:
                        QtWidgets.QMessageBox.about(
                            self.tab, "Error", "Товар в единичном количестве"
                        )
                    else:
                        dialog = InputDialog(
                            value=str(values["название"]), qty=str(qty)
                        )
                        if dialog.exec():
                            new_qty = dialog.getInputs()
                            item = NumericItem()
                            item.setData(QtCore.Qt.DisplayRole, (new_qty))
                            self.tableWidget_2.setItem(
                                (counter - 1), 2, QtWidgets.QTableWidgetItem(item)
                            )
                            cart_item["qty_item_in_cart"] = new_qty
                            item.setData(
                                QtCore.Qt.DisplayRole,
                                (int(values["цена"]) * int(new_qty)),
                            )
                            self.tableWidget_2.setItem(
                                (counter - 1), 3, QtWidgets.QTableWidgetItem(item)
                            )
                            self.update_total_price()

    def update_total_price(self):
        self.counting_price_income_from_cart_items("ГРН", "Закупка", "Продаж")
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))

    def if_item_in_cart(self, item_name):
        # check item in cartitem if in return cur qty in cart
        total_qty = 0
        for item in self.cart_items:
            if item["Название"] == item_name:
                total_qty += item["qty_item_in_cart"]
        if not total_qty:
            ret
        from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog
from good_form import GoodsForm
from db import Bicycle_db


class InputDialog(QDialog):
    def __init__(self, parent=None, value=None, qty=None):
        super().__init__(parent)
        self.value = value
        self.qty = qty
        #  self.second = QtWidgets.QLineEdit(self)
        self.setWindowTitle("изменить кол-во")
        buttonBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, self
        )
        layout = QtWidgets.QVBoxLayout(self)
        text = QtWidgets.QLabel(self.value)
        layout.addWidget(text)
        self.box = QtWidgets.QSpinBox(self)
        self.box.setMaximum(int(self.qty))
        if int(self.qty) > 0:
            self.box.setMinimum(1)
        self.box.setValue(int(1))
        layout.addWidget(self.box)
        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.box.value()


class CustomTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        QtWidgets.QTreeWidget.__init__(self, parent)

    def mousePressEvent(self, event):
        super(CustomTreeWidget, self).mousePressEvent(event)
        print("HERE")

    def contextMenuEvent(self, event):
        # handle right_click
        menu = QtWidgets.QMenu(self)
        add_category_Action = menu.addAction("добавить категорию")
        add_sub_category_Action = menu.addAction("добавить подкатегорию")
        edit_category_Action = menu.addAction("редактировать категорию")
        remove_category_Action = menu.addAction("удалить категорию")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        db = Bicycle_db()
        if action == add_category_Action:
            text, ok = QtWidgets.QInputDialog.getText(
                self, "Добавить категорию", "Имя для категории:"
            )
            if ok and text != "":
                rowcount = self.topLevelItemCount()
                self.addTopLevelItem(QtWidgets.QTreeWidgetItem(rowcount))
                self.topLevelItem(rowcount).setText(0, text)
                res = db.insert(
                    'INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",-1);'.format(
                        text
                    )
                )
                print(res)
                db.close()
        if action == remove_category_Action:
            item = self.currentItem()
            for SelectedItem in self.selectedItems():
                if SelectedItem.text(0) == item.text(0):
                    # check category is not null
                    qm = QtWidgets.QMessageBox()
                    ret = qm.question(self, "", "Удалить категорию?", qm.Yes | qm.No)
                    if ret == qm.Yes:
                        SelectedItem.removeChild(item)
                        text = item.text(0)
                        query = 'DELETE FROM categories WHERE name LIKE "%{}%";'.format(
                            text
                        )
                        db.insert(query)
                        db.close()
        if action == edit_category_Action:
            if self.selectedItems():
                old_name = self.currentItem().text(0)
                item = self.selectedItems()[0]
                text, ok = QtWidgets.QInputDialog.getText(
                    self,
                    "Редактировать",
                    "редактировать:",
                    QtWidgets.QLineEdit.Normal,
                    item.text(0),
                )
                if ok and text != "":
                    item.setText(0, text)
                    res = db.insert(
                        'UPDATE categories set name = "{}" where name like "%{}%";'.format(
                            text, old_name
                        )
                    )

        if action == add_sub_category_Action:
            text, ok = QtWidgets.QInputDialog.getText(
                self, "Добавить подкатегорию", "Имя для подкатегории:"
            )
            if ok and text != "":
                db = Bicycle_db()
                if len(self.selectedItems()) > 0:
                    QtWidgets.QTreeWidgetItem(self.selectedItems()[0], [text])
                    parent_id = db.insert(
                        'select id from categories where name like "%{}%"'.format(
                            self.currentItem().text(0)
                        )
                    )
                    db.insert(
                        'INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",{});'.format(
                            text, parent_id[0][0]
                        )
                    )
                else:
                    print("here")
                    QtWidgets.QTreeWidgetItem(self, [text])
                    res = db.insert(
                        'INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",-1);'.format(
                            text
                        )
                    )


class TreeWidgetGoods(CustomTreeWidget):
    def contextMenuEvent(self, event):
        pass


class ProcentItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)


class NumericItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)


class NumericItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)


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

    def parse_row(self,by_row=None):
        columns = self.columnCount()
        names = []
        values = []

        for i in range(columns):
            names.append(self.horizontalHeaderItem(i).text())
        if  by_row:
            for i in range(columns):
                values.append(self.item(by_row, i).text())
        else:
            for i in range(columns):
                values.append(self.item(self.currentRow(), i).text())
        return dict(zip(names, values))

    def find_in_table_by_name(self,name_for_search):
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
        if display_all:
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

    def display_goods(self, tree=False, for_search=False):
        list_with_goods = []
        current_category = None
        # if tree:
        current_category = tree
        list_with_goods = self.get_goods(display_all=True)
        row = len(list_with_goods)
        self.insertRow(row)
        self.setRowCount(row)
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
            item.setData(
                QtCore.Qt.DisplayRole,
                self.calculate_sell_price(good["sell"], good["buy"]),
            )
            self.setItem(row, 3, QtWidgets.QTableWidgetItem(item))

            item.setData(QtCore.Qt.DisplayRole, (good["qty"]))
            self.setItem(row, 5, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (good["sell_uah"]))
            self.setItem(row, 6, QtWidgets.QTableWidgetItem(item))

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


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        db = Bicycle_db()
        db.insert("drop table if exists cur_category")
        db.close()
        event.accept()
urn None
        else:
            return total_qty

    def cart_items_rounder(self, values, qty_in_cart):

        row = self.tableWidget_2.find_in_table_by_name(values["Название"])
        total = self.if_item_in_cart(values["Название"])
        values["qty_item_in_cart"] = total
        self.cart_items.append(values)
        values["qty_item_in_cart"] += 1
        items_price = int(values["ГРН"]) * int(values["qty_item_in_cart"])
        item = NumericItem()
        self.update_total_price()
        item.setData(QtCore.Qt.DisplayRole, (items_price))
        self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
        item.setData(QtCore.Qt.DisplayRole, values["qty_item_in_cart"])
        self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
        print(self.cart_items)

    def parse_row_and_move_to_cart(self):
        values = self.tableWidget.parse_row()
        if int(values["Кол-во."]) > 0:
            item_in_cart = self.if_item_in_cart(values["Название"])
            if item_in_cart:
                if int(item_in_cart) < int(values["Кол-во."]):
                    self.cart_items_rounder(values, item_in_cart)
                else:
                    QtWidgets.QMessageBox.about(
                        self.tab, "Error", "Нет доступного количества"
                    )

            else:
                self.total_price = 0
                row = self.tableWidget_2.rowCount()
                values = self.tableWidget.parse_row()
                self.tableWidget_2.insertRow(row + 1)
                self.tableWidget_2.setRowCount(row + 1)
                item = NumericItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setData(QtCore.Qt.DisplayRole, values["Название"])
                self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
                item.setData(QtCore.Qt.DisplayRole, (values["ГРН"]))
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(item))
                values["qty_item_in_cart"] = 1
                items_price = int(values["ГРН"]) * int(values["qty_item_in_cart"])
                self.cart_items.append(values)
                self.update_total_price()
                item.setData(QtCore.Qt.DisplayRole, (items_price))
                self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
                item.setData(QtCore.Qt.DisplayRole, values["qty_item_in_cart"])
                self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
        else:
            QtWidgets.QMessageBox.about(
                self.tab, "Error", "Нельзя добавить товар с количеством 0"
            )

    def remove_from_cart(self):
        item_text = self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()
        for cart_item in range(len(self.cart_items)):
            if self.cart_items[cart_item]["Название"] == item_text:

                self.tableWidget_2.removeRow(self.tableWidget_2.currentRow())
                removed_item = self.cart_items.pop(cart_item)
                break

        if removed_item["Арт"]:
            minus_from_cart = int(removed_item["ГРН"]) * int(
                removed_item["qty_item_in_cart"]
            )
            self.update_total_price()

    def calculate_good_income(self, sell, buy, qty):
        income = (round(abs((float(sell) - float(buy))) * self.course, 1)) * qty
        self.total_income += income

    def counting_price_income_from_cart_items(
        self, grivna_keyword, sell_keyword=False, buy_keyword=False, sale=False
    ):
        self.total_price = 0
        self.total_income = 0
        for item in self.cart_items:
            total_price = int(item[grivna_keyword]) * int(item["qty_item_in_cart"])
            self.total_price += total_price

            if "Арт" in item:
                if sell_keyword:
                    income = self.calculate_good_income(
                        item[sell_keyword], item[buy_keyword], item["qty_item_in_cart"]
                    )
        if sale:
            self.total_price -= int(sale)

    def show_insert_window(self):
        pass

    def get_cart_items(self):
        pass
>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e

    def cart_qty_handler(self):
        cart_items = self.tableWidget_2.get_values_from_cart()
        key_for_search = "кол-во"
        unique = []
        for item in cart_items:
            if item not in unique:
                unique.append(item)
        print(unique)

    def get_values_from_db(self):
        self.set_into_table_goods()
        self.set_into_categories_table()

    def find_child_category(self, list_with_results):
        id_with_child = []
        for result in list_with_results:
            if result["parent_id"] == -1:
                id_with_child.append({"id": result["id"], "childs": []})
            else:
                for number in range(len(id_with_child)):
                    if id_with_child[number]["id"] == result["parent_id"]:
                        id_with_child[number]["childs"].append(result["name_category"])
        return id_with_child

    def get_category_values(self):
        list_dict_with_results = []
        db = Bicycle_db()
        result = db.edit("Select * FROM categories")
        count = len(result)
        for item in result:
            id = item[0]
            name_category = item[1]
            parent_id = item[2]
            export_date = item[3]
            list_dict_with_results.append(
                {
                    "id": id,
                    "name_category": name_category,
                    "parent_id": parent_id,
                    "export_date": export_date,
                }
            )
        # sort_by_id
        return sorted(list_dict_with_results, key=lambda k: k["parent_id"])

    def fill_tree(self):
        list_with_results = self.get_category_values()
        childs_categories = self.find_child_category(list_with_results)
        for res in list_with_results:
            if res["parent_id"] == -1:
                item = QtWidgets.QTreeWidgetItem([res["name_category"]])
                current_index = self.treeWidget.currentItem()
                self.treeWidget.addTopLevelItem(item)
                for child in childs_categories:
                    if res["id"] == child["id"]:
                        if len(child["childs"]) != 0:
                            for element in child["childs"]:
                                QtWidgets.QTreeWidgetItem(item, [element])

<<<<<<< HEAD
    def display_goods_from_category(self, for_search=False):
<<<<<<< HEAD
        self.tableWidget.clean_table()
=======
>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e
=======

    
    def display_goods_from_category(self,for_search=False):
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
        goods_for_display = []
        try:
            category = self.treeWidget.currentItem().text(0)
        except:
<<<<<<< HEAD
            category = "Всі"
<<<<<<< HEAD
        self.tableWidget.display_goods(category)
        if self.lineEdit_4.text() != "":
            self.find_in(self.lineEdit_4, 1)
        elif self.lineEdit.text() != "":
            self.find_in(self.lineEdit, 0)
=======
=======
            category = 'Всі'
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
        category_number = category_ids[category]
        for good in self.tableWidget.goods_from_table:
            if str(category_number) in good["category"]:
                goods_for_display.append(good["article"])
        for row in range(self.tableWidget.rowCount()):
            twItem = self.tableWidget.item(row, 0)
            if int(twItem.text()) in goods_for_display:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)
>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e

    def find_in(self, textinput, column):
        text = textinput.text()
        if column == 1:
            for row in range(self.tableWidget.rowCount()):
                twItem = self.tableWidget.item(row, column)
                if "{}".format(text.lower()) in str(twItem.text()).lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)
<<<<<<< HEAD
        else:
            for row in range(self.tableWidget.rowCount()):
=======

        else:
            for row in range(self.tableWidget.rowCount ()):
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
                twItem = self.tableWidget.item(row, column)
                text_in_window = twItem.text()
                if "{}".format(str(text).lower()) in str(text_in_window).lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)

    def set_current_category(self, category):
        db = Bicycle_db()

        query = "CREATE TABLE IF NOT EXISTS cur_category (id INTEGER PRIMARY KEY AUTOINCREMENT, name_category TEXT);"
        query_2 = 'insert into cur_category(name_category) values("{}")'.format(
            category
        )
        db.insert(query)
        db.insert(query_2)
        db.close()

<<<<<<< HEAD
=======
    def hander_for_handy_buttons(self, line_edit, button):
        self.total_price = 0
        price = line_edit.text()
        specific = button.text()
        row = self.tableWidget_2.rowCount()
        item = QtWidgets.QTableWidgetItem()
        item.setData(QtCore.Qt.DisplayRole, (price))
        self.tableWidget_2.insertRow(row + 1)
        self.tableWidget_2.setRowCount(row + 1)
        self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(specific)))
        self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(item))

        if button == self.sale_button:
            self.counting_price_income_from_cart_items("ГРН", sale=price)
        else:
<<<<<<< HEAD
            self.cart_items.append({"Название": specific, "ГРН": price})
            self.counting_price_income_from_cart_items("ГРН")
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))
        self.tableWidget_2.setItem(
            row, 2, QtWidgets.QTableWidgetItem(str((self.total_price)))
        )

>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e
=======
            self.cart_items.append({'Название':specific,'ГРН':price})
            self.counting_price_income_from_cart_items('ГРН')
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))
        self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(str((self.total_price))))
   
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
    def clean_cart(self):
        self.total_price = 0
        self.cart_items = []
        self.total_income = 0
        self.tableWidget_2.clean_table()

    def add_actions(self):
        # calling in UI

        self.add_additional_custom_elements()
<<<<<<< HEAD
=======
        # self.add_goods_action.triggered.connect(self.show_insert_window)
>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e
        self.treeWidget.clicked.connect(self.display_goods_from_category)
        self.tableWidget.doubleClicked.connect(self.parse_row_and_move_to_cart)
        self.tableWidget_2.doubleClicked.connect(self.remove_from_cart)
<<<<<<< HEAD
        # show name good on bottom
        self.tableWidget.clicked.connect(
            lambda: self.statusBar.showMessage(
                self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
            )
        )
        self.tableWidget_2.clicked.connect(self.change_product_qty_in_cart)
        self.tableWidget_2.clicked.connect(
            lambda: self.statusBar.showMessage(
                self.tableWidget_2.item(
                    self.tableWidget_2.currentRow(), self.tableWidget_2.currentColumn()
                ).text()
            )
        )
<<<<<<< HEAD
        # self.tableWidget.clicked.connect(lambda: print(self.tableWidget.currentRow()))
=======
        self.tableWidget.clicked.connect(lambda: print(self.tableWidget.currentRow()))
>>>>>>> c3d4b704476aebddf3c5842be44864b8cc11248e
        self.treeWidget.clicked.connect(
            lambda: self.statusBar.showMessage(self.treeWidget.currentItem().text(0))
        )
        self.treeWidget.clicked.connect(
            lambda: self.set_current_category(self.treeWidget.currentItem().text(0))
        )
        # self.tableWidget.c
        self.materials_button.clicked.connect(
            lambda: self.hander_for_handy_buttons(
                self.lineEdit_3, self.materials_button
            )
        )
        self.workshop_button.clicked.connect(
            lambda: self.hander_for_handy_buttons(self.lineEdit_5, self.workshop_button)
        )
        self.sale_button.clicked.connect(
            lambda: self.hander_for_handy_buttons(self.lineEdit_6, self.sale_button)
        )

        # clean cart button
        self.pushButton_4.clicked.connect(self.clean_cart)
        self.lineEdit.textChanged.connect(lambda: self.find_in(self.lineEdit, 0))
        self.lineEdit_4.textChanged.connect(lambda: self.find_in(self.lineEdit_4, 1))
        self.lineEdit.inputRejected.connect(lambda: self.find_in(self.lineEdit, 0))
        self.lineEdit_4.inputRejected.connect(lambda: self.find_in(self.lineEdit_4, 1))
        self.pushButton_8.clicked.connect(lambda: self.lineEdit.clear())
        self.pushButton_8.clicked.connect(lambda: self.lineEdit_4.clear())
=======
        self.tableWidget.clicked.connect(lambda :print(self.tableWidget.currentRow()))
        self.treeWidget.clicked.connect(lambda :self.statusBar.showMessage(self.treeWidget.currentItem().text(0)))
        self.treeWidget.clicked.connect(lambda :self.set_current_category(self.treeWidget.currentItem().text(0)))
        # self.tableWidget.c
        self.materials_button.clicked.connect(lambda : self.hander_for_handy_buttons(self.lineEdit_3,self.materials_button))
        self.workshop_button.clicked.connect(lambda : self.hander_for_handy_buttons(self.lineEdit_5,self.workshop_button))
        self.sale_button.clicked.connect(lambda : self.hander_for_handy_buttons(self.lineEdit_6,self.sale_button))
       # self.treeWidget.cellClicked.connect(self.updateUiCellClick) 
       
       
       
        #clean cart button
        self.pushButton_4.clicked.connect(self.clean_cart)
        self.lineEdit.textChanged.connect(lambda:self.find_in(self.lineEdit,0))
        self.lineEdit_4.textChanged.connect(lambda: self.find_in(self.lineEdit_4,1))
        self.lineEdit.inputRejected.connect(lambda:self.find_in(self.lineEdit,0))
        self.lineEdit_4.inputRejected.connect(lambda: self.find_in(self.lineEdit_4,1))
        self.pushButton_8.clicked.connect(lambda : self.lineEdit.clear() )
        self.pushButton_8.clicked.connect(lambda:self.lineEdit_4.clear() )

        
>>>>>>> 191eb7a3e5cca42409226c1fbe6924c54bb97052
