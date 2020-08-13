from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtWidgets import QDialog
from good_form import GoodsForm
from db import Bicycle_db



class CustomTreeWidget(QtWidgets.QTreeWidget):

    def __init__(self, parent = None):
           QtWidgets.QTreeWidget.__init__(self, parent)
    def mousePressEvent(self, event):
           super(CustomTreeWidget,self).mousePressEvent(event)
           print('HERE')


    def contextMenuEvent(self, event):
           #handle right_click
           menu = QtWidgets.QMenu(self)
           add_category_Action = menu.addAction("добавить категорию")
           add_sub_category_Action = menu.addAction("добавить подкатегорию")
           edit_category_Action = menu.addAction("редактировать категорию")
           remove_category_Action = menu.addAction("удалить категорию")
           action = menu.exec_(self.mapToGlobal(event.pos()))
           db = Bicycle_db()
           if action == add_category_Action:
              text, ok = QtWidgets.QInputDialog.getText(self, "Добавить категорию", "Имя для категории:")
              if ok and text != "":
                     rowcount = self.topLevelItemCount()
                     self.addTopLevelItem(QtWidgets.QTreeWidgetItem(rowcount))
                     self.topLevelItem(rowcount).setText(0,text)
                     res = db.insert('INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",-1);'.format(text))
                     print(res)
                     db.close()
           if action == remove_category_Action:
                  item = self.currentItem()
                  for SelectedItem in self.selectedItems():
                     if SelectedItem.text(0) == item.text(0):
                            #check category is not null
                            qm = QtWidgets.QMessageBox()
                            ret = qm.question(self,'', "Удалить категорию?", qm.Yes | qm.No)
                            if ret == qm.Yes:
                                   SelectedItem.removeChild(item)
                                   text = item.text(0)
                                   query = 'DELETE FROM categories WHERE name LIKE "%{}%";'.format(text)
                                   db.insert(query)
                                   db.close()
           if action == edit_category_Action:
                  if self.selectedItems():
                     old_name = self.currentItem().text(0)
                     item = self.selectedItems()[0]
                     text, ok = QtWidgets.QInputDialog.getText(self, "Редактировать", "редактировать:", QtWidgets.QLineEdit.Normal, item.text(0))
                     if ok and text != "":
                            item.setText(0, text)
                            res = db.insert('UPDATE categories set name = "{}" where name like "%{}%";'.format(text,old_name))
                            
           if action == add_sub_category_Action:
                  text, ok = QtWidgets.QInputDialog.getText(self, "Добавить подкатегорию", "Имя для подкатегории:")
                  if ok and text != "":
                         db = Bicycle_db()
                         if len(self.selectedItems()) > 0:
                            QtWidgets.QTreeWidgetItem(self.selectedItems()[0], [text])
                            parent_id = db.insert('select id from categories where name like "%{}%"'.format(self.currentItem().text(0)))
                            db.insert('INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",{});'.format(text,parent_id[0][0]))
                         else:
                            print('here')
                            QtWidgets.QTreeWidgetItem(self, [text])
                            res = db.insert('INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",-1);'.format(text))
       



class TreeWidgetGoods(CustomTreeWidget):

    def contextMenuEvent(self,event):
           pass

class ProcentItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
       return (self.data(QtCore.Qt.UserRole) >
                other.data(QtCore.Qt.UserRole))

class NumericItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        return (self.data(QtCore.Qt.UserRole) <
                other.data(QtCore.Qt.UserRole))
       # def __init__(self, text, sortKey):
       #      QtGui.QTableWidgetItem.__init__(self, text, QtGui.QTableWidgetItem.UserType)
       #      self.sortKey = sortKey

    #Qt uses a simple < check for sorting items, override this to use the sortKey
       # def __lt__(self, other):
       #      return self.sortKey > other.sortKey 


