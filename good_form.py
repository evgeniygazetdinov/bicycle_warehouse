import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel,QDialog)
from db import Bicycle_db


class GoodsForm(QMainWindow):
    def __init__(self,new_good=False,values=False):
        super().__init__()
        self.values = values
        self.new_good = new_good
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 297)
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
        self.USD_value.setGeometry(QtCore.QRect(200, 10, 41, 16))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 20, 81, 21))
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
        self.additional_actions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle('добавить новый товар')
        if self.values:
            Form.setWindowTitle('изменить товар')
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
        self.label_9.setText(_translate("Form", "USD-"))
        self.USD_value.setText(_translate("Form", "30"))
        self.label_10.setText(_translate("Form", "Артикул"))
        self.category_title.setText(_translate("Form", "Категория"))

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







    def additional_actions(self):
        self.add_actions()
     
        self.fill_tree()
        if self.values:
            #when change_item
            self.lineEdit_4.setText(self.values['profit'])
            self.lineEdit_3.setText(self.values['sell'])
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_2.setText(self.values['buy'])
            self.lineEdit_6.setText(self.values['article'])
            self.lineEdit_5.setText(self.values['sell_uah'])
            self.lineEdit.setText(self.values['name'])
            self.spinBox.setValue(int(self.values['qty']))
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.label_9.setText('')
            self.comboBox.hide()
            self.label_4.hide()
            # move categories
            db = Bicycle_db()
            res = db.edit('Select category from goods where name like "%{}%"'.format(self.values['name']))
            ids = (str(res[0][0]).split())
            category_title = db.edit('select name from categories where id like "%{}%"'.format(res[0]))
            


   
            
    def store_values_from_form(self):

        def get_values_from_form():
            #get_data_from windows
            #get data from category 
            pass
        def store_data_from_form():
            pass

        from_form = get_values_from_form()
        store_data_from_form()

        
            

    def get_values_from_table(self):
        values = []
        headers = []
        for column in range(self.tableWidget.columnCount()):
            header = self.tableWidget.horizontalHeaderItem(column)
            if header is not None:
                    headers.append(header.text())
        for row in range(self.tableWidget.rowCount()):
            rowdata = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    rowdata.append(item.text())
                else:
                    rowdata.append('""')

            values.append(dict(zip(headers,rowdata)))
        return values
    
    def upload_to_base(self):
        res = []
        db = Bicycle_db()
        #add course
        values = self.get_values_from_table()
        for row in values:
            values = ','.join(map(str, row.values()))
            db.edit("insert into goods(article, article_old, name, qty, buy, profit, category, sell_uah ) values({});".format(values))
        print('executed')
        


    def add_actions(self):
        self.pushButton_2.clicked.connect(self.store_values_from_form)
        self.treeWidget.clicked.connect(lambda : self.category_title.setText(self.treeWidget.currentItem().text(0)))
        