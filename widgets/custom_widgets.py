from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt

from PySide2.QtWidgets import QDialog
from widgets.good_form import GoodsForm
from widgets.category_tree import CustomTreeWidget
from library.db import Bicycle_db


class InputDialog(QDialog):
    def __init__(self, parent=None, value=None, qty=None):
        super().__init__(parent)
        self.value = value
        self.qty = qty
        #  self.second = QtWidgets.QLineEdit(self)
        self.setWindowTitle("изменить кол-во")
        buttonBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, self
        )
        layout = QtWidgets.QVBoxLayout(self)
        text = QtWidgets.QLabel(self.value)
        layout.addWidget(text)
        self.box = QtWidgets.QSpinBox(self)
        self.box.setMaximum(int(self.qty))
        if int(self.qty) > 0:
            self.box.setMinimum(1)
        self.box.setValue(int(1))
        layout.addWidget(self.box)
        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.box.value()


class TreeWidgetGoods(CustomTreeWidget):
    def contextMenuEvent(self, event):
        pass


class ProcentItem(QtWidgets.QTableWidgetItem):
    def __init__(self):
        super().__init__()

    def __gt__(self,other):
        print('fsdf')

    def __lt__(self, other):
       print('here')
       text_inside = int(str(self.text()).split('%')[-1])
       other_text_inside = int((str(self.other_text_inside()).split('%'))[-1])
       return text_inside < other_text_inside



class NumericItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)



class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        db = Bicycle_db()
        db.insert("drop table if exists cur_category")
        db.close()
        event.accept()
