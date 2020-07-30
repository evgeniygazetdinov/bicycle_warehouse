from  PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtCore import *
import sys
import os
import sqlite3

class Bicycle_db():
    def __init__(self):
        self.name = 'bicycle_db.sqlite'
        self.base_path = os.getcwd()+'/'+self.name
        #if not os.path.exists(self.base_path):
        self.db = self.create_db()
        if not os.path.exists(self.base_path):
            if self.db.open():
                query = QSqlQuery()
                query.exec_("CREATE TABLE [categories] ( [id] integer, [name] text, [parent_id] integer, [export] integer );")
                query.exec_("CREATE TABLE [basket] ( [id] integer, [price] text, [qty] integer, [total_price] integer, [article] text, [payment] text, [profit] integer, [dated] text, [article_old] text, [name] text );")
                query.exec_("CREATE TABLE [goods] ( [article_old] text, [name] text, [qty] integer, [buy] real, [sell] real, [profit] text, [category] text, [currency] text, [sell_uah] integer, [article] integer )")
                query.exec_("CREATE TABLE [settings] ( [Код] integer, [name] text, [value] text, [type] text );")


    def create_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.base_path)
        return db
    
    def edit(self, query):
        if self.db.open():
            sql_query = QSqlQuery()
            res = sql_query.exec_(query)
            self.db.close()


    def select(self, query):
        if self.db.open():
            res = []
            sql_query = QSqlQuery()
            sql_query.exec_(query)
            while sql_query.next():
                    res.append(sql_query.value(0)) 
            
            self.db.close()    
            return res


    def put_csv_into_table(file,table):
        pass


    def put_dump(self):
        old_base = sqlite3.connect('output.sqlite')

        new_base = sqlite3.connect(self.base_path)
        old_base.backup(new_base)
        old_base.close()
        
      





if __name__ =="__main__":
    db = Bicycle_db()
    db.put_dump()    
