from  PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtCore import *
import sys
import os

class Bicycle_db():
    def __init__(self):
        self.name = 'bicycle_db.sqlite'
        self.base_path = os.getcwd()+'/'+self.name
        #if not os.path.exists(self.base_path):
        db = self.create_db()
        if db.open():
            query = QSqlQuery()
            query.exec_("create table good(id int primary key, article_st varchar(20) , article_number int(30), good_name varchar(50), purchase real(3),markup_on_price decimal(3), sale_price real(2), complect int(5), grivna_price int(6))")
            query.exec_("""CREATE TABLE categories (
                    category_id   int PRIMARY KEY,
                    category_name varchar(10),
                    goods  int(3));""")

            #query.exec_("create table category (id int primary key, category_name varchar(30), goods INTEGER , FOREIGN KEY(good_id) REFERENCES good(good_id))")
            
            db.close()
            print('executed')

    def create_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.base_path)
        return db



if __name__ =="__main__":
    db = Bicycle_db()