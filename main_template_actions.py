
from main_template import Ui_MainWindow
from PySide2 import QtWidgets, QtCore, QtGui


class Main_Template_Runner(Ui_MainWindow):
    def __init__(self):
        self.add_actions()
        
    def show_insert_window(self):
        widget = QDialog()
        ui = Insert_Into_Window()
        ui.setupUi(widget)
        widget.exec_()

    def add_actions(self):
        self.add_goods_action.triggered.connect(self.show_insert_window)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main_Template_Runner()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

