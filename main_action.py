from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from good_form import GoodsForm
from custom_widgets import CustomTreeWidget,CustomTableWithGoods
import sqlite3
from db import Bicycle_db
import re





class Views_Main_Window: 
    def __init__(self):
        self.current_row = {}
        self.goods_from_category = []
    def add_additional_custom_elements(self):
        self.add_custom_tree()
        self.add_custom_table()
        self.fill_tree()
        self.resize_tableWidget()
        #fill_table_by_default
         #if pass true  ==> display all categories 
         #when in treewidget without choose treewidget.current item is none
        self.display_goods_from_category()
        self.change_search_widget_section()
        self.fixes_on_cart()
        self.ui_fixes()

    def ui_fixes(self):
        item = self.tableWidget_6.horizontalHeaderItem(8)
        item.setText("Доход")
        self.tabWidget.setTabText(2, "Настройки")
        self.label_22.setText('Наличные')
        self.label_22.setFont(QtGui.QFont('Sans Serif', 11)) 
        #set no editable
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    
    def fixes_on_cart(self):
        self.lineEdit_3.setFixedWidth(50)
        self.lineEdit_5.setFixedWidth(50)
        self.lineEdit_6.setFixedWidth(50)
        self.label_7.setGeometry(QtCore.QRect(1030, 60, 141,21))
        self.label_8.setGeometry(QtCore.QRect(1030, 90, 131, 20))
        self.label_9.setGeometry(QtCore.QRect(1030, 120, 131, 20))
        self.label_9.setText('скидка')
        
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(9)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.pushButton_5.setText('Наличные')


    def change_search_widget_section(self):
        # m = self.lineEdit.textMargins()
        # m.setLeft(10)
        self.lineEdit.setFixedWidth(50)
        self.lineEdit_4.setFixedWidth(200)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 40, 101, 20))
        self.pushButton_8.setGeometry(QtCore.QRect(390, 40, 31, 21))
        self.comboBox.hide()


    def parse_row(self):
        name = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        self.statusBar.showMessage(name)
        

    def show_insert_window(self):
        #self.parse_table()
        pass
    
    def resize_tableWidget(self):
        values = [50, 480, 50, 50, 50, 50, 50, 70]
        for i in range(8):
            self.tableWidget.setColumnWidth(i,values[i])
         

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
        #refactor after code from design-generator
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget = CustomTableWithGoods(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(140, 70, 801, 721))
        self.tableWidget.setMaximumSize(QtCore.QSize(801, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0,i, item)
        #refactor this after
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Арт"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Закупка"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Нац"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Продаж"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Кол-во."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ГРН"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.verticalHeader().setDefaultSectionSize(9)
        self.tableWidget.verticalHeader().setVisible(False)


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
    @staticmethod
    def get_category_values():
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
        list_with_results = Views_Main_Window.get_category_values()
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
            #article_old = value[0]
            name = value[1]
            qty = value[2]
            buy = value[3]
            sell = value[4]
            profit = value[5]
            category = value[6]
            currency = value[7]
            sell_uah = value[8]
            article = value[9]
            res.append({"name":name,
                        'qty':qty,"buy":buy,"sell":sell,
                        "profit":profit,"category":category,
                        "currency":currency,"sell_uah":sell_uah,
                        "article":article})
        self.goods_from_category = res
        return res





    def get_goods(self,category_name,default=False):
        db = Bicycle_db()
        if category_name is None:
            category_name ='Всі'
        category_id = db.select('SELECT id from categories  where name like "%{}%"'.format(category_name))
        goods = db.edit('Select * from goods where category like "%{}%";'.format(category_id[0]))
        db.close()
        return self.from_sqlgoods_to_dict(goods)
    


    
    def display_goods_from_category(self,for_search=False):
        list_with_goods = []
        try:
            current_category = self.treeWidget.currentItem().text(0)
        except:
            current_category = None
        #warning here
        if isinstance(for_search, list):
            list_with_goods = for_search
        else:
            list_with_goods = self.get_goods(current_category)
        self.tableWidget.insertRow(len(list_with_goods))
        self.tableWidget.setRowCount(len(list_with_goods))
        row = len(list_with_goods)
        
        for good in list_with_goods:
            row -=1
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(good["article"])))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(good["name"])))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(good["buy"])))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(good["sell"])))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(good["profit"])))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(good['qty'])))

            self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(good["sell_uah"])))

    def finder(self,window_for_search):
        values = []
        row =self.tableWidget.rowCount()
        
        for i in range(row):
            item =self.tableWidget.item(i, 0)
            values.append(item.text())
        text = re.compile(r"{}".format(window_for_search.text()))
        return  list(filter(text.match, values))


    def find_in(self,textinput,where):
        res = self.finder(textinput)
        values_for_dispay = []
        for good in self.goods_from_category:
            for article in res:
                if str(good[where]) == article:
                    values_for_dispay.append(good)
        self.goods_from_category = values_for_dispay
        self.display_goods_from_category(values_for_dispay)
        
        
        # if text_for_search == headertext:
        #     cell = widget.item(row, 0).text()   # get cell at row, col
        #     print(cell)

            

    
    def add_actions(self):
        #calling in UI
        self.add_additional_custom_elements()
        #self.add_goods_action.triggered.connect(self.show_insert_window)
        self.treeWidget.clicked.connect(self.display_goods_from_category)
        self.tableWidget.clicked.connect(self.parse_row)
        self.lineEdit.textChanged.connect(lambda:self.find_in(self.lineEdit,'article'))
        self.lineEdit_4.textChanged.connect(lambda: self.find_in(self.lineEdit_4,'name'))
        self.lineEdit.inputRejected.connect(lambda:self.find_in(self.lineEdit,'article'))
        self.lineEdit_4.inputRejected.connect(lambda: self.find_in(self.lineEdit_4,'name'))
        #self.statusBar.showMessage()

        
