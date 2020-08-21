# import PySide2.QtCore as QtCore
# import PySide2.QtGui as QtGui
from PySide2 import QtWidgets, QtCore, QtGui
import random, string


def base_str():
    return random.choice(string.ascii_letters) + random.choice(string.digits)


class CustomSortModel(QtCore.QSortFilterProxyModel):
    def lessThan(self, left, right):
        # USE CUSTOM SORTING LOGIC HERE
        lvalue = left.data()
        rvalue = right.data()
        return lvalue[::-1] < rvalue[::-1]


class CustomTableWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(CustomTableWidget, self).__init__(parent)
        self.model = QtGui.QStandardItemModel(rows, columns)
        self.table = QtWidgets.QTableView()
        self.proxy_model = CustomSortModel()
        self.setItems()
        self.table.setSortingEnabled(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)

        self.model.itemChanged.connect(self.update_proxy)

        self.update_proxy()

    def setItems(self):
        self.model.setHorizontalHeaderLabels([str(x) for x in range(1, columns + 1)])
        for row in range(rows):
            for column in range(columns):
                item = QtGui.QStandardItem(str(base_str()))
                self.model.setItem(row, column, item)

    def update_proxy(self, item=None):
        self.proxy_model.setSourceModel(self.model)
        self.table.setModel(self.proxy_model)


class StandardTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent):
        super(StandardTableWidget, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setRowCount(rows)
        self.setColumnCount(columns)
        self.setSortingEnabled(True)
        self.setItems()

    def setItems(self):
        for row in range(rows):
            for column in range(columns):
                item = QtGui.QTableWidgetItem()
                item.setText(str(base_str()))
                self.setItem(row, column, item)


if __name__ == "__main__":

    rows = 10
    columns = 5
    useCustomSorting = True

    app = None
    if QtWidgets.QApplication.instance() is None:
        app = QtWidgets.QApplication([])

    if useCustomSorting:
        widget = CustomTableWidget(None)
    else:
        widget = StandardTableWidget(None)

    widget.show()

    if app:
        app.exec_()
