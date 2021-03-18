import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QTableWidget, QTableWidgetItem

import Grades_design
from Database import get_table


class Main_window(QtWidgets.QMainWindow, Grades_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = get_table()
        self.textBrowser.setText(self.data.to_string())