from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from good_form import GoodsForm
from custom_widgets import CustomTreeWidget,CustomTableWithGoods
import sqlite3
from db import Bicycle_db





class Views_Main_Window: 

    def add_additional_custom_elements(self):
        self.add_custom_tree()
        self.add_custom_table()
        self.fill_tree()
        self.fill_combobox_with_categories()
        self.resize_tableWidget()
        #fill_table_by_default
        self.display_goods_from_category(True)

    def parse_table(self):
        self.tbl_anggota.item(r,0).text()
       
    

    def show_insert_window(self):
        #self.parse_table()
        widget = QDialog()
        ui = GoodsForm()
        ui.setupUi(widget)
        widget.exec_()
    
    def resize_tableWidget(self):
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)   
        self.tableWidget.setColumnWidth(2,500)   
        self.tableWidget.setColumnWidth(3,50)   
        self.tableWidget.setColumnWidth(4,40)   
        self.tableWidget.setColumnWidth(5,50)   
        self.tableWidget.setColumnWidth(6,50)   
        self.tableWidget.setColumnWidth(7,50)   

    def get_values_from_db(self):
        self.set_into_table_goods()
        self.set_into_categories_table()

    def add_top_element_in_tree_widget(self,item_name):
        current_index = self.treeWidget.current_item()
        self.treeWidget.insertTopLevelItems(index, item_name)


    def add_custom_tree(self):
        self.treeWidget = CustomTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 131, 741))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "имя")
    def add_custom_table(self):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget = CustomTableWithGoods(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(140, 70, 801, 721))
        self.tableWidget.setMaximumSize(QtCore.QSize(801, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Aрт.Ст")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(192, 252, 187))
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsTristate)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(192, 252, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 7, item)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Арт.Cт"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Арт.H"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "закупка"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "нац"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Продаж."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "К-ть"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ГРН"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def fill_combobox_with_categories(self):
        categories = self.get_category_values()
        _translate = QtCore.QCoreApplication.translate
        for category in range(len(categories)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(category,(categories[category]['name_category']))


    def find_child_category(self,list_with_results):
        id_with_child =[]
        for result in list_with_results:
            if result['parent_id'] ==-1:
                id_with_child.append({'id':result['id'],'childs':[]})
            else:
                for number in range(len(id_with_child)):
                    if id_with_child[number]['id'] == result['parent_id']:
                        id_with_child[number]['childs'].append(result['name_category'])
        return id_with_child

    def get_category_values(self):
        list_dict_with_results = []
        db = Bicycle_db()
        result = db.edit("Select * FROM categories")
        count = (len(result))
        for item in result:
            id = item[0]
            name_category = item[1]
            parent_id = item[2]
            export_date = item[3]
            list_dict_with_results.append({'id':id,'name_category':name_category,'parent_id':parent_id,'export_date':export_date})
        #sort_by_id
        return sorted(list_dict_with_results, key=lambda k: k['parent_id'])
        
    def fill_tree(self):
        list_with_results = self.get_category_values()
        childs_categories = self.find_child_category(list_with_results)
        for res in list_with_results:
            if res['parent_id'] == -1:
                item =QtWidgets.QTreeWidgetItem([res['name_category']])
                current_index = self.treeWidget.currentItem()
                self.treeWidget.addTopLevelItem(item)
                for child in childs_categories:
                    if res['id'] == child['id']:
                        if len(child['childs'])!=0:
                            for element in child['childs']:
                                QtWidgets.QTreeWidgetItem(item, [element])


    def from_sqlgoods_to_dict(self,goods):
        res = []
        for value in goods:
            article_old = value[0]
            name = value[1]
            qty = value[2]
            buy = value[3]
            sell = value[4]
            profit = value[5]
            category = value[6]
            currency = value[7]
            sell_uah = value[8]
            article = value[9]
            res.append({'article_old':article_old,"name":name,
                        'qty':qty,"buy":buy,"sell":sell,
                        "profit":profit,"category":category,
                        "currency":currency,"sell_uah":sell_uah,
                        "article":article})
        return res





    def get_goods(self,category_name,default=False):
        db = Bicycle_db()
        if default:
            category_name ='Всі'
        category_id = db.select('SELECT id from categories  where name like "%{}%"'.format(category_name))
        goods = db.edit('Select * from goods where category like "%{}%";'.format(category_id[0]))
        db.close()
        return self.from_sqlgoods_to_dict(goods)
    
    def set_current_category(self):
        text = self.treeWidget.currentItem().text(0)
        index = self.comboBox.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboBox.setCurrentIndex(index)



    
    def display_goods_from_category(self,default=False):
        current_category = self.comboBox.currentText()
        #warning here
        if default == True:
            list_with_goods = self.get_goods(current_category,default)
        else:
            list_with_goods = self.get_goods(current_category)
        self.tableWidget.insertRow(len(list_with_goods))
        self.tableWidget.setRowCount(len(list_with_goods))
        row = len(list_with_goods)
        for good in list_with_goods:
            row -=1
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(good["article_old"])))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(good["article"])))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(good["name"])))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(good["buy"])))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(good["sell"])))
            self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(good["qty"])))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem('None'))

            self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(good["sell_uah"])))

            




        


    
    def add_actions(self):
        #calling in UI
        self.add_additional_custom_elements()
        #self.add_goods_action.triggered.connect(self.show_insert_window)
        self.treeWidget.clicked.connect(self.set_current_category)
        self.tableWidget.clicked.connect(self.show_insert_window)
        self.comboBox.activated.connect(lambda:self.display_goods_from_category())
        self.comboBox.currentIndexChanged.connect(lambda:self.display_goods_from_category())
