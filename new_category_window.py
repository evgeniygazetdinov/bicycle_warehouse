# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_category.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel,QDialog)
from db import Bicycle_db

class Ui_New_Category_Form(QtWidgets.QMainWindow):
    def __init__(self,treeWidget,text_for_change=None,subcategory=False):
        self.text_for_change = text_for_change
        self.treeWidget = treeWidget
        self.subcategory = subcategory
        super(QtWidgets.QMainWindow).__init__()
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(275, 177)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 110, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 231, 31))
        self.textEdit.setObjectName("textEdit")
    
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 30, 191, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.additional_action(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "добавить "))
        self.label.setText(_translate("Form", "имя для категории"))

    def edit_category_handler(self,tree_widget):
        #
        print('this edit')

    def new_category_handler(self,tree_widget):
        #put to base 
        #rewrite 
        rowcount = self.treeWidget.topLevelItemCount()
        self.treeWidget.addTopLevelItem(QtWidgets.QTreeWidgetItem(rowcount))
        category_name = self.textEdit.toPlainText()
        if category_name != None:
            self.treeWidget.topLevelItem(rowcount).setText(0,category_name)
            db =Bicycle_db()
            #get_last_id
            id = db.edit('select max(id) from categories')
            schema = ','.join(db.schema['categories'])
            #INSERT INTO `categories`(`id`,`name`,`parent_id`,`export`) VALUES (214,"es",-1,0);
            query = "insert into categories({}) values({},{},-1,0)".format(schema,214,'"'+category_name+'"')
            res = db.edit(query)
            print(res)
        

            

    def add_subcategory_handler(self,tree_widget):
        rowcount = self.treeWidget.topLevelItemCount()
        category_name = self.textEdit.toPlainText()
        #subgory is item for need child
        self.subcategory.addChild(QtWidgets.QTreeWidgetItem(list(category_name)))

    def additional_action(self,Form):
        _translate = QtCore.QCoreApplication.translate
        if self.text_for_change:
            self.textEdit.setText(self.text_for_change)
            self.pushButton.setText(_translate("Form", "изменить"))
            self.label.setText(_translate("Form", "новое имя для категории"))
            self.pushButton.clicked.connect(lambda:self.edit_category_handler(self.treeWidget))
        elif self.subcategory:
            self.pushButton.setText(_translate("Form", "добавить"))
            self.label.setText(_translate("Form", "имя для субкатегории"))
            self.pushButton.clicked.connect(lambda:self.add_subcategory_handler(self.treeWidget))
        else:
            #if it's new category
            self.pushButton.clicked.connect(lambda:self.new_category_handler(self.treeWidget))



