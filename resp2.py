from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from lang import getLang
import sys, os, configparser

config = configparser.ConfigParser()
config.read("Settings.ini")

# Config get setting and change setting
#print(config.get("Main", "language"))
#config.set("Main", "language", "danish")
#with open("Settings.ini", "w") as cfg_file:
    #config.write(cfg_file)

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.x, self.y, self.w, self.h = 0, 0, 300, 200

        self.setGeometry(self.x, self.y, self.w, self.h)

        self.window = MainWindow(self)
        self.setCentralWidget(self.window)
        self.setWindowTitle("Window title") # Window Title
        self.show()

class MainWindow(QWidget):        
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        layout = QVBoxLayout(self)

        # Run this after settings
        self.lang = getLang(config.get("Main", "language"))

        # Initialize tabs
        tab_holder = QTabWidget()   # Create tab holder
        tab_1 = QWidget()           # Tab one
        tab_2 = QWidget()           # Tab two

        # Add tabs
        tab_holder.addTab(tab_1, self.lang["tab_1_title"]) # Add "tab1" to the tabs holder "tabs"
        tab_holder.addTab(tab_2, self.lang["tab_2_title"]) # Add "tab2" to the tabs holder "tabs" 

        # Create first tab
        tab_1.layout = QVBoxLayout(self)
        tab_2.layout = QVBoxLayout(self)

        # Buttons
        button_start = QPushButton(self.lang["btn_start"])
        button_stop = QPushButton(self.lang["btn_stop"])
        button_test = QPushButton(self.lang["btn_test"])

        # Button Extra
        button_start.setToolTip("This is a tooltip for the button!")    # Message to show when mouse hover
        button_start.clicked.connect(self.on_click)

        button_stop.clicked.connect(self.on_click)

        button_test.clicked.connect(self.on_click)
        #button_start.setEnabled(False)

        # comboBox
        label_language = QLabel("Language")
        combo_language = QComboBox(self)
        combo_language.addItem(self.lang["language_danish"])
        combo_language.addItem(self.lang["language_english"])

        # Move widgets
        combo_language.move(50, 150)
        label_language.move(50, 50)

        # Tab Binding
        self.AddToTab(tab_1, button_start)
        self.AddToTab(tab_1, button_stop)
        self.AddToTab(tab_2, label_language)
        self.AddToTab(tab_2, combo_language)

        # Add tabs to widget        
        tab_1.setLayout(tab_1.layout)
        tab_2.setLayout(tab_2.layout)
        layout.addWidget(tab_holder)
        self.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        button = self.sender().text()
        if button == self.lang["btn_start"]:
            print("Dank")
        elif button == self.lang["btn_stop"]:
            print("Not dank")

    def AddToTab(self, tab, obj):
        tab.layout.addWidget(obj)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())