from widgets.custom_widgets import NumericItem, InputDialog
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from library.db import Bicycle_db
from decimal import Decimal
import time
from widgets.custom_widgets import NumericItem, InputDialog
from library.sublings import category_ids
from PySide2.QtCore import Qt


class CartFinance_methods:
    def change_product_qty_in_cart(self):
        # get values
        if self.tableWidget_2.currentColumn() == 2:
            values = self.tableWidget_2.parse_row()
            counter = 0
            for cart_item in self.cart_items:
                counter += 1
                if cart_item["Название"] == values["название"]:
                    # it' handy buttons
                    if "Арт" not in cart_item:
                        qty = 1
                        break

                    elif int(cart_item["Кол-во."]) == 1:
                        QtWidgets.QMessageBox.about(
                            self.tab, "Error", "Товар в единичном количестве"
                        )
                    else:
                        qty = cart_item["Кол-во."]
                        dialog = InputDialog(
                            value=str(values["название"]), qty=str(qty)
                        )
                        if dialog.exec():
                            new_qty = dialog.getInputs()
                            item = NumericItem()
                            # if need more append
                            qty_now = self.if_item_in_cart(cart_item["Название"])
                            if qty_now < new_qty:
                                how_many_item_need_add = new_qty - qty_now
                                for one_add in range(how_many_item_need_add):
                                    self.cart_items.append(cart_item)
                            elif qty_now > new_qty:
                                how_many_item_need_delete = qty_now - new_qty
                                for one_delete in range(how_many_item_need_delete):
                                    self.remove_item_in_cart_by_name(
                                        cart_item["Название"]
                                    )

                            # else pop
                            item.setData(QtCore.Qt.DisplayRole, (new_qty))
                            self.tableWidget_2.setItem(
                                (counter - 1), 2, QtWidgets.QTableWidgetItem(item)
                            )
                            # cart_item["qty_item_in_cart"] = new_qty
                            item.setData(
                                QtCore.Qt.DisplayRole,
                                (int(values["цена"]) * int(new_qty)),
                            )
                            self.tableWidget_2.setItem(
                                (counter - 1), 3, QtWidgets.QTableWidgetItem(item)
                            )
                            self.update_total_price()
                            break

    def update_total_price(self, sale=False):
        if sale:
            self.counting_price_income_from_cart_items(
                "ГРН", "Закупка", "Продаж", sale=sale
            )
        else:
            self.counting_price_income_from_cart_items("ГРН", "Закупка", "Продаж")
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))

    def calculate_good_income(self, sell, buy, qty):
        income = (round(abs((float(sell) - float(buy))) * self.course, 1)) * qty
        self.total_income += income

    def counting_price_income_from_cart_items(
        self, grivna_keyword, sell_keyword=False, buy_keyword=False, sale=False
    ):
        self.total_price = 0
        self.total_income = 0
        for item in self.cart_items:

            if item["Название"] == "работа":
                work_price = int(item[grivna_keyword])
                self.total_income += work_price
                self.total_price += work_price
            elif item["Название"] == "скидка":
                self.total_income -= int(item["ГРН"])
                self.total_price -= int(item["ГРН"])
            else:
                total_price = int(item[grivna_keyword]) * int(item["qty_item_in_cart"])
                self.total_price += total_price
                if "Арт" in item:
                    # if sell_keyword:
                    income = self.calculate_good_income(
                        item[sell_keyword], item[buy_keyword], item["qty_item_in_cart"]
                    )

    def cart_items_rounder(self, values, qty_in_cart):
        values["qty_item_in_cart"] = 1
        self.cart_items.append(values)
        row = self.tableWidget_2.find_in_table_by_name(values["Название"])
        total = self.if_item_in_cart(values["Название"])
        items_price = int(values["ГРН"]) * int(total)
        item = NumericItem()
        self.update_total_price()
        item.setData(QtCore.Qt.DisplayRole, (items_price))
        self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
        item.setData(QtCore.Qt.DisplayRole, total)
        self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(item))

    def if_item_in_cart(self, item_name):
        # check item in cartitem if in return cur qty in cart
        total_qty = 0
        for item in self.cart_items:
            if item["Название"] == item_name:
                total_qty += item["qty_item_in_cart"]
        if not total_qty:
            return None
        else:
            return total_qty

    def parse_row_and_move_to_cart(self):
        values = self.tableWidget.parse_row()
        if int(values["Кол-во."]) > 0:
            # return qty values in cart
            item_in_cart = self.if_item_in_cart(values["Название"])
            if item_in_cart:
                # if qty not bigger availiable
                if int(item_in_cart) < int(values["Кол-во."]):
                    self.cart_items_rounder(values, item_in_cart)
                else:
                    QtWidgets.QMessageBox.about(
                        self.tab, "Error", "Нет доступного количества"
                    )
            # item not in self.cart_items
            else:
                self.total_price = 0
                self.tableWidget_2.setSelectionBehavior(
                    QtWidgets.QAbstractItemView.SelectRows
                )
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

    def hander_for_handy_buttons(self, line_edit, button):
        self.total_price = 0
        self.total_income = 0
        price = line_edit.text()
        try:
            int(price)
        except:
            raise QtWidgets.QMessageBox.about(
                self.tab, "Error", "это не число".format(button.text())
            )
        if price != "":
            item_in_cart = self.if_item_in_cart(button.text())
            specific = button.text()
            if item_in_cart:
                row = self.tableWidget_2.find_in_table_by_name(specific)
                items_price = int(price)
                item = NumericItem()
                self.remove_item_in_cart_by_name(specific)
                values = {"Название": specific, "ГРН": price, "qty_item_in_cart": 1}
                self.cart_items.append(values)
                self.update_total_price()
                item.setData(QtCore.Qt.DisplayRole, (items_price))
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(item))
                item.setData(QtCore.Qt.DisplayRole, (items_price))
                self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
                item.setData(QtCore.Qt.DisplayRole, 1)
                self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
            else:
                row = self.tableWidget_2.rowCount()
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, (price))
                self.tableWidget_2.insertRow(row + 1)
                self.tableWidget_2.setRowCount(row + 1)
                self.tableWidget_2.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(str(specific))
                )
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(item))

                self.cart_items.append(
                    {"Название": specific, "ГРН": price, "qty_item_in_cart": 1}
                )
                self.update_total_price()
                # self.label_37.setText(str(self.total_price))
                # self.label_38.setText(str(round(self.total_income)))
                total_qty = 1
                self.tableWidget_2.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(str((total_qty)))
                )
                self.tableWidget_2.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(str((price * total_qty)))
                )
            line_edit.setText("")
        else:
            QtWidgets.QMessageBox.about(
                self.tab, "Error", "нет значения поле в {}".format(button.text())
            )

