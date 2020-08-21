from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog
from widgets.good_form import GoodsForm
from library.db import Bicycle_db


class CustomTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        QtWidgets.QTreeWidget.__init__(self, parent)

    def mousePressEvent(self, event):
        super(CustomTreeWidget, self).mousePressEvent(event)
        print("HERE")

    def contextMenuEvent(self, event):
        # handle right_click
        menu = QtWidgets.QMenu(self)
        add_category_Action = menu.addAction("добавить категорию")
        add_sub_category_Action = menu.addAction("добавить подкатегорию")
        edit_category_Action = menu.addAction("редактировать категорию")
        remove_category_Action = menu.addAction("удалить категорию")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        db = Bicycle_db()
        if action == add_category_Action:
            text, ok = QtWidgets.QInputDialog.getText(
                self, "Добавить категорию", "Имя для категории:"
            )
            if ok and text != "":
                rowcount = self.topLevelItemCount()
                self.addTopLevelItem(QtWidgets.QTreeWidgetItem(rowcount))
                self.topLevelItem(rowcount).setText(0, text)
                res = db.insert(
                    'INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",-1);'.format(
                        text
                    )
                )
                print(res)
                db.close()
        if action == remove_category_Action:
            item = self.currentItem()
            for SelectedItem in self.selectedItems():
                if SelectedItem.text(0) == item.text(0):
                    # check category is not null
                    qm = QtWidgets.QMessageBox()
                    ret = qm.question(self, "", "Удалить категорию?", qm.Yes | qm.No)
                    if ret == qm.Yes:
                        SelectedItem.removeChild(item)
                        text = item.text(0)
                        query = 'DELETE FROM categories WHERE name LIKE "%{}%";'.format(
                            text
                        )
                        db.insert(query)
                        db.close()
        if action == edit_category_Action:
            if self.selectedItems():
                old_name = self.currentItem().text(0)
                item = self.selectedItems()[0]
                text, ok = QtWidgets.QInputDialog.getText(
                    self,
                    "Редактировать",
                    "редактировать:",
                    QtWidgets.QLineEdit.Normal,
                    item.text(0),
                )
                if ok and text != "":
                    item.setText(0, text)
                    res = db.insert(
                        'UPDATE categories set name = "{}" where name like "%{}%";'.format(
                            text, old_name
                        )
                    )

        if action == add_sub_category_Action:
            text, ok = QtWidgets.QInputDialog.getText(
                self, "Добавить подкатегорию", "Имя для подкатегории:"
            )
            if ok and text != "":
                db = Bicycle_db()
                if len(self.selectedItems()) > 0:
                    QtWidgets.QTreeWidgetItem(self.selectedItems()[0], [text])
                    parent_id = db.insert(
                        'select id from categories where name like "%{}%"'.format(
                            self.currentItem().text(0)
                        )
                    )
                    db.insert(
                        'INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",{});'.format(
                            text, parent_id[0][0]
                        )
                    )
                else:
                    print("here")
                    QtWidgets.QTreeWidgetItem(self, [text])
                    res = db.insert(
                        'INSERT INTO categories (id,name,parent_id) values((SELECT MAX(id)from categories)+1,"{}",-1);'.format(
                            text
                        )
                    )
