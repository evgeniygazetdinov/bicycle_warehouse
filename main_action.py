from PySide2 import QtWidgets, QtCore
from library.db import Bicycle_db
from operations.ui.main_ui_fixes import FixesMainWindow
from operations.finances_action import CartFinance_methods
from widgets.custom_widgets import NumericItem


class Views_Main_Window(FixesMainWindow, CartFinance_methods):
    def __init__(self):
        self.current_row = {}
        self.goods_from_category = []
        self.cart_items = []
        self.total_price = 0
        self.total_income = 0
        self.course = 27.69

    def remove_item_in_cart_by_name(self, item_name):
        # check item in cartitem if in return cur qty in cart
        total_qty = 0
        for item in self.cart_items:
            if item["Название"] == item_name:
                self.cart_items.remove(item)
                self.update_total_price()
                break

    def remove_from_cart(self):
        item_text = self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()
        qty_items_in_cart = self.if_item_in_cart(item_text)
        if qty_items_in_cart:
            for delete_item in range(qty_items_in_cart):
                self.remove_item_in_cart_by_name(item_text)
        self.tableWidget_2.removeRow(self.tableWidget_2.currentRow())
        self.update_total_price()

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

    def display_goods_from_category(self, for_search=False):
        self.tableWidget.clean_table()
        goods_for_display = []
        try:
            category = self.treeWidget.currentItem().text(0)
        except:
            category = "Всі"
        self.tableWidget.display_goods(category)
        if self.lineEdit_4.text() != "":
            self.find_in()
        elif self.lineEdit.text() != "":
            self.find_in()

    def find_in(self):
        text = self.lineEdit_4.text()
        text_2 = self.lineEdit.text()
        for row in range(self.tableWidget.rowCount()):
            find_by_name = self.tableWidget.item(row, 1)
            find_by_article = self.tableWidget.item(row, 0)
            if "{}".format(text_2.lower()) in str(find_by_article.text()).lower():
                self.tableWidget.setRowHidden(row, False)
            if "{}".format(text.lower()) in str(find_by_name.text()).lower():
                self.tableWidget.setRowHidden(row, False)
            if (
                "{}".format(text_2.lower()) in str(find_by_article.text()).lower()
                and "{}".format(text.lower()) in str(find_by_name.text()).lower()
            ):
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

    def clean_cart(self):
        self.total_price = 0
        self.cart_items = []
        self.total_income = 0
        self.tableWidget_2.clean_table()

    def add_actions(self):
        # calling in UI

        self.add_additional_custom_elements()
        self.treeWidget.clicked.connect(self.display_goods_from_category)
        self.tableWidget.doubleClicked.connect(self.parse_row_and_move_to_cart)
        self.tableWidget_2.doubleClicked.connect(self.remove_from_cart)
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
        # self.tableWidget.clicked.connect(lambda: print(self.tableWidget.currentRow()))
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
        self.lineEdit.textChanged.connect(self.find_in)
        self.lineEdit_4.textChanged.connect(self.find_in)
        self.lineEdit.inputRejected.connect(self.find_in)
        self.lineEdit_4.inputRejected.connect(self.find_in)
        self.pushButton_8.clicked.connect(lambda: self.lineEdit.clear())
        self.pushButton_8.clicked.connect(lambda: self.lineEdit_4.clear())
