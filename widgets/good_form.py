import sys
from PySide2 import QtGui, QtWidgets, QtCore, Qt
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QToolTip,
    QMessageBox,
    QLabel,
    QDialog,
)
from library.db import Bicycle_db
import time


class Communicate(QtCore.QObject):

    closeApp = QtCore.Signal()


class GoodsForm(QMainWindow):
    def __init__(
        self, table=False, new_good=False, values=False, category_widget=False, course=False):
        super().__init__()
        
        self.values = values
        self.new_good = new_good
        self.category_widget = category_widget
        self.table = table
        self.values_for_new_good_window = {}

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 297)
        self.c = Communicate()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 80, 53, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 130, 71, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(160, 150, 61, 21))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 100, 371, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 81, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 180, 71, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(250, 200, 81, 21))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 200, 81, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(340, 180, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 200, 91, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(440, 180, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(450, 130, 81, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 150, 91, 21))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(0, 50, 151, 241))
        self.treeWidget.setObjectName("treeWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 240, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 30, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(150, 10, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.USD_value = QtWidgets.QLabel(Form)
        self.USD_value.setGeometry(QtCore.QRect(200, 10, 65, 16))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.USD_value.setFont(font)
        self.USD_value.setObjectName("USD_value")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(300, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 20, 81, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.category_title = QtWidgets.QLabel(Form)
        self.category_title.setGeometry(QtCore.QRect(180, 50, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category_title.setFont(font)
        self.category_title.setObjectName("category_title")
        self.comboBox.hide()
        self.label_4.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.additional_actions(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("добавить новый товар")
        if self.values:
            Form.setWindowTitle("изменить товар")
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "В наличии"))
        self.label_3.setText(_translate("Form", "Закупка"))
        self.label_4.setText(_translate("Form", "Валюта"))
        self.comboBox.setItemText(0, _translate("Form", "USD"))
        self.label_5.setText(_translate("Form", "Наценка"))
        self.label_6.setText(_translate("Form", "Продаж,USD"))
        self.label_7.setText(_translate("Form", "Продаж,ГРН"))
        self.pushButton.setText(_translate("Form", "Отмена"))
        self.pushButton_2.setText(_translate("Form", "Подтвердить"))
        self.label_8.setText(_translate("Form", "Категория"))
        self.USD_value.setText(_translate("Form", "30"))
        self.label_10.setText(_translate("Form", "Артикул"))
        self.category_title.setText(_translate("Form", "Категория"))

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

    def transtlate_category(self, category):
        db = Bicycle_db()
        if isinstance(category, str):
            category_id = db.insert(
                'SELECT id from categories where name like "%{}%"'.format(category)
            )
            return category_id[0]
        elif isinstance(category, int):
            category_id = db.insert(
                "SELECT name from categories where id ={}".format(category)
            )
            return category_id[0][0]

    def get_values_from_good_windows(self):
        good_values = {}
        good_values["article"] = self.lineEdit_6.text()
        good_values["profit"] = self.lineEdit_3.text()
        good_values["buy"] = self.lineEdit_2.text()
        good_values["sell"] = self.lineEdit_4.text()
        good_values["name"] = self.lineEdit.text()
        good_values["sell_uah"] = self.lineEdit_5.text()
        if self.category_title.text() == "категории":
            good_values["category"] = 0
        else:
            good_values["category"] = (
                self.transtlate_category(self.category_title.text())
            )[0]
        good_values["qty"] = str(self.spinBox.value())
        return good_values

    def insert_into_good_form(self, good_values):
        f = self.texteditor1.font()
        f.setPointSize(20)
      
        self.lineEdit_6.setText(good_values["article"])
        self.lineEdit_3.setText(good_values["profit"])
        self.lineEdit_2.setText(good_values["buy"])
        self.lineEdit_4.setText(good_values["sell"])
        self.lineEdit_5.setText(good_values["sell_uah"])
        self.spinBox.setValue(int(good_values["qty"]))
        self.lineEdit_6.setFont(f)
        self.lineEdit_3.setFont(f)
        self.lineEdit_2.setFont(f)
        self.lineEdit_4.setFont(f)
        self.lineEdit_5.setFont(f)
       
        

    def store_good(self):
        values = self.get_values_from_good_windows()
        db = Bicycle_db()
        schema = db.schema["goods"]
        str_schema = ",".join(schema)
        query = 'insert into "goods"({}) values("","{}",{},{},{},{},{},"{}",{},{})'.format(
            str_schema,
            values["name"],
            values["qty"],
            values["buy"],
            values["sell"],
            values["profit"],
            values["category"],
            "USD",
            values["sell_uah"],
            values["article"],
        )
        db.insert(query)
        self.table.update_table()
        self.update_good_window()

    def edit_good(self):
        values = self.get_values_from_good_windows()
        db = Bicycle_db()
        query = """UPDATE goods SET (name,qty,buy,sell,profit,category,sell_uah,article)=("{}",{},{},{},"{}",{},{},{}) WHERE article like "%{}%";""".format(
            values["name"],
            values["qty"],
            values["buy"],
            values["sell"],
            values["profit"],
            values["category"],
            values["sell_uah"],
            values["article"],
            values["article"],
        )
        db.insert(query)
        self.table.update_table()

    def cur_category_handler(self):
        db = Bicycle_db()
        cur_category = db.exists("cur_category")
        if cur_category:
            res = db.insert(
                "select name_category from cur_category where id=(select max(id) from cur_category)"
            )
            cur_category = res[0][0]
        else:
            cur_category = "Всі"
        return cur_category

    def update_good_window(self):
        self.values_for_new_good_window = self.get_values_from_good_windows()
        self.values_for_new_good_window["article"] = int(
            self.values_for_new_good_window["article"]
        )
        self.values_for_new_good_window["article"] += 1
        self.values_for_new_good_window["article"] = str(
            self.values_for_new_good_window["article"]
        )
        self.values_for_new_good_window["category"] = self.transtlate_category(
            self.values_for_new_good_window["category"]
        )
        self.insert_into_good_form(self.values_for_new_good_window)

    def selectItem(self, widget, itemOrText):
        oldIndex = widget.selectionModel().currentIndex()
        try:  # an item is given--------------------------------------------
            newIndex = widget.model().indexFromItem(itemOrText)
        except:  # a text is given and we are looking for the first match---
            listIndexes = widget.model().match(
                widget.model().index(0, 0),
                QtCore.Qt.DisplayRole,
                itemOrText,
                QtCore.Qt.MatchStartsWith,
            )
            newIndex = listIndexes[0]
        widget.selectionModel().select(  # programmatical selection---------
            newIndex, QtGui.QItemSelectionModel.ClearAndSelect
        )

    def additional_actions(self, Form):
        self.add_actions(Form)

        self.fill_tree()
        self.treeWidget.setHeaderHidden(True)
        if self.values:
            # when change_item
            self.lineEdit_4.setText(self.values["Продаж"])
            self.lineEdit_3.setText(self.values["Нац"])
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_2.setText(self.values["Закупка"])
            self.lineEdit_6.setText(self.values["Арт"])
            self.lineEdit_5.setText(self.values["ГРН"])
            self.lineEdit.setText(self.values["Название"])
            self.spinBox.setValue(int(self.values["Кол-во."]))
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_6.setEnabled(False)
            self.label_9.setText("")
            self.comboBox.hide()
            self.label_4.hide()
            self.pushButton_2.clicked.connect(self.edit_good)
            self.pushButton_2.clicked.connect(lambda: Form.close())
            # move categories
            category = self.cur_category_handler()
            item = QtWidgets.QTreeWidgetItem(category)
            self.category_title.setText(category)
            index = self.find_element_index_in_tree(category)

            if len(index) == 1:
                pass
                # self.treeWidget.model().index(index[0])
            # handle for child or not child element

        else:
            self.lineEdit_6.setEnabled(False)
            ids_for_new_good = "SELECT MAX(article)from goods"
            db = Bicycle_db()
            good_id = (db.insert(ids_for_new_good))[0][0] + 1
            self.lineEdit_6.setText(str(good_id))
            self.spinBox.setValue(1)
            self.treeWidget.setCurrentItem(QtWidgets.QTreeWidgetItem("Bci"))
            category = self.cur_category_handler()
            self.category_title.setText(category)
            self.pushButton_2.clicked.connect(self.store_good)
            db.close()

    def find_element_index_in_tree(self, category):
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            url = item.text(0)  # text at first (0) column
            if root.child(i).text(0) == category:
                return [i]
            for x in range(item.childCount()):
                if root.child(i).child(x).text(0) == category:
                    return [i, x]


    def get_current_course(self):
        db = Bicycle_db()
        query = db.insert("SELECT value FROM settings WHERE name = 'Курс'")
        db.close()
        course = int(query[0][0])
        self.USD_value.setText(f'USD-{str(course)}')
        return int(query[0][0])

    def recalculate_procent(self,sell,buy):
        dif = abs(float(buy) - float(sell))
        return int(str(int(round((dif / buy) * 100, 1))))


    def recalculate_price(self):
        buy_price = self.lineEdit_2.text()
        try:
            int(buy_price)
        except:
            if str(buy_price).endswith('.'):
                buy_price  = (str(buy_price).split('.'))[0]
            else:
                buy_price = [int(s) for s in buy_price.split() if s.isdigit()]  
        sell_price = int(buy_price) * self.course
        procent = self.recalculate_procent(int(sell_price),int(buy_price))
        self.lineEdit_5.setText('')
        self.lineEdit_5.setText(str(sell_price))
        self.lineEdit_3.setText('')
        if procent:
            self.lineEdit_3.setText(str(procent)+'%')
        
    def new_item_calculate(self):
        pass

    def add_actions(self, Form):
        self.pushButton.clicked.connect(lambda: Form.close())
        self.lineEdit_2.inputRejected.connect(self.recalculate_price)
        self.lineEdit_2.textChanged.connect(self.recalculate_price)
        self.treeWidget.clicked.connect(
            lambda: self.category_title.setText(self.treeWidget.currentItem().text(0))
        )
        self.course = self.get_current_course()