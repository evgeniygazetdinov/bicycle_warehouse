from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtWidgets import QDialog
from new_category_window import Ui_New_Category_Form
from good_form import GoodsForm
from db import Bicycle_db



class CustomTreeWidget(QtWidgets.QTreeWidget):

    def __init__(self, parent = None):
           QtWidgets.QTreeWidget.__init__(self, parent)


    def contextMenuEvent(self, event):
           #handle right_click
           menu = QtWidgets.QMenu(self)
           add_category_Action = menu.addAction("добавить категорию")
           add_sub_category_Action = menu.addAction("добавить подкатегорию")
           edit_category_Action = menu.addAction("редактировать категорию")
           remove_category_Action = menu.addAction("удалить категорию")
           action = menu.exec_(self.mapToGlobal(event.pos()))
           if action == add_category_Action:
              text, ok = QtWidgets.QInputDialog.getText(self, "Добавить подкатегорию", "Имя для подкатегории:")
              if ok and text != "":
                     rowcount = self.topLevelItemCount()
                     self.addTopLevelItem(QtWidgets.QTreeWidgetItem(rowcount))
                     self.topLevelItem(rowcount).setText(0,text)
           if action == remove_category_Action:
                  item = self.currentItem()
                  for SelectedItem in self.selectedItems():
                     if SelectedItem.text(0) == item.text(0):
                            SelectedItem.removeChild(item)
                            db = Bicycle_db()
                            db.edit("DELETE FROM categories WHERE name LIKE '%{}%';".format(item.text(0)))
           if action == edit_category_Action:
                  if self.selectedItems():
                     item = self.selectedItems()[0]
                     text, ok = QtWidgets.QInputDialog.getText(self, "Редактировать", "редактировать:", QtWidgets.QLineEdit.Normal, item.text(0))
                     if ok and text != "":
                            item.setText(0, text)
           if action == add_sub_category_Action:
                  text, ok = QtWidgets.QInputDialog.getText(self, "Добавить подкатегорию", "Имя для подкатегории:")
                  if ok and text != "":
                         if len(self.selectedItems()) > 0:
                            QtWidgets.QTreeWidgetItem(self.selectedItems()[0], [text])
                         else:
                            QtWidgets.QTreeWidgetItem(self, [text])


class TreeWidgetGoods(CustomTreeWidget):

       def contextMenuEvent(self,event):
              pass


class CustomTableWithGoods(QtWidgets.QTableWidget):
       
       def __init__(self, parent = None,values=None):
           QtWidgets.QTableWidget.__init__(self, parent)
           self.values = values
           self.last_added_category = 'Всі'

       def parse_row(self):
              columns = self.columnCount()
              names = []
              values = []
              for i in range(columns):
                  names.append(self.horizontalHeaderItem(i).text())
              for i in range(columns):
                     values.append(self.item(self.currentRow(),i).text())
              return dict(zip(names,values))


       def remove_values_from_row(self):
              pass

        
       def contextMenuEvent(self,event):
              menu = QtWidgets.QMenu(self)
              add_Action = menu.addAction("добавить")
              edit_Action = menu.addAction("редактировать")
              remove_Action = menu.addAction("удалить")
              action = menu.exec_(self.mapToGlobal(event.pos()))
              if action == add_Action:
                     widget = QDialog()
                     ui = GoodsForm()
                     ui.setupUi(widget)
                     widget.exec_()

              if action == remove_Action:
                     values = self.parse_row()
              if action == edit_Action:
                     widget = QDialog()
                     ui = GoodsForm(values=self.parse_row())
                     ui.setupUi(widget)
                     widget.exec_()

class CartTable(CustomTableWithGoods):



       def contextMenuEvent(self,event):
              pass
