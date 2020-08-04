from main_template import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog

class Main(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.remove_uis()


    def remove_uis(self):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
