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
from custom_widgets import NumericItem


class Views_Main_Window(FixesMainWindow): 
    def __init__(self):
        self.current_row = {}
        self.goods_from_category = []
        self.cart_items = []
        self.total_price = 0
        self.total_income = 0
        self.course = 27.69
        
        
    def parse_row_and_move_to_cart(self):
        self.total_price = 0
        row = self.tableWidget_2.rowCount()
        values = self.tableWidget.parse_row()
        self.tableWidget_2.insertRow(row+1)
        self.tableWidget_2.setRowCount(row+1)
        self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(str(values['Название'])))
        self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(str(values['ГРН'])))
        self.cart_items.append(values)
        self.counting_price_income_from_cart_items("ГРН",'Закупка',"Продаж")
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))
        self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(str((self.total_price))))
    
    
    def remove_from_cart(self):
        values = self.tableWidget_2.parse_row()
        print(values)

    def calculate_good_income(self,sell,buy):
        income = round(abs((float(sell)-float(buy)))*self.course,1)
        self.total_income+=income
        


    def counting_price_income_from_cart_items(self,grivna_keyword,sell_keyword=False,buy_keyword=False,sale=False):
        for item in self.cart_items:
            self.total_price+=(int(item[grivna_keyword]))
            
            if ('Арт' in item):
                if sell_keyword:
                    income = self.calculate_good_income(item[sell_keyword],item[buy_keyword])
        if sale:
            self.total_price -= int(sale)
        
    def show_insert_window(self):
        pass
    
    
         

    def get_values_from_db(self):
        self.set_into_table_goods()
        self.set_into_categories_table()

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
        res = tuple()
        for value in goods:
            name = value[1]
            qty = value[2]
            buy = value[3]
            sell = value[4]
            profit = value[5]
            category = value[6]
            currency = value[7]
            sell_uah = value[8]
            article = value[9]
            data ={'name':name,'qty':qty,"buy":buy,"sell":sell,
                        "profit":profit,"category":category,
                        "currency":currency,"sell_uah":sell_uah,
                        "article":article}
            res+=(data,)
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
    
    def calculate_sell_price(self,sell,buy):
        dif = abs(float(buy) - float(sell))
        res = round((dif/buy)*100,1)
        if res == int(res):
            return str(int(res))
        else:
            return str(res)

    
    def display_goods_from_category(self,for_search=False):
        list_with_goods = []
        try:
            current_category = self.treeWidget.currentItem().text(0)
        except:
            current_category = None
        #warning here
        if isinstance(for_search, list):
            list_with_goods = for_search
        elif isinstance(for_search,str):
            current_category=  for_search
            list_with_goods = self.get_goods(current_category)
            row= len(list_with_goods)
            self.tableWidget.insertRow(row)

            self.tableWidget.setRowCount(row)
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        else:
            list_with_goods = self.get_goods(current_category)
        row= len(list_with_goods)
        self.tableWidget.insertRow(row)

        self.tableWidget.setRowCount(row)
        #self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for good in list_with_goods:
            row -=1
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.DisplayRole,good["article"])
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(good["name"])))
            #item = QtWidgets.QTableWidgetItem()
            if good['buy'] == int(good['buy']):
                item.setData(QtCore.Qt.DisplayRole,int(good["buy"]))             
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(item))
            else:
                item.setData(QtCore.Qt.DisplayRole,good["buy"])
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(item))
            #item = QtWidgets.QTableWidgetItem()    
            if good['sell'] == int(good['sell']):
                item.setData(QtCore.Qt.DisplayRole,int(good["sell"]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(item)) 
            else:
                item.setData(QtCore.Qt.DisplayRole,(good["sell"]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(item))
            #item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole,self.calculate_sell_price(good['sell'],good['buy'])+'%')      
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(item))
            #item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole,(good["qty"]))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(item))
            #item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole,(good["sell_uah"]))
            self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(item))
            
            
    def finder(self,window_for_search,word_search=False):
        values = []
        self.display_goods_from_category(self.goods_from_category)
        row =self.tableWidget.rowCount()
        if word_search:
            column_for_search = 1
        else:
            column_for_search = 0
        for i in range(row):
            item =self.tableWidget.item(i, column_for_search)
            values.append(item.text())
        text = re.compile(r"{}".format(window_for_search.text()))
        if word_search:
            #find substring in string
            res = [s for s in values if "{}".format((window_for_search.text()).lower()) in s.lower()]
        else:
            #find by first
            res = list(filter(text.search, values))
        return  res


    def find_in(self,textinput,where,word_search=False):
        if word_search:
            res = self.finder(textinput,True)
        else:
            res = self.finder(textinput)
     
        values_for_dispay = []
        for good in self.goods_from_category:
            for article in res:
                if str(good[where]) == article:
                    values_for_dispay.append(good)
        self.display_goods_from_category(values_for_dispay)

    def set_current_category(self, category):
        db = Bicycle_db()
        
        query = 'CREATE TABLE IF NOT EXISTS cur_category (id INTEGER PRIMARY KEY AUTOINCREMENT, name_category TEXT);'    
        query_2 = 'insert into cur_category(name_category) values("{}")'.format(category)
        db.insert(query)
        db.insert(query_2)
        db.close()
    

    def hander_for_handy_buttons(self,line_edit,button):
        self.total_price = 0
        price = line_edit.text()
        specific = button.text()
        row = self.tableWidget_2.rowCount()
        item = QtWidgets.QTableWidgetItem()
        item.setData(QtCore.Qt.DisplayRole,(price))
        self.tableWidget_2.insertRow(row+1)
        self.tableWidget_2.setRowCount(row+1)
        self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(str(specific)))
        self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(item)) 
        
        if button == self.sale_button:
            self.counting_price_income_from_cart_items('ГРН',sale=price)
        else:
            self.cart_items.append({'Название':specific,'ГРН':price})
            self.counting_price_income_from_cart_items('ГРН')
        # self.cart_items.append(values)
        #self.counting_price_income_from_cart_items("Продаж",'Закупка',"ГРН")
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))
        self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(str((self.total_price))))
    def clean_cart(self):
        self.total_price=0
        self.cart_items = []
        self.total_income =0
        self.tableWidget_2.clean_table()

    
    def add_actions(self):
        #calling in UI
        self.add_additional_custom_elements()
        #self.add_goods_action.triggered.connect(self.show_insert_window)
        self.treeWidget.clicked.connect(self.display_goods_from_category)
        self.tableWidget.doubleClicked.connect(self.parse_row_and_move_to_cart)
        #show name good on bottom
        self.tableWidget.clicked.connect(lambda:self.statusBar.showMessage(self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn()).text()))
        self.tableWidget_2.clicked.connect(lambda:self.statusBar.showMessage(self.tableWidget_2.item(self.tableWidget_2.currentRow(), self.tableWidget_2.currentColumn()).text()))
        self.tableWidget_2.doubleClicked.connect(self.remove_from_cart)
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
        self.lineEdit.textChanged.connect(lambda:self.find_in(self.lineEdit,'article'))
        self.lineEdit_4.textChanged.connect(lambda: self.find_in(self.lineEdit_3,'name',word_search=True))
        self.lineEdit.inputRejected.connect(lambda:self.find_in(self.lineEdit,'article'))
        self.lineEdit_4.inputRejected.connect(lambda: self.find_in(self.lineEdit_4,'name',word_search=True))
        self.pushButton_8.clicked.connect(lambda : self.lineEdit.clear() )
        self.pushButton_8.clicked.connect(lambda:self.lineEdit_4.clear() )
        
