from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from insert_into_base import Insert_Into_Window
from custom_widgets import CustomTreeWidget
import sqlite3
from db import Bicycle_db





class Views_Main_Window: 

    def add_additional_custom_elements(self):
        self.add_custom_tree()
        self.fill_tree()        

    def show_insert_window(self):
        widget = QDialog()
        ui = Insert_Into_Window()
        ui.setupUi(widget)
        widget.exec_()

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


    def fill_tree(self):
        #separate_this
        list_dict_with_results = []
        db = Bicycle_db()
        db = sqlite3.connect('bicycle_db.sqlite')
        cursor = db.cursor()
        sql1="Select * FROM categories"
        cursor.execute(sql1)
        result = cursor.fetchall()
        count = (len(result))
        for item in result:
            id = item[0]
            name_category = item[1]
            parent_id = item[2]
            export_date = item[3]
            list_dict_with_results.append({'id':id,'name_category':name_category,'parent_id':parent_id,'export_date':export_date})
        #print(list_dict_with_results)
        #sort_by_id
        list_with_results = sorted(list_dict_with_results, key=lambda k: k['parent_id'])
        childs_categories = self.find_child_category(list_with_results)

        for res in list_dict_with_results:
            if res['parent_id'] == -1:
                item =QtWidgets.QTreeWidgetItem([res['name_category']])
                current_index = self.treeWidget.currentItem()
                self.treeWidget.addTopLevelItem(item)
                for child in childs_categories:
                    if res['id'] == child['id']:
                        if len(child['childs'])!=0:
                            for element in child['childs']:
                          
                                QtWidgets.QTreeWidgetItem(item, [element])




#        cursor.close()
        # cg = QtWidgets.QTreeWidgetItem(self.treeWidget,['top_carrot'])
        # c1 = QtWidgets.QTreeWidgetItem(cg,['carrot','0.99'])
        # h = QtWidgets.QTreeWidgetItem(['ham','50.15'])
        # self.treeWidget.addTopLevelItem(h)

    
    
    @QtCore.Slot()
    def actionClicked(self):
        action = self.sender()
        print('Action: ', action.text())
    def mouseMoveEvent(self, event):
        self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))

    def add_actions(self):
        #calling in UI
        self.add_additional_custom_elements()
        self.add_goods_action.triggered.connect(self.show_insert_window)
        self.treeWidget.clicked.connect(self.show_insert_window)