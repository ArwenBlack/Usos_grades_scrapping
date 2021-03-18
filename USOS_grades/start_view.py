import sys

from PyQt6 import QtWidgets

import Grades_design
import grades_view
import start_page
from Database import get_table
from main import to_account


class Main_window(QtWidgets.QMainWindow, start_page.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_login_data)

    def get_login_data(self):
        page = self.comboBox.currentText()
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        to_account(page, name, password)
        self.w = grades_view.Main_window()
        self.w.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
