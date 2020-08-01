from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog
from new_category_window import Ui_New_Category_Form




class CustomTreeWidget(QtWidgets.QTreeWidget):

    def __init__(self, parent = None):
           QtWidgets.QTreeWidget.__init__(self, parent)

    def contextMenuEvent(self, event):
           #handle right_click
           menu = QtWidgets.QMenu(self)
           add_category_Action = menu.addAction("добавить категорию")
           edit_category_Action = menu.addAction("редактировать категорию")
           remove_category_Action = menu.addAction("удалить категорию")
           action = menu.exec_(self.mapToGlobal(event.pos()))
           if action == add_category_Action:
                     widget = QDialog()
                     #send_to form
                     ui = Ui_New_Category_Form()
                     ui.setupUi(widget)
                     widget.exec_()
           if action == remove_category_Action:
                  item = self.currentItem()
                  self.removeChild(item)
                  print('this removeadd')
           if action == edit_category_Action:
                  item = self.currentItem()
                  print( item.text(0))
                  print('this editadd')