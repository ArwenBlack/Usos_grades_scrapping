import sys

from PyQt6 import QtWidgets

import start_page


class Main_window(QtWidgets.QMainWindow, start_page.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
