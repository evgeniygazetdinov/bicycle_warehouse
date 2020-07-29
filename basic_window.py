import sys
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setGeometry(100, 100, 800, 800)
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My first label')
        self.label.move(20, 50)
        self.createTable()

    def createTable(self):
    # Create table
        print('here')
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,100)
        self.tableWidget.doubleClicked.connect(self.on_click)

    
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        self.button = QtWidgets.QPushButton(self)
        self.button.setText('click me')
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('button are pressed')

    def changeHorizontalHeader(self, index):
        oldHeader = self.table.horizontalHeaderItem(index).text()
        newHeader, ok = QtGui.QInputDialog.getText(self,
                                                      'Change header label for column %d' % index,
                                                      'Header:',
                                                       QtGui.QLineEdit.Normal,
                                                       oldHeader)
        if ok:
            self.table.horizontalHeaderItem(index).setText(newHeader)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main_Window()
    win.show()
    sys.exit(app.exec_())