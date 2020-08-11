from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtWidgets import QDialog
from new_category_window import Ui_New_Category_Form
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


class CustomTableWithGoods(QtWidgets.QTableWidget):
       
       def __init__(self, parent = None,values=None,category_widget=None):
           QtWidgets.QTableWidget.__init__(self, parent)
           self.values = values
           self.last_added_category = 'Всі'
           self.category_widget = category_widget
       
       def __lt__(self, otherItem):
              column = self.treeWidget().sortColumn()
              return self.text(column).toLower() < otherItem.text(column).toLower()
   
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
                     #self.goods_from_category = res
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
              return str(round((dif/buy)*100,1))







       def display_goods_from_category(self,for_search=False):
              list_with_goods = []
              try:
                     current_category = self.currentItem().text(0)
              except:
                     current_category = None
              #warning here
              if isinstance(for_search, list):
                     list_with_goods = for_search
              elif isinstance(for_search,str):
                     current_category=  for_search
                     list_with_goods = self.get_goods(current_category)
                     row= len(list_with_goods)
                     self.insertRow(row)

                     self.setRowCount(row)
                     self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
              else:
                     list_with_goods = self.get_goods(current_category)
                     row= len(list_with_goods)
                     self.insertRow(row)

                     self.setRowCount(row)
                     self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
              for good in list_with_goods:
                     row -=1
                     self.setItem(row,0,QtWidgets.QTableWidgetItem(str(good["article"])))
                     self.setItem(row,1,QtWidgets.QTableWidgetItem(str(good["name"])))
                     self.setItem(row,2,QtWidgets.QTableWidgetItem(str(good["buy"])))
                     self.setItem(row,4,QtWidgets.QTableWidgetItem(str(good["sell"])))
                     self.setItem(row,3,QtWidgets.QTableWidgetItem(str(self.calculate_sell_price(good['sell'],good['buy'])+'%')))
                     self.setItem(row,5,QtWidgets.QTableWidgetItem(str(good['qty'])))
                     self.setItem(row,6,QtWidgets.QTableWidgetItem(str(good["sell_uah"])))


       def update_table(self):
              db = Bicycle_db()
              cat = 'Всі'
              try:
                     cat = (db.insert('select name_category from cur_category where id=(select max(id) from cur_category)'))[0][0]
                     print('here')
              except:
                    pass # self.display_goods_from_category(cat)
              self.display_goods_from_category(cat)       

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