class CustomTableWithGoods(QtWidgets.QTableWidget):
       
       def __init__(self, parent = None,values=None,category_widget=None):
           QtWidgets.QTableWidget.__init__(self, parent)
           self.values = values
           self.last_added_category = 'Всі'
           self.category_widget = category_widget
           self.sortItems(0, QtCore.Qt.AscendingOrder)
           self.setSortingEnabled(True)
           self.goods_from_table = []
           self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)



       def parse_row(self):
              columns = self.columnCount()
              names = []
              values = []
              
              for i in range(columns):
                  names.append(self.horizontalHeaderItem(i).text())
              for i in range(columns):
                     values.append(self.item(self.currentRow(),i).text())
              return dict(zip(names,values))

       def from_sqlgoods_to_dict(self,goods):
              res = tuple()
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
                     data ={'name':name,'qty':qty,"buy":buy,"sell":sell,
                                   "profit":profit,"category":category,
                                   "currency":currency,"sell_uah":sell_uah,
                                   "article":article}
                     res+=(data,)
                     self.goods_from_table = res
              return res


       def get_goods(self,category_name=False,display_all=None):
              db = Bicycle_db()
              if display_all:
                     goods = db.edit('Select * from goods')
                     db.close()
                     return self.from_sqlgoods_to_dict(goods)
              else:       
                     if category_name is None:
                            category_name ='Всі'
                     category_id = db.select('SELECT id from categories  where name like "%{}%"'.format(category_name))
                     goods = db.edit('Select * from goods where category like "%{}%";'.format(category_id[0]))
                     db.close()
                     return self.from_sqlgoods_to_dict(goods)

       def calculate_sell_price(self,sell,buy):
              dif = abs(float(buy) - float(sell))
              return (str(int(round((dif/buy)*100,1))))+'%'





       def display_goods(self,tree=False,for_search=False):
              list_with_goods = []
              current_category = None
              # if tree:
              current_category = tree
              list_with_goods = self.get_goods(display_all=True)
              row= len(list_with_goods)
              self.insertRow(row)
              self.setRowCount(row)
              self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
              self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
              for good in list_with_goods:
                     row -=1
                     item = NumericItem()
                     item.setFlags(QtCore.Qt.ItemIsEnabled)
                     item.setData(QtCore.Qt.DisplayRole,good["article"])
                     
                     self.setItem(row,0,QtWidgets.QTableWidgetItem(item))
                     item.setData(QtCore.Qt.DisplayRole,good["name"])
                     self.setItem(row,1,QtWidgets.QTableWidgetItem(item))
              #item = QtWidgets.QTableWidgetItem()
                     if good['buy'] == int(good['buy']):
                            item.setData(QtCore.Qt.DisplayRole,int(good["buy"]))             
                            self.setItem(row,2,QtWidgets.QTableWidgetItem(item))
                     else:
                            item.setData(QtCore.Qt.DisplayRole,good["buy"])
                            self.setItem(row,2,QtWidgets.QTableWidgetItem(item))
                     #item = QtWidgets.QTableWidgetItem()    
                     if good['sell'] == int(good['sell']):
                            item.setData(QtCore.Qt.DisplayRole,int(good["sell"]))
                            self.setItem(row,4,QtWidgets.QTableWidgetItem(item)) 
                     else:
                            item.setData(QtCore.Qt.DisplayRole,(good["sell"]))
                            self.setItem(row,4,QtWidgets.QTableWidgetItem(item))
                     item = NumericItem()
                     item.setData(QtCore.Qt.DisplayRole,(self.calculate_sell_price(good['sell'],good['buy'])))      
                     self.setItem(row,3,QtWidgets.QTableWidgetItem(item))
                     item = NumericItem()
                     item.setData(QtCore.Qt.DisplayRole,(good["qty"]))
                     self.setItem(row,5,QtWidgets.QTableWidgetItem(item))
                     #item = QtWidgets.QTableWidgetItem()
                     item.setData(QtCore.Qt.DisplayRole,(good["sell_uah"]))
                     self.setItem(row,6,QtWidgets.QTableWidgetItem(item))

       def update_table(self):
              db = Bicycle_db()
              cat = 'Всі'
              # try:
              #        cat = (db.insert('select name_category from cur_category where id=(select max(id) from cur_category)'))[0][0]
              #        print('here')
              # except:
              #        pass
              self.display_goods()       

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
                     ui = GoodsForm(table=self)
                     ui.setupUi(widget)
                     widget.exec_()


              if action == remove_Action:
                     reply = QtWidgets.QMessageBox.question(self, 'Удалить товар?',
                                     'Вы уверенны что хотите удалить?',
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

                     if reply == QtWidgets.QMessageBox.Yes:
                            values= self.parse_row()
                            if values['Кол-во.'] != '0':
                                   # widget = QDialog()
                                   error_dialog = QtWidgets.QErrorMessage(self)
                                   error_dialog.showMessage('товар с количеством удалить нельзя')

                                   # widget.exec_()
                            else:       
                                   db = Bicycle_db()
                                   db.insert("DELETE FROM goods WHERE article LIKE '%{}%'".format(values['Арт']))
                                   self.update_table()
                                   db.close()

              if action == edit_Action:
                     widget = QDialog()
                     ui = GoodsForm(table=self,values=self.parse_row(),category_widget=self.category_widget)
                     ui.setupUi(widget)
                     widget.exec_()

class CartTable(CustomTableWithGoods):
       def __init__(self, parent = None,profit=None,total=None):
           QtWidgets.QTableWidget.__init__(self, parent)

           self.sortItems(0, QtCore.Qt.AscendingOrder)
           self.setSortingEnabled(True)
           self.profit = profit
           self.total = total

       def clean_table(self):
              while self.rowCount() >0:
                     self.removeRow(0)
              if self.profit:
                     self.profit.setText('')
              if self.total:
                     self.total.setText('')



       def contextMenuEvent(self,event):
              pass



class CustomMainWindow(QtWidgets.QMainWindow):
       def __init__(self):
              super().__init__()

       

     
       def closeEvent(self, event):
              db = Bicycle_db()
              db.insert('drop table if exists cur_category')
              db.close()
              event.accept()