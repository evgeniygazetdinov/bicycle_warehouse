from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from insert_into_base import Insert_Into_Window
from custom_widgets import CustomTreeWidget
 





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

    def listItemRightClicked(self, QPos): 
          

        self.listMenu= QtWidgets.QMenu()
        menu_item = self.listMenu.addAction("Remove Item")
        
        #self.listMenu.move(self.treeWidget.mapToGlobal(QtCore.QPoint(1,1)))
        self.listMenu.show() 

    def add_custom_tree(self):
        self.treeWidget = CustomTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 131, 741))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "имя")


    def fill_tree(self):
        cg = QtWidgets.QTreeWidgetItem(self.treeWidget,['top_carrot'])
        c1 = QtWidgets.QTreeWidgetItem(cg,['carrot','0.99'])
        h = QtWidgets.QTreeWidgetItem(['ham','50.15'])
        self.treeWidget.addTopLevelItem(h)

    
    
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