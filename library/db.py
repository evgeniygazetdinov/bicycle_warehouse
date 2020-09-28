from PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtCore import *
import sys
import os
import sqlite3
import csv
import csv_to_sqlite


class Bicycle_db:
    def __init__(self):
        self.name = "bicycle_db.sqlite"
        self.base_path = os.getcwd() + "/" + self.name
        self.query_creation = [
            """CREATE TABLE [categories] ( [id] integer,
                [name] text, [parent_id] integer, [export] integer );""",
            """CREATE TABLE [basket] ( [id] integer, [price] text, 
                [qty] integer, [total_price] integer, [article] text,
                [payment] text, [profit] integer, [dated] text, 
                [article_old] text, [name] text );""",
            """CREATE TABLE [goods] ( [article_old] text,
                [name] text, [qty] integer, [buy] real,
                [sell] real, [profit] text, [category] text,
                [currency] text, [sell_uah] integer, 
                [article] integer )""",
            """CREATE TABLE [settings] ( [Код] integer, 
                [name] text, [value] text, [type] text );""",
            """CREATE TABLE [cur_category] ( [name] text );""" ]
        self.tables_scheme = ["categories", "basket", "goods", "settings"]
        self.schema = {
            "categories": ["id", "name", "parent_id", "export"],
            "basket": [
                "id",
                "price",
                "qty",
                "total_price",
                "article",
                "payment",
                "profit",
                "dated",
                "article_old",
                "name",
            ],
            "goods": [
                "article_old",
                "name",
                "qty",
                "buy",
                "sell",
                "profit",
                "category",
                "currency",
                "sell_uah",
                "article",
            ],
            "settings": ["Код", "name", "value", "type"],
        }

        if not os.path.exists(self.base_path):
            self.db = self.create_db()
            self.connection = sqlite3.connect(self.name)
            for query in self.query_creation:
                self.edit(query)
        else:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

    def create_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.base_path)
        return db

    def insert(self, query):
        query_res = self.cursor.execute(query)
        res = query_res.fetchall()
        self.connection.commit()
        return res

    def edit(self, query):
        db =  self.connection
        cursor = db.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def select(self, query):
        if self.db.open():
            res = []
            sql_query = QSqlQuery()
            sql_query.exec_(query)
            while sql_query.next():
                res.append(sql_query.value(0))
            self.db.close()
            return res

    def close(self):
        self.connection.close()

    def put_csv_into_table(file, table):
        pass

    def get_tables_from_mdb_dump(self, mdb_db):
        tables = []
        for tbl in mdb.list_tables(mdb_db):
            tables.append(tbl)
        return tables

    def exists(self, table_name):
        query = "SELECT * FROM sqlite_master WHERE type='table' AND  name='{}'".format(
            table_name
        )
        res = self.insert(query)
        if len(res) > 0:
            return True
        return False

    def make_db_from_csv_files(self):
        options = csv_to_sqlite.CsvOptions(typing_style="full")
        input_files = ("ui_templates/" + table + ".csv" for table in self.tables_scheme)
        csv_to_sqlite.write_csv(input_files, self.name, options)

    def table_from_csv_table(table, filename, database_name):
        cur = con.cursor()
        cur.executescript(
            """
            DROP TABLE IF EXISTS {};
            CREATE TABLE {} ();
        """,
            format(table, schema[table],),
        )  # checks to see if table exists and makes a fresh table.

        with open(filename, "rb") as f:  # CSV file input
            reader = csv.reader(
                f, delimiter=","
            )  # no header information with delimiter
            for row in reader:
                to_db = [
                    unicode(row[0], "utf8"),
                    unicode(row[1], "utf8"),
                ]  # Appends data from CSV file representing and handling of text
                cur.execute("INSERT INTO neto (COL1, COL2) VALUES(?, ?);", to_db)
                con.commit()
        con.close()

    def put_dump(self, table, filename, database_name):
        pass


if __name__ == "__main__":
    db = Bicycle_db()
    db.put_dump()
