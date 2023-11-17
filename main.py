import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = QTableWidget()
        uic.loadUi('main.ui', self)
        self.fill_table()

    def fill_table(self):
        db = QSqlDatabase.addDatabase('SQLITE')
        db.setDatabaseName('coffe.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffe')
        model.select()

        self.view.setModel(model)  # todo исправить таблицу


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
