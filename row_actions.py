#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from pandas import DataFrame
import sys
import csv
  
  
data_single = {'hi': ['a', 'b'], 'hi2': ['d', 'c']}
tell_row=1
  
class TableWidget(QTableWidget):
    def __init__(self, df, parent=None):
        QTableWidget.__init__(self, parent)
        self.df = df
        nRows = len(self.df.index)
        nColumns = len(self.df.columns)
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)
  
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                x = self.df.iloc[i, j]
                self.setItem(i, j, QTableWidgetItem(x))
  
        self.cellChanged.connect(self.onCellChanged)
  
    #@pyqtSlot(int, int)
    def onCellChanged(self, row, column):
        text = self.item(row, column).text()
        number = float(text)
        self.df.set_value(row, column, number)
  
  
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
  
    def initUI(self):
        self.setGeometry(700, 100, 350, 380)
        df_rows = tell_row
        df_cols = 1
        df =pd.DataFrame(data_single)
        self.tableWidget = TableWidget(df, self)
  
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.button = QPushButton('Print DataFrame', self)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.writeCsv)
  
    @Slot()
    def print_my_df(self):
        some_df =self.tableWidget.df
        print(some_df)
  
        fn, _ = QFileDialog.getSaveFileName(self, 'Speichern unter', None, 'Excel Dateien (.xlsx);;Alle Dateien()')
        if fn != '':
            if QFileInfo(fn).suffix() == "": fn += '.xlsx'
        df = DataFrame(some_df)
        df.to_excel(fn, sheet_name='Ergebnisse', index=False)
 
    def writeCsv(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/export.csv", "CSV Files(*.csv *.txt)")
        if path:
            with open(path, 'w') as stream:
                print("saving", path)
                writer = csv.writer(stream, delimiter='\t')
                headers = []
                for column in range(self.tableWidget.columnCount()):
                    header = self.tableWidget.horizontalHeaderItem(column)
                    if header is not None:
                         headers.append(header.text())
                    else:
                        headers.append("Column " + str(column))
                writer.writerow(headers)
                for row in range(self.tableWidget.rowCount()):
                    rowdata = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
  
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

