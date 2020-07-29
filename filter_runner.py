import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Qt, Slot, QFile
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide2.QtCharts import QtCharts
from PySide2.QtUiTools import QUiLoader
import sys
# from filter_template  import   Ui_MainWindow



 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        ui_file = QFile("filter.ui")
        loader = QUiLoader()
        window = loader.load(ui_file)
 
 
if __name__ == '__main__':
    # app = 0
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())