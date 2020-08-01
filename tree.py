import sys

from PySide2 import QtWidgets,QtCore

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)


tw = QtWidgets.QTreeWidget()
tw.setAlternatingRowColors(True)
tw.setHeaderLabels(['none','1','2'])
cg = QtWidgets.QTreeWidgetItem(tw,['carrots','0.99'])
c1 = QtWidgets.QTreeWidgetItem(cg,['carrot','0.99'])
h = QtWidgets.QTreeWidgetItem(['ham','50.15'])

tw.addTopLevelItem(h)


layout.addWidget(tw)
window.show()

sys.exit(app.exec_())